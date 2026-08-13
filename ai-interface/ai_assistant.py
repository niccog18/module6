import streamlit as st
import time


# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Assistant")
st.write("Chat with an AI assistant using customizable context.")


# ---------------------------------------------------------
# Mock AI response
# ---------------------------------------------------------

def mock_response(prompt, system_prompt, contexts):
    context_str = ", ".join(contexts) if contexts else "general knowledge"

    response = (
        f"Based on my {context_str} expertise, here's my take on "
        f"'{prompt[:40]}': [This would be a real AI response in production. "
        f"The system prompt and {len(contexts)} context areas would shape "
        f"how the AI responds.]"
    )

    # The system prompt is included as part of the AI's context.
    # This mock does not generate a real AI response, but it demonstrates
    # how the prompt would be passed to an AI API in a real application.
    if system_prompt:
        response += (
            f" Your customized system instructions are also being "
            f"considered."
        )

    for word in response.split():
        yield word + " "
        time.sleep(0.03)


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:
    st.header("Assistant Settings")

    # Editable system prompt
    system_prompt = st.text_area(
        "System Prompt",
        value=(
            "You are a helpful AI assistant. "
            "Answer questions clearly and helpfully."
        ),
        height=150
    )

    st.subheader("Context")

    # Context checkboxes
    python_context = st.checkbox(
        "Include Python expertise"
    )

    web_context = st.checkbox(
        "Include web development context"
    )

    ai_context = st.checkbox(
        "Include AI/ML context"
    )

    # Build selected context list
    contexts = []

    if python_context:
        contexts.append("Python")

    if web_context:
        contexts.append("web development")

    if ai_context:
        contexts.append("AI/ML")

    # -----------------------------------------------------
    # Combine system prompt with selected contexts
    # -----------------------------------------------------

    full_system_prompt = system_prompt

    if contexts:
        full_system_prompt += (
            "\n\nAdditional expertise/context: "
            + ", ".join(contexts)
        )

    st.divider()

    # Clear chat button
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------------------------------------------------
# Display previous chat messages
# ---------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------------------------------------
# Chat input
# ---------------------------------------------------------

prompt = st.chat_input("What would you like to ask?")


if prompt:

    # Add user's message to history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.write_stream(
                mock_response(
                    prompt,
                    full_system_prompt,
                    contexts
                )
            )

    # Save assistant response to chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

