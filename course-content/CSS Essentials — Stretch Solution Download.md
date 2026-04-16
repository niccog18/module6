# CSS Essentials — Stretch Solution Download

**Reference solution:** `module-06/solutions/responsive-portfolio/`

The reference solution adds a media query to the portfolio stylesheet:

```css
@media (max-width: 600px) {
    .project-grid {
        flex-direction: column;
    }
}
```

This single rule stacks the project cards vertically on screens narrower than 600px. Test by opening Chrome DevTools (Cmd/Ctrl + Shift + I) and using the device toggle to resize the viewport.

**Key concept:** Media queries are the foundation of responsive design — applying different CSS rules at different screen sizes. Streamlit handles this automatically, but understanding the principle helps you debug layout issues in any web tool.

**Note:** Your breakpoint and layout changes may differ. The key is demonstrating that the layout adapts to screen size.