"""
L9 — Stateful Quiz App  (STARTER)
===================================
Run with:
    streamlit run solution.py

Your goal: build a 5-question multiple-choice quiz app that tracks state
across re-runs using st.session_state.

Required features:
    1. 5 hardcoded multiple-choice questions on course topics
    2. Session state tracking: current_question, score, answered
    3. Show the question and radio-button options
    4. Submit button → reveal right/wrong feedback
    5. Next button → advance to the next question
    6. Progress bar and "Question X of 5" indicator
    7. Results screen with final score and Restart button

Session state lifecycle:
    1. INITIALIZE — set defaults once with the pattern:
         if "key" not in st.session_state:
             st.session_state.key = default_value
    2. READ   — use st.session_state.key anywhere
    3. UPDATE — assign st.session_state.key = new_value
    4. RESET  — reassign all keys to defaults (Restart button)
"""

import streamlit as st

# ── Step 1: Quiz data ──────────────────────────────────────────────────────
# TODO: Create a list called QUESTIONS with 5 dicts.
# Each dict should have:
#   "question"    : str  — the question text
#   "options"     : list — 4 answer choices
#   "answer"      : str  — must match exactly one of the options
#   "explanation" : str  — shown after the user answers
QUESTIONS = [
    # TODO: Add 5 question dicts here
]

# ── Step 2: Session state initialisation ──────────────────────────────────
# Use this pattern for EVERY piece of state:
#   if "key" not in st.session_state:
#       st.session_state.key = default_value
#
# This runs ONLY on the first load. On every re-run (after a widget
# interaction), session_state already has the key so the block is skipped.

# TODO: Initialise `current_q` to 0
# TODO: Initialise `score` to 0
# TODO: Initialise `answered` to False
# TODO: Initialise `selected` to None
# TODO: Initialise `show_results` to False

# ── Step 3: Page config ───────────────────────────────────────────────────
# TODO: st.set_page_config and st.title

# ══════════════════════════════════════════════════════════════════════════
# RESULTS SCREEN
# Render when st.session_state.show_results is True
# ══════════════════════════════════════════════════════════════════════════
# TODO: if st.session_state.show_results:
#   - Calculate percentage score
#   - Show st.success / st.warning based on score
#   - Show st.progress(pct / 100)
#   - Show a Restart button that resets all session state keys
#   - Call st.stop() so the quiz below doesn't render
#   - Call st.rerun() after resetting state to refresh the page

# ══════════════════════════════════════════════════════════════════════════
# QUIZ SCREEN
# ══════════════════════════════════════════════════════════════════════════
# TODO: Get the current question from QUESTIONS[st.session_state.current_q]

# TODO: Show progress indicator: "Question X of 5"
# TODO: Show st.progress(q_index / total_qs)

# TODO: Show st.subheader with the question text

# TODO: Show st.radio with the answer options
#   - Use disabled=True after the user has submitted (st.session_state.answered)
#   - Give it a unique key per question: key=f"q_{q_index}"
#   - Store the selection in st.session_state.selected

# TODO: If not yet answered: show a Submit button
#   - On click: set st.session_state.answered = True
#   - If correct: increment st.session_state.score
#   - Call st.rerun() to trigger a re-render showing feedback

# TODO: If answered: show feedback
#   - st.success if correct, st.error if wrong (show the correct answer)
#   - st.info with the explanation
#   - Show a Next / Finish button
#     - If last question: set show_results = True, call st.rerun()
#     - Otherwise: increment current_q, reset answered/selected, call st.rerun()
