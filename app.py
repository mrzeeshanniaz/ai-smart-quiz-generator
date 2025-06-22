import streamlit as st
from config import configure_page
from ui.layout import get_quiz_settings
from generators.quiz_generator import generate_quiz
from ui.display import display_quiz

def main():
    configure_page()
    topic, difficulty, num_questions, model_choice, variety_level = get_quiz_settings()

    if st.button("Generate Smart Quiz", type="primary"):
        st.session_state.last_topic = topic
        st.divider()

        if model_choice in ["OpenAI", "Both"]:
            with st.spinner("Generating optimized questions..."):
                openai_quiz = generate_quiz("OpenAI", topic, difficulty, num_questions, variety_level)
                display_quiz(openai_quiz, "OpenAI")

        if model_choice in ["Groq", "Both"]:
            with st.spinner("Generating optimized questions..."):
                groq_quiz = generate_quiz("Groq", topic, difficulty, num_questions, variety_level)
                display_quiz(groq_quiz, "Groq")

if __name__ == "__main__":
    main()
