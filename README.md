# Data Scientist Interview Preparation Bot

An interactive interview‐prep application that dynamically generates multiple-choice questions on data-science and software-engineering topics using a local LLaMA model.  
The **backend** is a FastAPI service powered by **LangChain + CTransformers**, and the **frontend** is a Streamlit app for a straightforward, session-state-powered UX.

---

## 🔍 Features

- **Dynamic Question Generation**  
  Generates technical interview questions on demand (e.g. “Machine Learning”, “Data Structures”, “Python”, “Generative AI”, “Computer Vision”, “Deep Learning”), complete with four multiple-choice options and a marked correct answer.
- **FastAPI Backend**  
  Exposes a `POST /get_question/` endpoint that accepts `{"category": "<topic>"}` and returns JSON:
  ```json
  {
    "question": "…",
    "options": ["A) …", "B) …", "C) …", "D) …"],
    "correct_answer": "b"
  }
