# Building an AI-Powered Interface — Stretch Solution Download

**Reference solution:** `module-06/solutions/chat-export/`

The reference solution adds conversation export with two features:

1. **Copy Conversation button:** Formats the full chat history as plain text with user/AI labels, displays in `st.code()` for easy copying
2. **Download Chat button:** Uses `st.download_button()` to save the conversation as a `.txt` file

Both handle the empty conversation case gracefully.

**Key concepts:**

- `st.code(text, language=None)` renders text in a monospace block with a built-in copy button (recent Streamlit versions)
- `st.download_button()` lets users download generated content without a server-side file

**Note:** Your export format may differ. The key is formatting session state data into a downloadable/copyable format.