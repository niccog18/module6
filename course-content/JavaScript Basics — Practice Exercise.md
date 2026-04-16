# JavaScript Basics — Practice Exercise

## Interactive Flashcard App

**Objective:** Build a small interactive web app using DOM manipulation and event listeners — reinforcing how JavaScript makes pages dynamic.

**Time:** 30 minutes

**What you’ll build:**

A single HTML file (`flashcards.html`) that displays flashcard-style Q&A pairs one at a time.

**Requirements:**

1. Create an array of **5 question/answer pairs** related to topics from this course. For example:
    - Q: "What does HTTP stand for?" / A: "HyperText Transfer Protocol"
    - Q: "What status code means ‘Not Found’?" / A: "404"
    - Q: "What does CSS stand for?" / A: "Cascading Style Sheets"
    - Q: "What does DOM stand for?" / A: "Document Object Model"
    - Q: "What Python library do we use for HTTP requests?" / A: "requests"
2. Display the **current question** on screen
3. Add a **"Show Answer" button** — when clicked, the answer appears below the question
4. Add a **"Next" button** — moves to the next card and hides the answer
5. Show a **progress indicator**: "Card 1 of 5", "Card 2 of 5", etc.
6. When the user reaches the last card and clicks Next, loop back to Card 1

**Deliverable:** A working `flashcards.html` file that you can open in a browser. No external libraries or CSS files needed — inline styles are fine.

**Hints:**

- Store the current card index in a `let` variable
- Use `textContent` to update the question, answer, and progress text
- Use `style.display = "none"` and `style.display = "block"` to show/hide the answer
- Use the modulo operator (`%`) to loop back to the start: `currentIndex = (currentIndex + 1) % cards.length`

**Why this exercise?** You’re practicing the core JavaScript pattern: store state in a variable, listen for events, update the DOM. This is the same pattern that drives every interactive web app — and the same pattern Streamlit abstracts away for you in Python.