import streamlit as st
from src import tutor, diagrams, quiz

st.set_page_config(page_title="AI Coding Tutor", page_icon="🤖")

st.title("🤖 AI Coding Tutor")
st.write("Learn coding step by step with explanations, diagrams, and quizzes!")

concept = st.text_input("Enter a coding concept (e.g., Binary Search, Recursion)")

if st.button("Teach Me!"):
    if concept:
        explanation = tutor.explain_concept(concept)
        st.subheader("📘 Explanation")
        st.write(explanation)

        diagram = diagrams.generate_diagram(concept)
        if diagram:
            st.subheader("🖼️ Diagram")
            st.image(diagram)

        q, options, ans = quiz.generate_quiz(concept)
        st.subheader("❓ Quiz")
        st.write(q)
        for i, opt in enumerate(options):
            if st.button(opt):
                if i == ans:
                    st.success("Correct! 🎉")
                else:
                    st.error("Oops! Try again.")
