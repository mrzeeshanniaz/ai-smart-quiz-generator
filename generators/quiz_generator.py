from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
import random
from constants import VARIETY_PROFILES, BANNED_QUESTIONS, TOPIC_EXPANDERS
from utils.helpers import generate_session_seed

def generate_quiz(model: str, topic: str, difficulty: str, num_questions: int, variety: str):
    profile = VARIETY_PROFILES[variety]
    banned = "\n".join([f"- {q}" for q in BANNED_QUESTIONS.get(topic, [])])
    expander = random.choice(TOPIC_EXPANDERS.get(topic, [""]))
    session_seed = generate_session_seed(topic)

    prompt_text = f"""Generate {num_questions} unique {difficulty}-level trivia questions about {topic}.
    
    Strict Requirements:
    1. Absolutely avoid these overused questions:
    {banned}
    2. {expander}
    3. Vary question types (what, why, how, which, when)
    4. Include specific examples or numbers where possible
    5. Current session context: {session_seed}
    6. Question diversity level: {profile['diversity']}/3
    7. NO introductory explanations - jump straight to questions
    8. ALL answers must be contained within expanders

    Format each question exactly like this:
    Q: [your creative question]
    A: [concise answer]
    ---"""

    if model == "OpenAI":
        llm = ChatOpenAI(
            temperature=profile['temp'],
            model="gpt-4",
            model_kwargs={"seed": int(session_seed[:8], 16) % 100000}
        )
    else:
        llm = ChatGroq(
            temperature=profile['temp'],
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )

    chain = ChatPromptTemplate.from_template(prompt_text) | llm | StrOutputParser()
    return chain.invoke({})
