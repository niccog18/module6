# CSS Essentials — Stretch Challenge

## Responsive Media Query

Web pages look different on phones versus laptops. A **media query** lets you apply CSS rules only when the screen meets certain conditions.

**Challenge:** Add a media query to your portfolio CSS that stacks the project cards into a single column on screens narrower than 600px.

Here's the syntax:

```css
/* This CSS only applies when the screen is 600px or narrower */
@media (max-width: 600px) {
    .project-grid {
        flex-direction: column;  /* Stack cards vertically instead of in a row */
    }
}
```

To test it, open your page in Chrome and use DevTools (Cmd/Ctrl + Shift + I) → click the device toggle icon (looks like a phone and tablet) → resize the viewport width below and above 600px. Watch the layout change.

This is a core concept in **responsive design** — making your layout adapt to different screen sizes. Streamlit handles this automatically, but understanding the principle helps you debug layout issues in any web tool.