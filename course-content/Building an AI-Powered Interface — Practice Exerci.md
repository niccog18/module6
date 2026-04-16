# Building an AI-Powered Interface — Practice Exercise

## AI Assistant with Context

**Objective:** Build a chat interface with customizable context, combining chat history, sidebar controls, and AI integration.

**Time:** 45 minutes

**What you’ll build:**

Create `ai_assistant.py` — a chat app with the following features:

**Requirements:**

1. **Chat interface** using `st.chat_message()` and `st.chat_input()`
2. **Chat history** stored in `st.session_state` and re-rendered on every run
3. **Sidebar with:**
    - A system prompt text area (editable personality for the AI)
    - Context checkboxes (e.g., "Include Python expertise", "Include web development context", "Include AI/ML context") — when checked, these append relevant context to the system prompt
    - A "Clear Chat" button that resets the history
4. **Loading indicator** — show `st.spinner("Thinking...")` while generating a response
5. **Response generation** — use a real API (OpenAI, Anthropic) if the student has a key, or a meaningful mock that references the prompt and selected context checkboxes

**Mock response hint:**

```python
def mock_response(prompt, contexts):
    context_str = ", ".join(contexts) if contexts else "general knowledge"
    response = (f"Based on my {context_str} expertise, here's my take on "
                f"'{prompt[:40]}': [This would be a real AI response in production. "
                f"The system prompt and {len(contexts)} context areas would shape "
                f"how the AI responds.]")
    for word in response.split():
        yield word + " "
        time.sleep(0.03)
```

**Deliverable:** A running chat app with sidebar context controls, persistent history, and streaming responses.

**Why this exercise?** This is the exact interface pattern used by most AI products: a chat area, customizable system context, and streaming responses. You’re building a simplified version of what ChatGPT’s custom instructions do.