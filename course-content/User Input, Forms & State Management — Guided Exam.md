# User Input, Forms & State Management — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 10 min — "Build notes_app.py: add notes with tags, notes persist across re-runs via session state, sidebar tag filter, individual delete buttons with unique keys, clear_on_submit, st.rerun()."]`

Let’s build a notes app that demonstrates all the state management patterns you’ll need. Create `notes_app.py`:

```python
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Notes App", page_icon="📝", layout="wide")

# --- Initialize Session State ---
if "notes" not in st.session_state:
    st.session_state["notes"] = [
        {"text": "Welcome to the Notes App!", "tag": "General",
         "time": datetime.now().strftime("%H:%M")}
    ]

# --- Sidebar: Tag Filter ---
with st.sidebar:
    st.title("🏷️ Filter by Tag")

    # Get unique tags from all notes
    all_tags = list(set(note["tag"] for note in st.session_state["notes"]))
    all_tags.sort()

    selected_tag = st.radio(
        "Show notes tagged:",
        ["All"] + all_tags
    )

    st.divider()
    st.metric("Total Notes", len(st.session_state["notes"]))

# --- Main Content ---
st.title("📝 Notes App")

# --- Add Note Form ---
with st.form("add_note", clear_on_submit=True):  # Clears fields after submit
    st.subheader("Add a New Note")

    note_text = st.text_area("Note", placeholder="Write your note here...")
    note_tag = st.selectbox("Tag", ["General", "Work", "Personal", "Ideas", "Todo"])

    submitted = st.form_submit_button("➕ Add Note")

    if submitted and note_text.strip():  # Only add if there's actual text
        st.session_state["notes"].append({
            "text": note_text.strip(),
            "tag": note_tag,
            "time": datetime.now().strftime("%H:%M")
        })
        st.rerun()  # Force re-run to show the new note immediately

st.divider()

# --- Display Notes ---
# Filter notes based on sidebar selection
if selected_tag == "All":
    filtered = st.session_state["notes"]
else:
    filtered = [n for n in st.session_state["notes"] if n["tag"] == selected_tag]

st.subheader(f"Notes ({len(filtered)} showing)")

if not filtered:
    st.info("No notes found for this tag. Try 'All' or add a new note!")

# Display each note with a delete button
for i, note in enumerate(filtered):
    col_text, col_delete = st.columns([5, 1])  # 5:1 ratio

    with col_text:
        st.write(f"**[{note['tag']}]** {note['text']}")
        st.caption(f"Added at {note['time']}")

    with col_delete:
        # CRITICAL: unique key for each delete button
        if st.button("🗑️", key=f"delete_{i}_{note['time']}"):
            st.session_state["notes"].remove(note)
            st.rerun()  # Re-run to update the display

    st.divider()
```

Run it:

```bash
streamlit run notes_app.py
```

---

## What You Should See

1. A form to add notes with a text area, tag selector, and submit button
2. The form clears after submission (`clear_on_submit=True`)
3. Notes appear below with their tag and timestamp
4. The sidebar lets you filter notes by tag
5. Each note has a delete button that removes it

---

## Key Patterns in This Example

**Initialization:** `if "notes" not in st.session_state` — the standard pattern.

**Form batching:** The text area and selectbox inside `st.form()` don’t trigger re-runs until you click "Add Note."

**Unique keys:** `key=f"delete_{i}_{note['time']}"` ensures each delete button is uniquely identified. Without unique keys, Streamlit would confuse which button was clicked.

**`st.rerun()`:** After adding or deleting a note, we force a re-run so the display updates immediately.

**Filtered display:** The sidebar filter uses a simple list comprehension on the session state data. The data lives in session state; the display is rebuilt from it on every run.