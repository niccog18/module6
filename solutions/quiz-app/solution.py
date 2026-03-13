"""
L9 — Stateful Quiz App  (Solution)
=====================================
Run with:
    streamlit run solution.py

Session state lifecycle:
    1. INITIALIZE — set default values once (guard: `if "key" not in st.session_state`)
    2. READ        — access st.session_state.key anywhere in the script
    3. UPDATE      — assign st.session_state.key = new_value (triggers re-run)
    4. RESET       — reassign all keys back to defaults (Restart button)

Why session state?
    Without it, every re-run starts from scratch. We need to remember:
      - Which question the user is on
      - Their score
      - Whether they already submitted an answer for the current question
"""

import streamlit as st

# ── Quiz data ─────────────────────────────────────────────────────────────────
QUESTIONS = [
    {
        "question": "What does HTTP stand for?",
        "options": [
            "HyperText Transfer Protocol",
            "High-Tech Transfer Process",
            "Hyper Transfer Text Protocol",
            "Hosted Text Transfer Platform",
        ],
        "answer": "HyperText Transfer Protocol",
        "explanation": "HTTP is the foundation of data communication on the World Wide Web.",
    },
    {
        "question": "Which HTTP status code means 'Not Found'?",
        "options": ["200", "301", "404", "500"],
        "answer": "404",
        "explanation": "404 is returned when the server cannot find the requested resource.",
    },
    {
        "question": "In CSS, which property is used to add space INSIDE an element's border?",
        "options": ["margin", "padding", "border-spacing", "gap"],
        "answer": "padding",
        "explanation": "padding is inside the border; margin is outside. Remember: Content → Padding → Border → Margin.",
    },
    {
        "question": "What does `async` before a Python function declaration do?",
        "options": [
            "Makes the function run faster",
            "Allows the function to use `await` and returns a coroutine",
            "Runs the function in a separate thread",
            "Prevents the function from returning a value",
        ],
        "answer": "Allows the function to use `await` and returns a coroutine",
        "explanation": "async functions return coroutine objects. They can pause execution with `await` to let other tasks run.",
    },
    {
        "question": "Which Streamlit function renders a chat-style message bubble?",
        "options": ["st.write()", "st.message()", "st.chat_message()", "st.bubble()"],
        "answer": "st.chat_message()",
        "explanation": "st.chat_message('user') or st.chat_message('assistant') creates a chat bubble with the appropriate styling.",
    },
]

# ── Session state initialisation ──────────────────────────────────────────────
# Pattern: `if "key" not in st.session_state:` ensures we set defaults ONLY
# on the very first run — never again. On subsequent re-runs this block is skipped.
if "current_q" not in st.session_state:
    st.session_state.current_q = 0        # index of current question (0-4)

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False     # has the user submitted the current question?

if "selected" not in st.session_state:
    st.session_state.selected = None      # which option was chosen

if "show_results" not in st.session_state:
    st.session_state.show_results = False # are we on the results screen?

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Web Dev Quiz", page_icon="🧠", layout="centered")
st.title("🧠 Web Dev Quiz")

# ══════════════════════════════════════════════════════════════════════════════
# RESULTS SCREEN
# Show after the final question has been answered and Next is clicked.
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.show_results:
    total = len(QUESTIONS)
    score = st.session_state.score
    pct   = score / total * 100

    if pct == 100:
        st.balloons()
        st.success(f"🎉 Perfect Score! {score}/{total} ({pct:.0f}%)")
    elif pct >= 60:
        st.success(f"✅ Good job! {score}/{total} ({pct:.0f}%)")
    else:
        st.warning(f"📚 Keep practising! {score}/{total} ({pct:.0f}%)")

    # Progress bar: value must be 0.0–1.0
    st.progress(pct / 100)

    if st.button("🔄 Restart Quiz"):
        # RESET all session state keys back to defaults
        st.session_state.current_q    = 0
        st.session_state.score        = 0
        st.session_state.answered     = False
        st.session_state.selected     = None
        st.session_state.show_results = False
        # st.rerun() immediately re-executes the script so the quiz page appears
        st.rerun()

    st.stop()  # Don't render the quiz below while on the results screen

# ══════════════════════════════════════════════════════════════════════════════
# QUIZ SCREEN
# ══════════════════════════════════════════════════════════════════════════════
q_index   = st.session_state.current_q
q_data    = QUESTIONS[q_index]
total_qs  = len(QUESTIONS)

# ── Progress indicator ─────────────────────────────────────────────────────────
st.caption(f"Question {q_index + 1} of {total_qs}")
# st.progress expects a float in [0.0, 1.0]
st.progress((q_index) / total_qs)

# ── Question ───────────────────────────────────────────────────────────────────
st.subheader(q_data["question"])

# ── Answer options ─────────────────────────────────────────────────────────────
# If already answered, disable the radio so the user can't change it.
selected = st.radio(
    "Choose an answer:",
    options=q_data["options"],
    index=None if not st.session_state.answered else q_data["options"].index(st.session_state.selected),
    disabled=st.session_state.answered,
    key=f"q_{q_index}",   # unique key per question prevents stale state
)

# Store the selection while user is choosing (before Submit)
if selected is not None and not st.session_state.answered:
    st.session_state.selected = selected

# ── Submit button ──────────────────────────────────────────────────────────────
if not st.session_state.answered:
    if st.button("Submit Answer", disabled=(st.session_state.selected is None)):
        # Mark as answered — this re-run will show feedback
        st.session_state.answered = True
        if st.session_state.selected == q_data["answer"]:
            st.session_state.score += 1
        st.rerun()

# ── Feedback (shown after Submit) ─────────────────────────────────────────────
if st.session_state.answered:
    if st.session_state.selected == q_data["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Wrong — the correct answer is: **{q_data['answer']}**")

    st.info(f"💡 {q_data['explanation']}")

    # ── Next button ────────────────────────────────────────────────────────────
    next_label = "Finish Quiz →" if q_index == total_qs - 1 else "Next Question →"
    if st.button(next_label):
        if q_index == total_qs - 1:
            # Last question — go to results screen
            st.session_state.show_results = True
        else:
            # Advance to next question and reset per-question state
            st.session_state.current_q += 1
            st.session_state.answered  = False
            st.session_state.selected  = None
        st.rerun()

# ── Score tracker ──────────────────────────────────────────────────────────────
st.divider()
st.caption(f"Score so far: {st.session_state.score} / {q_index + (1 if st.session_state.answered else 0)}")
