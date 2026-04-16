# User Input, Forms & State Management — Practice Exercise

## Stateful Quiz App

**Objective:** Build a multi-question quiz app that uses session state to track the current question, score, and user progress.

**Time:** 40 minutes

**What you’ll build:**

Create `quiz_app.py` — a quiz application with the following features:

**Requirements:**

1. **5 hardcoded questions** with multiple-choice answers (use topics from this course — HTML, CSS, JavaScript, Python, APIs)
2. **Session state** tracking:
    - `current_question` (index of the current question)
    - `score` (number of correct answers)
    - `answered` (whether the current question has been answered)
3. **Answer flow:** When the user selects an answer and clicks Submit:
    - Show whether they were correct or incorrect (using `st.success()` or `st.error()`)
    - Show the correct answer if they were wrong
    - Show a "Next" button to advance
4. **Progress indicator:** "Question 2 of 5" and a progress bar
5. **Results screen:** After the last question, show the final score and a "Restart" button that resets all session state

**Data structure hint:**

```python
questions = [
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Tech Modern Language",
                    "Hyper Transfer Markup Language", "Home Tool Markup Language"],
        "answer": 0  # Index of the correct option
    },
    # ... 4 more questions
]
```

**Deliverable:** A running Streamlit quiz app that tracks score across questions, shows feedback, and displays a results screen.

**Why this exercise?** You’re practicing the complete session state workflow: initialize, read, update, and reset. The same patterns apply to building any stateful interface — chat apps, multi-step forms, shopping carts, or interactive AI tools.