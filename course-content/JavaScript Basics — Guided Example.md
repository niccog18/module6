# JavaScript Basics — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 10 min — "Build interactive.html: dark mode toggle, character counter, and dynamic list. Show DOM manipulation in action with DevTools open to see changes."]`

Let’s build three small interactive features in one HTML file. Each one demonstrates a different DOM manipulation technique.

Create a file called `interactive.html`:

---

## Step 1: Set Up the HTML Shell

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Interactive Demo</title>
    <style>
        /* Inline styles for simplicity — just enough to see what’s happening */
        body { font-family: sans-serif; padding: 40px; max-width: 700px; margin: auto; transition: background-color 0.3s, color 0.3s; }
        .dark-mode { background-color: #1a1a2e; color: #e0e0e0; }
        .warning { color: #e74c3c; font-weight: bold; }
        .ok { color: #27ae60; }
        button { padding: 8px 16px; cursor: pointer; margin: 4px; }
        .task-item { padding: 8px; margin: 4px 0; background: #f0f0f0; border-radius: 4px; display: flex; justify-content: space-between; }
        .dark-mode .task-item { background: #2a2a4a; }
    </style>
</head>
<body>
    <!-- Feature 1: Dark Mode Toggle -->
    <!-- Feature 2: Character Counter -->
    <!-- Feature 3: Dynamic Task List -->

    <script>
        // All our JavaScript will go here
    </script>
</body>
</html>
```

---

## Step 2: Dark Mode Toggle (classList.toggle)

Add this HTML above the `<script>` tag:

```html
<h1>JavaScript Interactive Demo</h1>

<section>
    <h2>1. Dark Mode Toggle</h2>
    <button id="toggle-btn">Toggle Dark Mode</button>
</section>
<hr>
```

Now add this inside the `<script>` tag:

```jsx
// --- Feature 1: Dark Mode Toggle ---
const toggleBtn = document.querySelector("#toggle-btn");  // Find the button

toggleBtn.addEventListener("click", () => {
    // classList.toggle adds the class if missing, removes it if present
    document.body.classList.toggle("dark-mode");
});
```

Save and open in your browser. Click the button — the page should swap between light and dark mode. Click again and it swaps back. That’s `classList.toggle` in action: one line toggles the entire page’s appearance by adding or removing a CSS class.

---

## Step 3: Character Counter (input event + conditional styling)

Add this HTML below the first `<hr>`:

```html
<section>
    <h2>2. Character Counter</h2>
    <textarea id="text-input" rows="4" cols="50" placeholder="Type something..."></textarea>
    <p>Characters: <span id="char-count" class="ok">0</span> / 200</p>
</section>
<hr>
```

Add this JavaScript:

```jsx
// --- Feature 2: Character Counter ---
const textInput = document.querySelector("#text-input");    // The textarea
const charCount = document.querySelector("#char-count");    // The counter display
const MAX_CHARS = 200;

textInput.addEventListener("input", () => {
    // 'input' event fires on EVERY keystroke (unlike 'change' which fires on blur)
    const count = textInput.value.length;  // Current character count
    charCount.textContent = count;          // Update the displayed number

    // Change style based on how close to the limit
    if (count > MAX_CHARS) {
        charCount.className = "warning";     // Red — over limit
    } else if (count > MAX_CHARS * 0.8) {
        charCount.style.color = "#f39c12";   // Orange — getting close
        charCount.className = "";            // Clear any class
    } else {
        charCount.className = "ok";          // Green — plenty of room
    }
});
```

Save and refresh. Start typing in the textarea. The counter updates on every keystroke, turns orange when you pass 160 characters, and turns red and bold past 200.

Notice we used the `"input"` event, not `"change"`. The `input` event fires immediately on every keystroke. The `change` event only fires when the user leaves the field — not useful for a live counter.

---

## Step 4: Dynamic Task List (createElement, appendChild, remove)

Add this HTML:

```html
<section>
    <h2>3. Dynamic Task List</h2>
    <input type="text" id="task-input" placeholder="Add a task...">
    <button id="add-task-btn">Add</button>
    <div id="task-list"></div>
</section>
```

Add this JavaScript:

```jsx
// --- Feature 3: Dynamic Task List ---
const taskInput = document.querySelector("#task-input");
const addTaskBtn = document.querySelector("#add-task-btn");
const taskList = document.querySelector("#task-list");

function addTask() {
    const taskText = taskInput.value.trim();  // Get input, remove whitespace
    if (taskText === "") return;               // Don't add empty tasks

    // Create a new div element for the task
    const taskItem = document.createElement("div");
    taskItem.className = "task-item";

    // Create a span for the task text
    const textSpan = document.createElement("span");
    textSpan.textContent = taskText;

    // Create a delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.addEventListener("click", () => {
        taskItem.remove();  // Remove the entire task item from the DOM
    });

    // Assemble: add the text and button to the task item
    taskItem.appendChild(textSpan);   // Put text inside the task div
    taskItem.appendChild(deleteBtn);  // Put delete button inside the task div

    // Add the task item to the list container
    taskList.appendChild(taskItem);

    // Clear the input field for the next task
    taskInput.value = "";
    taskInput.focus();  // Put cursor back in the input
}

// Add task when clicking the button
addTaskBtn.addEventListener("click", addTask);

// Also add task when pressing Enter in the input field
taskInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") addTask();  // event.key tells us which key was pressed
});
```

Save and refresh. Type a task, click "Add" (or press Enter). The task appears below with a Delete button. Click Delete — the task disappears.

This demonstrates the full DOM manipulation cycle: **create** new elements, **fill** them with content, **attach** event listeners, **add** them to the page, and **remove** them when needed.

---

## Putting It All Together

In one file, you’ve used:

- `classList.toggle()` to switch between visual states
- The `input` event for real-time keystroke tracking
- `createElement()` and `appendChild()` to build new elements dynamically
- `.remove()` to delete elements from the page
- Event listeners for `click`, `input`, and `keydown`

These are the building blocks of every interactive web application. The patterns you see here — listening for events, updating the DOM, managing state — are exactly what Streamlit automates for you in Python. Understanding them helps you appreciate what Streamlit does under the hood.