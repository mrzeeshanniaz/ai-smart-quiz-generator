# 🤖 AI Smart Quiz Generator

An interactive Streamlit-based quiz application that uses OpenAI and Groq (via LangChain) to generate unique, high-quality trivia questions based on any topic, difficulty, and model preference.

---

## 🚀 Features

- ✅ Choose topic, difficulty, and number of questions
- 🤖 Generate questions using **OpenAI**, **Groq**, or both
- 🔄 Dynamic question variety with creativity levels
- 🧠 Expandable sections to reveal answers
- 💡 Avoids generic and overused questions
- 🛠️ Modular code structure for easy customization

---

## 📸 Demo

![screenshot](./assets/demo-screenshot.png) <!-- optional if you want to add a demo image -->

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4](https://openai.com/gpt-4)
- [Groq LLaMA](https://groq.com/)
- Python 3.8+

---

## 🔐 Environment Variables

Create a `.env` file in your project root with the following keys:

```env
OPENAI_API_KEY=your-openai-key
GROQ_API_KEY=your-groq-key
