import streamlit as st
from constants import DEFAULT_TOPIC, MODEL_CHOICES, DIFFICULTY_LEVELS, VARIETY_PROFILES

def get_quiz_settings():
    with st.sidebar:
        st.header("Quiz Settings")
        topic = st.text_input("Quiz Topic", DEFAULT_TOPIC)
        difficulty = st.selectbox("Difficulty", DIFFICULTY_LEVELS, index=1)
        num_questions = st.slider("Number of Questions", 3, 20, 5)
        model_choice = st.radio("AI Model", MODEL_CHOICES)
        variety_level = st.selectbox("Question Variety", list(VARIETY_PROFILES.keys()))
    return topic, difficulty, num_questions, model_choice, variety_level
