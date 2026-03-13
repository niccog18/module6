"""
L12 — AI Chat Interface  (STARTER)
=====================================
Run with:
    streamlit run solution.py

Your goal: build a Streamlit chat interface with streaming responses.

Required features:
    1. Sidebar: API key input (type="password"), system prompt text area,
       model selector, Clear button, message count
    2. Chat history in session state (list of {"role": ..., "content": ...})
    3. Full chat display using st.chat_message() for each message
    4. st.chat_input() for user messages
    5. Mock response generator for students without an API key
    6. st.write_stream() to display the streaming response

Key concepts:
    Chat history pattern:
        Store messages as a list in session state:
            [{"role": "user", "content": "Hello"},
             {"role": "assistant", "content": "Hi!"}]
        On every re-run, iterate through ALL messages and re-render them.
        This is why history appears to persist — it's stored in session_state
        and re-drawn each time from scratch.

    st.chat_message(role):
        Context manager that renders a styled chat bubble.
        `with st.chat_message("user"): st.markdown(text)`

    st.chat_input(placeholder):
        Fixed-to-bottom input; returns submitted text or None.

    st.write_stream(generator):
        Renders text from a generator token by token (typewriter effect).
        Returns the complete assembled string when done.
"""

import streamlit as st
import time

# ── Page config ────────────────────────────────────────────────────────────
# TODO: st.set_page_config(page_title, page_icon, layout="centered")

# ── Session state ──────────────────────────────────────────────────────────
# TODO: Initialise "messages" to [] — a list of {"role": ..., "content": ...} dicts
# TODO: Initialise "api_key" to ""

# ── Sidebar ────────────────────────────────────────────────────────────────
# TODO: with st.sidebar:
#   - st.header("Settings")
#   - API key: st.text_input("OpenAI API Key", type="password")
#     Store in st.session_state.api_key
#   - System prompt: st.text_area with a default value
#   - Model: st.selectbox with ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]
#   - st.divider()
#   - Clear button: if clicked, set messages = [] and st.rerun()
#   - Caption showing message count

# ── Page title ─────────────────────────────────────────────────────────────
# TODO: st.title and info banner if no API key

# ══════════════════════════════════════════════════════════════════════════
# RENDER CHAT HISTORY
# ──────────────────────────────────────────────────────────────────────────
# TODO: Loop through st.session_state.messages
#       For each message, use `with st.chat_message(message["role"]):`
#       and display the content with st.markdown()
#
# IMPORTANT: This loop re-renders ALL messages on every re-run.
# Messages appear to persist because they're stored in session_state.

# ── Mock response generator ────────────────────────────────────────────────
# TODO: Implement mock_stream(user_message) as a generator function.
#   - Map keywords to responses (e.g. "python", "streamlit", "fastapi")
#   - yield one word at a time with time.sleep(0.04) between each
#   - This simulates streaming without needing an API key

def mock_stream(user_message: str):
    # TODO: implement
    # Example structure:
    # response = "some text based on the message"
    # for word in response.split():
    #     yield word + " "
    #     time.sleep(0.04)
    pass  # remove this line when implementing


# ── Chat input ─────────────────────────────────────────────────────────────
# TODO: Use `if prompt := st.chat_input("Ask me anything…"):`
#   Inside:
#   1. Append {"role": "user", "content": prompt} to st.session_state.messages
#   2. Render the user message with st.chat_message("user")
#   3. Render the assistant response with st.chat_message("assistant"):
#      - Use mock_stream(prompt) as the generator
#      - Call `full_response = st.write_stream(generator)`
#        st.write_stream renders the generator output token by token
#        and returns the complete string
#   4. Append {"role": "assistant", "content": full_response} to messages
