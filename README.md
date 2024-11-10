# Data Scientist Interview Preparation App with LLaMA

## Overview
This is an application that helps users prepare for data science interviews by generating questions using the LLaMA model. The application consists of a FastAPI backend for generating questions and a Streamlit frontend for user interaction.

### Project Structure
data_scientist_prep/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── llama_model/
│       ├── llama_tokenizer/
│       └── llama_weights/
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── .env (Optional for API keys)
└── README.md


## Backend Setup
1. Navigate to the `backend/` directory.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
# Run the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Run the Streamlit app:
streamlit run app.py



### **Summary**
- **Backend** (`FastAPI`) to dynamically generate questions using LLaMA.
- **Frontend** (`Streamlit`) to interact with the user.
- **LLaMA Model Setup** to serve questions dynamically.
- **Requirements** files for both the backend and frontend to manage dependencies.

This setup allows users to dynamically generate questions on different data science topics, interactively answer, and keep practicing. Let me know if you have questions about deploying or modifying this further! 😊

