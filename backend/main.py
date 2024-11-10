from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import re

# Initialize FastAPI app
app = FastAPI()

# Define the data model for incoming requests
class TopicRequest(BaseModel):
    category: str

# Load the LLaMA model using CTransformers
model_path = r'C:\Users\singh\Documents\LLM\Interview_prep_bot\backend\Model\llama-2-7b-chat.ggmlv3.q8_0.bin'
try:
    llm = CTransformers(
        model=model_path,
        model_type='llama',
        config={
            'max_new_tokens': 150,
            'temperature': 0.3
        }
    )
except Exception as e:
    print(f"Error loading LLaMA model: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Data Scientist Interview Prep API with LLaMA!"}

@app.post("/get_question/")
def get_question(request: TopicRequest):
    category = request.category.lower()

    # Improved Prompt Template to Generate More Consistent Responses
    prompt_template = """
        You are an expert interviewer. Please generate a technical interview question on the topic of {category}.
        Provide four multiple-choice options labeled A), B), C), and D), with one correct answer marked with an asterisk (*) after the option label.
        Provide your response in the following format:
        Question: <The question>
        Options:
        A) <Option A>
        B) <Option B> *
        C) <Option C>
        D) <Option D>
    """
    prompt = PromptTemplate(input_variables=["category"], template=prompt_template)

    try:
        # Use LLaMA model to generate the question
        response = llm(prompt.format(category=category))
        print(f"\n[DEBUG] Generated Response from Model:\n{response}\n")  # Log the entire response for debugging

        # Extract the question and options using parsing
        lines = response.strip().splitlines()
        question_text = ""
        options = []
        correct_answer = None

        # Parse response to extract question and options
        parsing_options = False
        for line in lines:
            line = line.strip()

            # Extract question
            if line.lower().startswith("question:"):
                question_text = line.replace("Question:", "").strip()
                continue

            # Extract options
            if line.lower().startswith("options:"):
                parsing_options = True
                continue

            if parsing_options and re.match(r"^[A-D]\)", line):
                # Extract option and identify if it's the correct answer
                if '*' in line:
                    correct_answer = line[0].lower()  # Extract 'a', 'b', 'c', or 'd'
                    line = line.replace('*', '').strip()

                options.append(line)

            # Stop parsing if we find something irrelevant
            if "explanation" in line.lower() or "choose the correct" in line.lower():
                break

        # Validate the parsing result
        if not question_text or not options or correct_answer is None:
            raise ValueError("Incomplete question, options, or correct answer in the response")

        # Log the parsed question, options, and correct answer
        print(f"[DEBUG] Parsed Question: {question_text}")
        print("[DEBUG] Options:")
        for opt in options:
            print(f"  - {opt}")
        print(f"[DEBUG] Correct Answer: {correct_answer}\n")

        # Return structured response
        return {
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer
        }

    except ValueError as ve:
        print(f"[ERROR] Value error while processing response: {ve}")  # Log the error for debugging
        raise HTTPException(status_code=400, detail=f"Value error while processing response: {str(ve)}")
    except Exception as e:
        # Log the full error traceback for debugging
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error generating question: {str(e)}")

# To run the server, use the following command:
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
