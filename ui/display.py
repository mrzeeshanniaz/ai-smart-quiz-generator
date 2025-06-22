import streamlit as st

def display_quiz(quiz_text: str, model_name: str):
    st.subheader(f"{model_name} Quiz")
    st.caption("Try answering before revealing the solution!")

    entries = [block.strip() for block in quiz_text.split("---") if block.strip()]

    for index, entry in enumerate(entries, start=1):
        if "Q:" in entry and "A:" in entry:
            question_part, answer_part = entry.split("A:", 1)
            question = question_part.replace("Q:", "").strip()
            answer = answer_part.strip()

            with st.expander(f"Question {index}: {question}", expanded=False):
                st.markdown(f"Answer:{answer}")
    st.markdown("---")
