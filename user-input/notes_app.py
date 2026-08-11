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
