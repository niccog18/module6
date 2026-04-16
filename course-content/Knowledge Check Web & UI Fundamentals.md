# Knowledge Check: Web & UI Fundamentals

**Module 6 — Web Essentials & Streamlit**

**Mid-Module Assessment — Covers all of Week 1 plus a preview of Week 2 concepts**

---

**Question 1:** When you type `https://www.example.com` into your browser, what is the first step in loading the page?

- A) The browser downloads the HTML file
- B) The browser asks a DNS server to resolve the domain name to an IP address
- C) The browser applies CSS to the page
- D) The browser executes JavaScript

> **Answer: B** — DNS resolution happens first. The browser needs to know *where* the server is (its IP address) before it can send any HTTP requests. Only after DNS resolution does the browser connect to the server and request the HTML document.
> 

---

**Question 2:** Which of the following is a semantic HTML element?

- A) `<div>`
- B) `<span>`
- C) `<article>`
- D) `<b>`

> **Answer: C** — `<article>` is a semantic element — it describes that the enclosed content is a self-contained piece (like a blog post or product card). `<div>` and `<span>` are generic containers with no inherent meaning. `<b>` is a presentational element (bold text) without semantic significance — `<strong>` is the semantic alternative.
> 

---

**Question 3:** In the CSS box model, what is the correct order of layers from innermost to outermost?

- A) Margin → Border → Padding → Content
- B) Content → Border → Padding → Margin
- C) Content → Padding → Border → Margin
- D) Padding → Content → Margin → Border

> **Answer: C** — From inside out: Content is the actual text/image, Padding is space between content and border, Border is the visible line, and Margin is the space outside the border separating this element from neighbors. A helpful mnemonic: the content wears Padding like a coat, the Border is the fence, and the Margin is the yard.
> 

---

**Question 4:** What does `display: flex` do to an element’s children?

- A) Hides all children by default
- B) Stacks children vertically and removes their spacing
- C) Arranges children in a flexible row (by default) and allows control over spacing, alignment, and wrapping
- D) Makes each child the full width of the page

> **Answer: C** — Flexbox arranges direct children in a row (the default `flex-direction` is `row`). You can then control spacing with `gap`, wrapping with `flex-wrap`, and alignment with `justify-content` and `align-items`. It’s the modern way to create layouts like card grids, navigation bars, and dashboard metric rows.
> 

---

**Question 5:** What is the DOM?

- A) A CSS layout system for responsive design
- B) A programming language that runs in browsers
- C) A tree-structured representation of the HTML page that JavaScript can read and modify
- D) A database where browsers store website preferences

> **Answer: C** — The DOM (Document Object Model) is the browser’s in-memory representation of the HTML document. Every element becomes an object in a tree structure. JavaScript uses DOM methods like `querySelector()` and `addEventListener()` to find elements, change content, and respond to user actions.
> 

---

**Question 6:** You use `fetch()` to request a URL that returns a 404 status. What happens?

- A) `fetch()` throws an error that your catch block handles automatically
- B) `fetch()` resolves successfully — you must check `response.ok` to detect the 404
- C) The browser shows a built-in error page
- D) `fetch()` retries the request automatically

> **Answer: B** — This is the critical `response.ok` gotcha. `fetch()` only rejects (throws) for network-level failures like DNS errors or unreachable servers. A 404 is still a valid HTTP response, so `fetch()` treats it as successful. You MUST check `response.ok` to distinguish between 2xx success codes and 4xx/5xx error codes.
> 

---

**Question 7 (Streamlit preview):** Streamlit’s execution model is different from traditional web apps. What happens when a user interacts with a Streamlit widget (like clicking a button or moving a slider)?

- A) Only the affected widget re-renders
- B) The entire Python script re-runs from top to bottom
- C) JavaScript event listeners fire and update the DOM
- D) The page refreshes and reloads from the server

> **Answer: B** — This is the single most important concept in Streamlit. Every user interaction triggers a complete re-run of the entire script. This means all variables reset to their initial values on each run, which is why you’ll need `st.session_state` to persist data across interactions. Understanding this model is essential for building Streamlit apps.
> 

---

**Question 8 (Streamlit preview):** In Streamlit, why do you need `st.session_state` to track values across user interactions?

- A) Streamlit doesn’t support regular Python variables
- B) Because the script re-runs from top to bottom on every interaction, all local variables reset to their initial values
- C) `st.session_state` is faster than regular variables
- D) You don’t — regular Python variables work fine

> **Answer: B** — Since Streamlit re-runs the entire script on every interaction, a line like `count = 0` will always reset `count` back to 0. `st.session_state` is a dictionary that persists across re-runs, allowing you to store and update values like counters, login tokens, and form data. The standard initialization pattern is: `if "key" not in st.session_state: st.session_state["key"] = initial_value`.
> 

---

**Question 9 (Streamlit preview):** What is the benefit of wrapping Streamlit inputs in `st.form()`?

- A) It makes the inputs look better
- B) It batches multiple inputs so the script only re-runs once when the form is submitted, instead of re-running on every individual widget interaction
- C) Forms are required for all Streamlit input widgets
- D) It automatically validates the input data

> **Answer: B** — Without a form, every widget change triggers a re-run. If you have 5 inputs, filling them out triggers 5 re-runs. Wrapping them in `st.form()` with a submit button means the script waits for the user to fill everything out and click submit — only then does it re-run once. This is critical for forms that trigger expensive operations like API calls.
> 

---

**Question 10 (Streamlit preview):** In a Streamlit chat interface, why must you re-render the entire chat history on every script run?

- A) Streamlit has a bug that clears the screen
- B) Because Streamlit re-runs the entire script, the screen is rebuilt from scratch each time — so you must loop through the stored history and display each message
- C) Chat messages are automatically deleted after 30 seconds
- D) You don’t — Streamlit remembers what was displayed previously

> **Answer: B** — Streamlit’s re-run model means the display resets each time. Chat messages stored in `st.session_state` persist, but they must be explicitly re-displayed by looping through the history list and calling `st.chat_message()` for each entry. This pattern — store in state, re-render on every run — is fundamental to all Streamlit applications.
>