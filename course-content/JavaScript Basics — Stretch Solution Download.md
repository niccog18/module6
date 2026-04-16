# JavaScript Basics — Stretch Solution Download

**Reference solution:** `module-06/solutions/flashcard-keyboard/`

The reference solution adds keyboard navigation to the flashcard app:

- **Right arrow (→):** Next card
- **Left arrow (←):** Previous card (using `(currentIndex - 1 + cards.length) % cards.length` to avoid negative indices)
- **Space bar:** Toggle answer visibility (with `event.preventDefault()` to stop page scrolling)

The event listener is on `document` (not a specific element) since keyboard events can happen anywhere on the page.

**Key concept:** Global keyboard listeners are a common pattern for navigation shortcuts. The `preventDefault()` call is important — without it, the space bar would scroll the page.

**Note:** Your implementation may use different keys or add additional shortcuts. The key is using `document.addEventListener("keydown", ...)` and handling multiple key cases.