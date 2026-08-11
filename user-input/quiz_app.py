import streamlit as st


# --------------------------------------------------
# Quiz questions
# --------------------------------------------------

questions = [
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Tech Modern Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": 0
    },
    {
        "question": "Which CSS property is used to change the text color?",
        "options": [
            "font-style",
            "text-color",
            "color",
            "background-color"
        ],
        "answer": 2
    },
    {
        "question": "Which JavaScript keyword is used to declare a variable that can be reassigned?",
        "options": [
            "const",
            "let",
            "fixed",
            "varies"
        ],
        "answer": 1
    },
    {
        "question": "Which Python function is used to display output?",
        "options": [
            "display()",
            "show()",
            "output()",
            "print()"
        ],
        "answer": 3
    },
    {
        "question": "Which HTTP method is commonly used to retrieve data from an API?",
        "options": [
            "POST",
            "DELETE",
            "GET",
            "PATCH"
        ],
        "answer": 2
    }
]


# --------------------------------------------------
# Initialize session state
# --------------------------------------------------

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False


# --------------------------------------------------
# Restart function
# --------------------------------------------------

def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False


# --------------------------------------------------
# Page title
# --------------------------------------------------

st.title("🧠 Web Development Quiz")

st.write(
    "Test your knowledge of HTML, CSS, JavaScript, Python, and APIs!"
)


# --------------------------------------------------
# Results screen
# --------------------------------------------------

if st.session_state.current_question >= len(questions):

    st.header("🎉 Quiz Complete!")

    st.metric(
        "Final Score",
        f"{st.session_state.score} / {len(questions)}"
    )

    percentage = (
        st.session_state.score / len(questions)
    ) * 100

    st.write(f"You scored **{percentage:.0f}%**.")

    if percentage == 100:
        st.success("Perfect score! Great job!")
    elif percentage >= 60:
        st.success("Nice work! You passed the quiz.")
    else:
        st.warning("Keep practicing and try again!")

    st.button(
        "🔄 Restart Quiz",
        on_click=restart_quiz
    )


# --------------------------------------------------
# Quiz screen
# --------------------------------------------------

else:

    question_number = st.session_state.current_question + 1
    total_questions = len(questions)

    question = questions[
        st.session_state.current_question
    ]

    # Progress indicator
    st.write(
        f"### Question {question_number} of {total_questions}"
    )

    progress = (
        question_number / total_questions
    )

    st.progress(progress)

    # Question
    st.subheader(question["question"])

    # Answer selection
    selected_answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"question_{st.session_state.current_question}"
    )

    # --------------------------------------------------
    # Submit answer
    # --------------------------------------------------

    if not st.session_state.answered:

        if st.button("Submit Answer"):

            selected_index = question["options"].index(
                selected_answer
            )

            if selected_index == question["answer"]:

                st.session_state.score += 1

                st.session_state.answered = True

                st.success("✅ Correct!")

            else:

                st.session_state.answered = True

                correct_answer = question["options"][
                    question["answer"]
                ]

                st.error("❌ Incorrect!")

                st.write(
                    f"The correct answer is: **{correct_answer}**"
                )

            st.rerun()


    # --------------------------------------------------
    # Next question
    # --------------------------------------------------

    if st.session_state.answered:

        # Show correct answer when the user got it right
        if selected_answer == question["options"][question["answer"]]:

            st.success(
                f"Correct! The answer is **{question['options'][question['answer']]}**"
            )

        # Show correct answer when the user got it wrong
        else:

            st.error("Incorrect!")

            st.write(
                f"The correct answer is: "
                f"**{question['options'][question['answer']]}**"
            )

        if st.button("Next Question ➡️"):

            st.session_state.current_question += 1
            st.session_state.answered = False

            st.rerun()

