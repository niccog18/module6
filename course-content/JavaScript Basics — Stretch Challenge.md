# JavaScript Basics — Stretch Challenge

## Keyboard Navigation

Your flashcard app currently requires clicking buttons. Many users prefer keyboard shortcuts for faster navigation.

**Challenge:** Add keyboard support to your flashcard app:

- **Right arrow key** (→) — Go to the next card (same as clicking Next)
- **Left arrow key** (←) — Go to the previous card
- **Space bar** — Toggle the answer visibility (same as clicking Show Answer)

**Hint:** Add a `keydown` event listener to `document` (not a specific element) since keyboard events can happen anywhere on the page:

```jsx
document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
        // Go to next card
    } else if (event.key === "ArrowLeft") {
        // Go to previous card
    } else if (event.key === " ") {
        event.preventDefault();  // Prevent the spacebar from scrolling the page
        // Toggle answer
    }
});
```

For the "previous card" logic, you can use: `currentIndex = (currentIndex - 1 + cards.length) % cards.length` — the `+ cards.length` prevents negative numbers before the modulo operation.