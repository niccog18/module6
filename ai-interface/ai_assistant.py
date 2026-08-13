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
    # This mock demonstrates how the prompt would be passed
    # to an AI API in a real application.
    if system_prompt:
        response += (
            " Your customized system instructions are also being "
            "considered."
        )

    # Stream the response word-by-word
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

    # -----------------------------------------------------
    # Clear Chat button
    # -----------------------------------------------------

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # -----------------------------------------------------
    # Conversation Export
    # -----------------------------------------------------

    if st.button("📋 Copy Conversation", use_container_width=True):

        if st.session_state["messages"]:

            export_text = ""

            for msg in st.session_state["messages"]:

                role = (
                    "You"
                    if msg["role"] == "user"
                    else "AI"
                )

                export_text += (
                    f"{role}: {msg['content']}\n\n"
                )

            st.code(
                export_text,
                language=None
            )

            st.caption(
                "Select all the text above and copy it "
                "(Cmd/Ctrl + C)"
            )

            # Bonus: Download conversation as a text file
            st.download_button(
                "💾 Download Chat",
                data=export_text,
                file_name="chat_export.txt",
                mime="text/plain"
            )

        else:
            st.info("No messages to export yet.")


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
