# User Input, Forms & State Management — Solution Download

**GitHub:** `module-06-web-streamlit/solutions/exercises/quiz-app/`

Compare your solution to the reference. Key things to check:

- Do you initialize `current_question`, `score`, and `answered` in session state with the `if "key" not in st.session_state` pattern?
- Does clicking "Next" advance to the next question without losing the score?
- Does the results screen show the correct final score?
- Does "Restart" actually reset all session state values back to their initial values?
- Did you use `st.rerun()` after state changes to update the display?

Different question content, styling, and flow approaches are all valid.