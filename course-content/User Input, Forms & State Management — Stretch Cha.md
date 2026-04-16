# User Input, Forms & State Management — Stretch Challenge

## Countdown Timer

Add a countdown timer to each question that auto-advances if the student doesn’t answer in time.

**Challenge:** Use `st.empty()` and `time.sleep()` to create a 15-second countdown per question.

```python
import time

timer_placeholder = st.empty()  # Creates a slot we can update

for seconds_left in range(15, 0, -1):
    timer_placeholder.write(f"⏰ Time remaining: **{seconds_left}** seconds")
    time.sleep(1)

# Time's up! Auto-advance to next question
timer_placeholder.write("⏰ **Time's up!**")
st.session_state["current_question"] += 1
st.session_state["answered"] = False
time.sleep(1)
st.rerun()
```

**Important caveat:** `time.sleep()` blocks the entire Streamlit script during the countdown. This means the user can’t interact with widgets while the timer is running. For a production app, you’d use JavaScript callbacks or Streamlit’s `st.fragment` for more sophisticated timing. But for learning the `st.empty()` pattern, this approach works.

`st.empty()` is a powerful tool — it creates a placeholder that can be updated in-place, rather than appending new content below. You’ll use it for loading indicators, status messages, and streaming AI responses.