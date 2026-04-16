# Building an AI-Powered Interface — Stretch Challenge

## Conversation Export

Chat conversations are useful to save and share. Add an export feature to your AI assistant.

**Challenge:** Add a "Copy Conversation" button in the sidebar that:

1. Formats the entire chat history as plain text with clear user/assistant labels
2. Displays it in a `st.code()` block for easy copying

```python
if st.sidebar.button("📋 Copy Conversation"):
    if st.session_state["messages"]:
        export_text = ""
        for msg in st.session_state["messages"]:
            role = "You" if msg["role"] == "user" else "AI"
            export_text += f"{role}: {msg['content']}\n\n"

        st.sidebar.code(export_text, language=None)
        st.sidebar.caption("Select all the text above and copy it (Cmd/Ctrl + C)")
    else:
        st.sidebar.info("No messages to export yet.")
```

`st.code()` renders text in a monospace code block with a built-in copy button (in recent Streamlit versions). Setting `language=None` disables syntax highlighting, treating it as plain text.

**Bonus:** Add a "Download as .txt" option using `st.download_button()`:

```python
st.sidebar.download_button(
    "💾 Download Chat",
    data=export_text,
    file_name="chat_export.txt",
    mime="text/plain"
)
```