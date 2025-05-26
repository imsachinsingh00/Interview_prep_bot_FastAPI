# 🧠 Interview Preparation Bot (FastAPI Edition)

This is a backend API for an interview preparation chatbot built using **FastAPI** and integrated with **Hugging Face Inference API**. It generates MCQs based on selected topics to help users prepare for technical interviews.

## 🚀 Features

- RESTful API using FastAPI
- Topic-based MCQ generation using a Hugging Face model
- JSON-based structured responses (question, options, correct index)
- Extensible API design for frontend integration

## 📁 Project Structure

```
.
├── backend/
│   ├── main.py               # FastAPI app
│   ├── routes/               # Endpoint routes
│   ├── services/             # Hugging Face client & logic
│   └── models/               # Pydantic schemas
├── .github/                  # GitHub Actions (optional CI/CD)
├── requirements.txt          # Python dependencies
└── README.md
```

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone <repo-url>
cd Interview_prep_bot_FastAPI-master
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variable**

Create a `.env` file in the root directory:
```
HUGGINGFACEHUB_API_TOKEN=your_hf_api_key
```

5. **Run the API**
```bash
uvicorn backend.main:app --reload
```

6. **Access the docs**
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

## 🧠 Model Used

- `mistralai/Mixtral-8x7B-Instruct-v0.1` via Hugging Face Inference API

## 📄 License

MIT License.
