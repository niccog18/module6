"""
L12b — Conversation Export  (Stretch Challenge)
=================================================
Run with:
    streamlit run solution.py

Extends the AI Chat app with two export features:
    1. "Copy Conversation" — formats history as plain text → st.code()
    2. "Download Chat"     — st.download_button() to save as .txt

Key concepts:
    st.code(text, language="text"):
        Renders text in a monospace code block.
        Includes a built-in "Copy" button in the top-right corner.
        language="text" disables syntax highlighting.

    st.download_button(label, data, file_name, mime):
        Renders a button that triggers a file download in the browser.
        data   — the file content as str or bytes
        file_name — the suggested filename shown in the download dialog
        mime   — MIME type (e.g. "text/plain", "application/pdf")
        Does NOT save anything server-side — the browser handles the download.
"""

import streamlit as st
import time
from datetime import datetime

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Chat with Export",
    page_icon="🤖",
    layout="centered",
)

# ── Session state ──────────────────────────────────────────────────────────────
if "messages"     not in st.session_state: st.session_state.messages     = []
if "api_key"      not in st.session_state: st.session_state.api_key      = ""
if "show_export"  not in st.session_state: st.session_state.show_export  = False

# ── Helpers ───────────────────────────────────────────────────────────────────
def format_conversation() -> str:
    """Format chat history as plain text for copy/download."""
    if not st.session_state.messages:
        return "(No messages yet)"

    lines = [
        f"AI Chat Export",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 50,
        "",
    ]
    for msg in st.session_state.messages:
        role  = "You" if msg["role"] == "user" else "Assistant"
        lines.append(f"[{role}]")
        lines.append(msg["content"])
        lines.append("")  # blank line between messages
    return "\n".join(lines)


def mock_stream(user_message: str):
    """Simple mock streaming generator."""
    responses = {
        "python":    "Python is a versatile language known for readability.",
        "streamlit": "Streamlit re-runs your script from top to bottom on every interaction.",
        "export":    "You can export chat history with st.download_button — it triggers a browser download.",
    }
    lower    = user_message.lower()
    response = next(
        (text for keyword, text in responses.items() if keyword in lower),
        f"Mock response to: '{user_message}'. Add an API key for real answers!",
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.04)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input("OpenAI API Key (optional)", type="password")
    st.session_state.api_key = api_key

    st.divider()
    st.subheader("💾 Export")

    # ── "Copy Conversation" button ─────────────────────────────────────────
    # Toggles the display of a st.code() block in the sidebar.
    # st.code() has a built-in copy-to-clipboard button in the top-right corner.
    if st.button("📋 Copy Conversation", use_container_width=True):
        if not st.session_state.messages:
            st.warning("No messages to export yet.")
        else:
            st.session_state.show_export = not st.session_state.show_export

    if st.session_state.show_export:
        formatted = format_conversation()
        # st.code() renders text in a monospaced block.
        # language="text" means no syntax highlighting — plain text.
        # The built-in copy button in the top-right lets the user copy to clipboard.
        st.code(formatted, language="text")

    st.divider()

    # ── "Download Chat" button ─────────────────────────────────────────────
    # st.download_button() creates a download link.
    # When clicked, the browser downloads the data as a file.
    # Nothing is saved on the server.
    formatted_text = format_conversation()
    filename = f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"

    st.download_button(
        label="⬇️ Download Chat (.txt)",
        data=formatted_text,              # file content (str or bytes)
        file_name=filename,               # suggested filename in download dialog
        mime="text/plain",                # MIME type
        use_container_width=True,
        disabled=not st.session_state.messages,   # disabled when no messages
    )

    if not st.session_state.messages:
        st.caption("Send at least one message to enable export.")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages    = []
        st.session_state.show_export = False
        st.rerun()

    st.caption(f"Messages: {len(st.session_state.messages)}")

# ── Main chat UI ───────────────────────────────────────────────────────────────
st.title("🤖 AI Chat with Export")

if not api_key:
    st.info("No API key — using mock responses. Check the sidebar for export options!")

# Render history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        full_response = st.write_stream(mock_stream(prompt))

    st.session_state.messages.append({"role": "assistant", "content": full_response})
