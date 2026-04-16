# User Input, Forms & State Management — Stretch Solution Download

**Reference solution:** `module-06/solutions/quiz-timer/`

The reference solution adds a 15-second countdown timer per question using `st.empty()` and `time.sleep()`:

1. Creates a placeholder with `st.empty()`
2. Loops from 15 to 0, updating the placeholder each second
3. When time expires, auto-advances to the next question via `st.rerun()`

**Important caveat:** `time.sleep()` blocks the entire Streamlit script during the countdown — users can't interact with widgets while the timer runs. For production apps, you'd use JavaScript callbacks or `st.fragment` for non-blocking timing.

**Key concept:** `st.empty()` creates a reusable placeholder that updates in-place rather than appending new content. This pattern is used for loading indicators, status messages, and streaming AI responses.

**Note:** Your timer implementation may use different durations or display formats. The key is demonstrating the `st.empty()` update pattern.