# JavaScript Basics — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 35 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what JavaScript does that HTML and CSS cannot
2. Declare variables with `let` and `const`, and write functions including arrow functions
3. Describe what the DOM is and how JavaScript uses it to change webpage content
4. Add event listeners to respond to user actions like clicks and keyboard input

---

`[VIDEO PLACEHOLDER: 7 min — "JavaScript Basics: What JS does that HTML/CSS can’t. Live demo of DOM manipulation — clicking a button to change content, typing to filter a list. Show the JS vs Python syntax comparison."]`

You’ve built the frame (HTML) and painted the walls (CSS). Now it’s time to install the light switches, the doorbell, and the thermostat — the things that *respond* when someone interacts with them.

That’s JavaScript. It’s the programming language that makes webpages **interactive**. When you click a button and something happens. When you type in a search box and results filter in real time. When a menu opens, a form validates your input, or new content loads without refreshing the page — that’s all JavaScript.

HTML tells the browser *what’s on the page*. CSS tells it *how things look*. JavaScript tells it *what to do when things happen*.

---

## JavaScript vs. Python: You Already Know This

Here’s the good news: you already know how to program. JavaScript has different syntax than Python, but the concepts are the same — variables, functions, loops, conditionals. Let’s compare:

```python
# Python
name = "Alex"
age = 28
is_student = True

def greet(person):
    return f"Hello, {person}!"

if age >= 18:
    print(greet(name))
```

```jsx
// JavaScript
let name = "Alex";        // 'let' for variables that change
const age = 28;           // 'const' for values that don't change
let isStudent = true;     // camelCase, not snake_case

function greet(person) {
    return `Hello, ${person}!`;  // Backticks for template literals
}

if (age >= 18) {          // Parentheses required around condition
    console.log(greet(name));  // console.log, not print
}
```

The logic is identical. The differences are cosmetic: semicolons at the end of statements, curly braces instead of indentation for blocks, `let`/`const` instead of plain assignment, `console.log()` instead of `print()`, and camelCase naming convention instead of snake_case.

JavaScript also has **arrow functions** — a shorter way to write functions (similar to Python’s `lambda`, but much more widely used):

```jsx
// Traditional function
function greet(person) {
    return `Hello, ${person}!`;
}

// Arrow function — same thing, shorter syntax
const greet = (person) => `Hello, ${person}!`;
```

You’ll see arrow functions constantly in JavaScript code. They’re especially common for short, one-line operations.

---

## The DOM: JavaScript’s Window into the Page

Here’s where JavaScript gets its real power. When your browser loads an HTML page, it creates an internal representation called the **DOM** (Document Object Model). The DOM is a tree structure where every HTML element becomes an **object** that JavaScript can read, change, add to, or remove.

![image.png](JavaScript%20Basics%20%E2%80%94%20Concept/image.png)

Think of it this way: HTML is a blueprint on paper. The DOM is the actual built house. JavaScript is the person who can walk through the house and rearrange furniture, repaint walls, add rooms, or knock down walls — all while someone is living in it.

![image.png](JavaScript%20Basics%20%E2%80%94%20Concept/image%201.png)

JavaScript interacts with the DOM using methods like:

```jsx
// Find one element by its ID
const header = document.getElementById("main-header");

// Find one element using a CSS selector
const firstCard = document.querySelector(".card");

// Find ALL elements matching a CSS selector
const allCards = document.querySelectorAll(".card");
```

Once you have a reference to an element, you can change it:

```jsx
header.textContent = "New Title";        // Change the text
header.style.color = "red";              // Change the CSS
header.classList.add("highlighted");      // Add a CSS class
header.classList.toggle("dark-mode");     // Toggle a class on/off
```

---

## Event Listeners: Responding to User Actions

The most important JavaScript concept for interactivity is the **event listener**. It says: "When *this thing happens* to *this element*, run *this function*."

```jsx
const button = document.querySelector("#my-button");

button.addEventListener("click", () => {
    // This code runs when the button is clicked
    console.log("Button was clicked!");
});
```

Common events include:

- `"click"` — User clicks the element
- `"input"` — User types in a text field (fires on every keystroke)
- `"submit"` — A form is submitted
- `"keydown"` — A key is pressed on the keyboard
- `"mouseover"` — Mouse hovers over the element

This is the pattern that drives every interactive webpage: find an element, listen for an event, do something in response.

---

## Where JavaScript Lives in a Page

JavaScript goes in a `<script>` tag, usually placed just before the closing `</body>` tag:

```html
<body>
    <!-- Your HTML content -->
    <h1 id="title">Hello!</h1>
    <button id="change-btn">Click Me</button>

    <!-- JavaScript at the bottom, after all HTML has loaded -->
    <script>
        const btn = document.querySelector("#change-btn");
        btn.addEventListener("click", () => {
            document.querySelector("#title").textContent = "You clicked it!";
        });
    </script>
</body>
```

Placing it at the bottom ensures all the HTML elements exist before JavaScript tries to find them. If the script ran *before* the HTML loaded, `querySelector` would find nothing.

---

## A Note on Scope: This Is Web Literacy, Not Mastery

This lesson covers just enough JavaScript to understand how web interactivity works. You will **not** become a JavaScript developer from this module — and you don’t need to be. In Week 2, you’ll switch to Streamlit, which lets you build interactive UIs entirely in Python.

But knowing what JavaScript does, recognizing its syntax, and understanding the DOM will make you a more effective developer. You’ll read documentation more confidently, debug browser issues more effectively, and understand what’s happening under the hood when tools like Streamlit generate web interfaces.