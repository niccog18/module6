# JavaScript Basics — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What is the DOM?

- A) A programming language that browsers use instead of JavaScript
- B) A tree-structured representation of the HTML document that JavaScript can interact with
- C) A database where browsers store website data
- D) A CSS layout system for positioning elements

> **Answer: B** — The DOM (Document Object Model) is the browser’s internal tree representation of the HTML page. Every HTML element becomes an object in this tree, and JavaScript can read, modify, create, or delete these objects. The DOM is not a language itself (A) — it’s a structure that JavaScript manipulates. It’s not a database (C) or a layout system (D).
> 

---

**Question 2:** What is the difference between `let` and `const` in JavaScript?

- A) `let` is for strings; `const` is for numbers
- B) `let` declares a variable whose value can be reassigned; `const` declares a value that cannot be reassigned
- C) `const` is faster than `let`
- D) There is no difference — they are interchangeable

> **Answer: B** — `const` creates a binding that cannot be reassigned to a new value. `let` creates a binding that can change. Use `const` by default, and `let` only when you know the value will need to change. This is JavaScript’s way of being explicit about intent — similar to how Python developers use ALL_CAPS naming for constants, except JavaScript enforces it.
> 

---

**Question 3:** What does `document.querySelectorAll(".card")` return?

- A) The first element with class "card"
- B) A list (NodeList) of ALL elements with class "card"
- C) A boolean indicating whether any .card elements exist
- D) The CSS styles applied to .card elements

> **Answer: B** — `querySelectorAll` returns a NodeList (similar to an array) containing *all* elements that match the CSS selector. If you want only the *first* match, use `querySelector` (no "All"). The selector `.card` uses a dot prefix because it’s targeting a class — the same CSS selector syntax you learned in the CSS lesson.
> 

---

**Question 4:** When does the `"input"` event fire on a text field?

- A) Only when the user presses Enter
- B) Only when the user clicks away from the field
- C) On every keystroke or change to the field’s value
- D) Only when the field is first clicked

> **Answer: C** — The `input` event fires immediately whenever the field’s value changes — on every keystroke, paste, or deletion. This makes it ideal for live features like character counters and search-as-you-type. If you picked B, that’s the `change` event, which waits until the user leaves the field. If you picked A, that’s a `keydown` event filtered for the Enter key.
>