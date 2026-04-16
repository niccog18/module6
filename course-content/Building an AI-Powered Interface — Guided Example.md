# Building an AI-Powered Interface — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 12 min — "Build ai_chat.py: full chat interface with sidebar settings, API key input, system prompt, model selector, chat history, streaming responses, and mock fallback."]`

Create `ai_chat.py` — a complete AI chat interface:

```python
import streamlit as st
import time

st.set_page_config(page_title="AI Chat", page_icon="🤖", layout="centered")

# --- Session State Init ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Sidebar: Settings ---
with st.sidebar:
    st.title("⚙️ Settings")

    api_key = st.text_input("OpenAI API Key", type="password",
                             placeholder="sk-... (optional)")

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful AI assistant for students learning AI engineering.",
        help="This sets the AI's personality and behavior."
    )

    model = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])

    st.divider()

    use_real_api = api_key and len(api_key) > 10
    if use_real_api:
        st.success("Using real OpenAI API")
    else:
        st.info("No API key — using mock responses")

    st.divider()
    st.metric("Messages", len(st.session_state["messages"]))

    if st.button("🗑️ Clear Chat"):
        st.session_state["messages"] = []
        st.rerun()

# --- Mock Response Generator ---
def mock_stream(prompt):
    """Fake streaming response for demo purposes."""
    responses = {
        "default": f"That's a great question about '{prompt[:50]}'. As an AI engineering student, you'll encounter this topic in upcoming modules. The key concepts involve understanding how models process input, generate responses, and handle context. Keep exploring and building!"
    }
    response = responses["default"]
    for word in response.split():
        yield word + " "
        time.sleep(0.03)

# --- Real API Call ---
def real_stream(messages, api_key, model):
    """Stream from OpenAI API."""
    import openai  # Import here so app works without openai installed
    client = openai.OpenAI(api_key=api_key)
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_prompt}] + messages,
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:  # Some chunks have no content
            yield chunk.choices[0].delta.content

# --- Main Chat Interface ---
st.title("🤖 AI Chat")

# Re-render all previous messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle new input
if prompt := st.chat_input("Ask me anything..."):
    # Display and store user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate and stream assistant response
    with st.chat_message("assistant"):
        if use_real_api:
            try:
                response = st.write_stream(
                    real_stream(st.session_state["messages"], api_key, model)
                )
            except Exception as e:
                response = f"API Error: {str(e)}"
                st.error(response)
        else:
            response = st.write_stream(mock_stream(prompt))

    # Store assistant response
    st.session_state["messages"].append({"role": "assistant", "content": response})
```

Run it:

```bash
streamlit run ai_chat.py
```

---

## What You Should See

1. A clean chat interface with a text input pinned to the bottom
2. A sidebar with API key input (masked), system prompt, model selector, message count, and Clear button
3. Type a message — it appears in a user bubble, then the AI response streams in word by word
4. Chat history persists as you continue the conversation
5. Clear chat resets everything

Without an API key, you get mock responses. With one, you get real AI responses streamed in real-time.

`[DIAGRAM PLACEHOLDER: Screenshot of the ai_chat.py showing a multi-turn conversation with the sidebar settings panel visible]`

---

## Key Patterns

**History re-rendering:** The `for message in st.session_state["messages"]` loop at the top displays all previous messages. Without this, each re-run would show a blank page.

**Walrus operator (`:=`):** `if prompt := st.chat_input(...)` assigns and checks in one line. It’s a Python 3.8+ feature you’ll see in many Streamlit examples.

**Stream generator:** Both `mock_stream` and `real_stream` are generator functions that `yield` text chunks. `st.write_stream()` consumes these generators and displays each chunk as it arrives.

**Mock fallback:** The app works with or without an API key. This is good practice for any demo or educational app.