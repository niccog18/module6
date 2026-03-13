"""
L12 — AI Chat Interface  (Solution)
=====================================
Run with:
    streamlit run solution.py

Key concepts:
    Chat history pattern:
        History is stored in st.session_state as a list of
        {"role": "user"|"assistant", "content": "..."} dicts.
        On EVERY re-run, the ENTIRE history is re-rendered from scratch.
        This looks like the messages persist, but they're actually
        redrawn each time using the stored data.

    st.chat_message(role):
        Context manager that renders a chat bubble.
        role "user" → right-aligned / user icon
        role "assistant" → left-aligned / bot icon

    st.chat_input(placeholder):
        A fixed-to-bottom input box. Returns the submitted text (or None).
        This is the recommended way to accept user input in a chat app.

    st.write_stream(generator):
        Renders the output of a generator function as a stream,
        appending text token by token. Great for demonstrating streaming
        LLM responses. Works with real OpenAI stream iterators too.
"""

import streamlit as st
import time

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Chat",
    page_icon="🤖",
    layout="centered",
)

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    # messages is a list of {"role": ..., "content": ...} dicts.
    # It starts empty. Each new message is appended.
    st.session_state.messages = []

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    # API key input — type="password" masks the input
    api_key = st.text_input(
        "OpenAI API Key (optional)",
        type="password",
        placeholder="sk-...",
        help="Leave blank to use the built-in mock responses.",
    )
    st.session_state.api_key = api_key

    # System prompt — affects assistant behaviour in real OpenAI calls
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful assistant for an AI engineering bootcamp. "
              "Answer questions about Python, APIs, Streamlit, and web development.",
        height=100,
    )

    # Model selector
    model = st.selectbox(
        "Model",
        options=["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
    )

    st.divider()

    # Clear button — resets the chat history
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # Message count — updated every re-run
    st.caption(f"Messages in history: {len(st.session_state.messages)}")

# ── Page title ────────────────────────────────────────────────────────────────
st.title("🤖 AI Chat Interface")

if not st.session_state.api_key:
    st.info(
        "No API key provided — using **mock responses**. "
        "Add your OpenAI key in the sidebar to use real GPT responses."
    )

# ══════════════════════════════════════════════════════════════════════════════
# RENDER CHAT HISTORY
# ──────────────────────────────────────────────────────────────────────────────
# This loop runs on EVERY re-run and re-renders the full history.
# Messages appear to persist because they're stored in session_state and
# re-drawn each time. The UI always reflects the current state of messages.
# ══════════════════════════════════════════════════════════════════════════════
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Mock response generator ───────────────────────────────────────────────────
def mock_stream(user_message: str):
    """
    Generator that yields text tokens one by one, simulating streaming.
    Used when no API key is provided.

    st.write_stream() calls next() on this generator repeatedly,
    displaying each chunk as it arrives. This creates a typewriter effect.
    """
    responses = {
        "python":     "Python is a versatile language known for readability. In this bootcamp you've used it for scripting, APIs, and data work.",
        "streamlit":  "Streamlit turns Python scripts into interactive web apps. Every widget interaction triggers a full re-run — that's the core model!",
        "fastapi":    "FastAPI is a modern Python web framework. It uses type hints and Pydantic to automatically validate request bodies.",
        "api":        "APIs (Application Programming Interfaces) let programs talk to each other. REST APIs use HTTP methods: GET, POST, PUT, DELETE.",
        "html":       "HTML provides the structure of web pages using semantic elements like <header>, <main>, <section>, and <article>.",
        "css":        "CSS styles HTML elements. Key concepts: box model (margin/padding/border), flexbox for layout, and @media for responsive design.",
        "session":    "st.session_state lets you persist data across Streamlit re-runs. Always initialise with `if 'key' not in st.session_state:`",
    }

    lower = user_message.lower()
    response = next(
        (text for keyword, text in responses.items() if keyword in lower),
        f"Great question about '{user_message}'! This is a mock response. Add an OpenAI API key in the sidebar to get real AI-powered answers.",
    )

    # Yield one word at a time with a small delay to simulate streaming
    for word in response.split():
        yield word + " "
        time.sleep(0.04)


# ── Real OpenAI streaming (used when API key is provided) ────────────────────
def real_stream(messages_history: list, system: str, model_name: str):
    """
    Generator that calls the OpenAI API with streaming enabled.
    Yields text chunks as they arrive.
    Falls back to mock if import fails.
    """
    try:
        from openai import OpenAI
        client = OpenAI(api_key=st.session_state.api_key)

        system_msg = [{"role": "system", "content": system}]
        stream = client.chat.completions.create(
            model=model_name,
            messages=system_msg + messages_history,
            stream=True,     # receive tokens as they are generated
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    except ImportError:
        yield "OpenAI package not installed. Run: pip install openai"
    except Exception as e:
        yield f"Error calling OpenAI API: {e}"


# ── Chat input ────────────────────────────────────────────────────────────────
# st.chat_input() renders a sticky input at the bottom of the page.
# It returns the submitted text after the user presses Enter, otherwise None.
# This triggers a re-run, so the code below runs only when there's input.
if prompt := st.chat_input("Ask me anything about web development…"):

    # 1. Add user message to history and render it immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Generate and stream the assistant response
    with st.chat_message("assistant"):
        if st.session_state.api_key:
            generator = real_stream(st.session_state.messages, system_prompt, model)
        else:
            generator = mock_stream(prompt)

        # st.write_stream(generator) renders the streamed text token by token
        # and returns the full assembled string when the generator is exhausted.
        full_response = st.write_stream(generator)

    # 3. Store the complete response in history for future re-renders
    st.session_state.messages.append({"role": "assistant", "content": full_response})
