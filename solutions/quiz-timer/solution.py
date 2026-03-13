"""
L9b — Quiz App with Countdown Timer  (Stretch Challenge)
=========================================================
Run with:
    streamlit run solution.py

Demonstrates:
    • st.empty()    — a single reusable placeholder in the layout
    • time.sleep()  — pause execution (blocks the app thread)
    • Auto-advance  — if the timer runs out without an answer

KEY CONCEPT — st.empty():
    st.empty() returns a placeholder object. You can overwrite its content
    on every loop iteration using `placeholder.write(...)` or other methods.
    Without st.empty(), each st.write() adds a NEW element — you'd end up
    with 15 separate countdown numbers printed in the page.

    Pattern:
        timer_placeholder = st.empty()
        for i in range(15, 0, -1):
            timer_placeholder.metric("Time Left", f"{i}s")
            time.sleep(1)
        timer_placeholder.empty()   # clear when done

CAVEAT — time.sleep() blocks the Streamlit server thread.
    This means no other Streamlit interactions can be processed while
    the sleep loop is running. The whole app is frozen for that user.
    In production, use a background thread, asyncio, or a client-side
    JS timer instead. For demos/learning, sleep is fine.
"""

import streamlit as st
import time

# ── Quiz data ────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "question": "What does HTTP stand for?",
        "options": ["HyperText Transfer Protocol", "High-Tech Transfer Process",
                    "Hyper Transfer Text Protocol", "Hosted Text Transfer Platform"],
        "answer": "HyperText Transfer Protocol",
    },
    {
        "question": "Which HTTP status code means 'Not Found'?",
        "options": ["200", "301", "404", "500"],
        "answer": "404",
    },
    {
        "question": "Which CSS property adds space INSIDE an element's border?",
        "options": ["margin", "padding", "gap", "border-spacing"],
        "answer": "padding",
    },
    {
        "question": "Which Streamlit function renders a reusable placeholder?",
        "options": ["st.container()", "st.empty()", "st.placeholder()", "st.slot()"],
        "answer": "st.empty()",
    },
    {
        "question": "What does `async def` allow inside a Python function?",
        "options": [
            "Faster execution",
            "Use of `await` to pause for I/O",
            "Automatic threading",
            "Type annotations",
        ],
        "answer": "Use of `await` to pause for I/O",
    },
]

TIMER_SECONDS = 15

# ── Session state ────────────────────────────────────────────────────────────
if "current_q"    not in st.session_state: st.session_state.current_q    = 0
if "score"        not in st.session_state: st.session_state.score        = 0
if "answered"     not in st.session_state: st.session_state.answered     = False
if "selected"     not in st.session_state: st.session_state.selected     = None
if "timed_out"    not in st.session_state: st.session_state.timed_out    = False
if "show_results" not in st.session_state: st.session_state.show_results = False

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Timed Quiz", page_icon="⏱️", layout="centered")
st.title("⏱️ Timed Quiz")
st.caption(f"You have {TIMER_SECONDS} seconds per question.")

# ── Results screen ────────────────────────────────────────────────────────────
if st.session_state.show_results:
    total = len(QUESTIONS)
    score = st.session_state.score
    pct   = score / total * 100
    st.progress(pct / 100)
    if pct >= 80:
        st.success(f"🎉 Great job! {score}/{total} ({pct:.0f}%)")
    else:
        st.warning(f"📚 Keep practising! {score}/{total} ({pct:.0f}%)")

    if st.button("🔄 Restart"):
        for key in ["current_q", "score", "answered", "selected", "timed_out", "show_results"]:
            del st.session_state[key]
        st.rerun()
    st.stop()

# ── Quiz screen ───────────────────────────────────────────────────────────────
q_idx  = st.session_state.current_q
q_data = QUESTIONS[q_idx]
total  = len(QUESTIONS)

st.caption(f"Question {q_idx + 1} of {total}")
st.progress(q_idx / total)
st.subheader(q_data["question"])

selected = st.radio(
    "Choose an answer:",
    options=q_data["options"],
    index=None if not st.session_state.answered else
          (q_data["options"].index(st.session_state.selected) if st.session_state.selected in q_data["options"] else None),
    disabled=st.session_state.answered or st.session_state.timed_out,
    key=f"q_{q_idx}",
)

if selected is not None and not st.session_state.answered:
    st.session_state.selected = selected

# ── Countdown timer (runs only before the user answers) ──────────────────────
if not st.session_state.answered and not st.session_state.timed_out:
    # st.empty() creates a single placeholder that we overwrite each second.
    # Without it, each st.metric() call would ADD a new element to the page,
    # resulting in 15 numbers stacked vertically.
    timer_placeholder = st.empty()
    submit_col, _ = st.columns([1, 3])
    submit_btn = submit_col.button("Submit Answer", disabled=(st.session_state.selected is None), key=f"submit_{q_idx}")

    if submit_btn:
        st.session_state.answered = True
        if st.session_state.selected == q_data["answer"]:
            st.session_state.score += 1
        st.rerun()

    # Countdown loop
    for remaining in range(TIMER_SECONDS, 0, -1):
        # Re-check if a re-run happened (user submitted while timer was running)
        # In a real app, this pattern is imperfect because sleep blocks re-runs.
        timer_placeholder.metric(
            label="⏳ Time Remaining",
            value=f"{remaining}s",
            delta=f"-{TIMER_SECONDS - remaining}s elapsed",
            delta_color="inverse",
        )
        # CAVEAT: time.sleep(1) blocks the Streamlit server thread for 1 second.
        # No other user interactions are processed during this sleep.
        time.sleep(1)

    # Timer reached zero without a submission
    timer_placeholder.metric("⏳ Time Remaining", "0s — Time's up!")
    st.session_state.timed_out = True
    st.rerun()

# ── Feedback ──────────────────────────────────────────────────────────────────
if st.session_state.answered or st.session_state.timed_out:
    if st.session_state.timed_out and not st.session_state.answered:
        st.error("⏰ Time's up! You didn't answer in time.")
    elif st.session_state.selected == q_data["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Wrong — the correct answer is: **{q_data['answer']}**")

    if st.button("Next →" if q_idx < total - 1 else "Finish Quiz"):
        if q_idx == total - 1:
            st.session_state.show_results = True
        else:
            st.session_state.current_q += 1
            st.session_state.answered   = False
            st.session_state.selected   = None
            st.session_state.timed_out  = False
        st.rerun()
