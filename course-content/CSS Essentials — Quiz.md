# CSS Essentials — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What is the difference between `padding` and `margin`?

- A) Padding is space outside the border; margin is space inside the border
- B) Padding is space inside the border (between content and border); margin is space outside the border (between the element and its neighbors)
- C) Padding only works on text; margin only works on images
- D) They are the same thing with different names

> **Answer: B** — Padding is the space between the content and the element's border — like the cushion inside a picture frame. Margin is the space outside the border — like the gap between frames on a wall. If you picked A, you have them backwards, which is a common mix-up. Remember: **p**adding is **p**ersonal space (inside), **m**argin is the **m**oat around the castle (outside).
> 

---

**Question 2:** What does `text-align: center;` do when applied to a `<div>` element?

- A) It centers the `<div>` itself on the page
- B) It centers the text (and inline content) inside the `<div>`
- C) It centers the `<div>` vertically
- D) It has no effect on `<div>` elements

> **Answer: B** — `text-align: center` centers the *inline content* (text, images, inline elements) inside the element. It does NOT center the element itself — that's done with `margin: 0 auto` combined with a set `max-width`. This is one of the most common CSS misunderstandings for beginners.
> 

---

**Question 3:** Given this CSS, which `<p>` elements will be styled?

```css
nav p {
    color: red;
}
```

- A) All `<p>` elements on the page
- B) Only `<p>` elements that are directly inside a `<nav>` element
- C) Only the first `<p>` element on the page
- D) Only `<p>` elements with the class "nav"

> **Answer: B** — This is a *descendant selector*. `nav p` means "select any `<p>` that is inside a `<nav>`, at any nesting level." It won't affect `<p>` elements in other parts of the page. If you picked D, that would be written as `.nav p` (with a dot, indicating a class selector).
> 

---

**Question 4:** What does `display: flex` do?

- A) It makes the element invisible
- B) It turns the element into a Flexbox container, allowing its children to be arranged in a row or column
- C) It makes the element flexible in size
- D) It applies only to images

> **Answer: B** — `display: flex` activates Flexbox on the container element. By default, its direct children will arrange themselves in a horizontal row. You can control spacing with `gap`, wrapping with `flex-wrap`, and direction with `flex-direction`. It's the most practical way to put elements side by side in modern CSS.
>