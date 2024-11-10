import streamlit as st
import requests

# Streamlit settings
st.set_page_config(page_title="Data Science Interview Prep Bot", page_icon='🧠', layout='centered')

# Title and Header
st.title("Data Science Interview Prep Bot🧠")
st.subheader("Select a Topic You Want to Practice:")

# Topic Selection (Retain topic selection between interactions)
if "topic" not in st.session_state:
    st.session_state.topic = None

st.session_state.topic = st.selectbox(
    'Select a Topic',
    ['Machine Learning', 'Data Structures', 'Python', 'Generative AI', 'Computer Vision', 'Deep Learning'],
    index=['Machine Learning', 'Data Structures', 'Python', 'LLM', 'Computer Vision', 'Deep Learning'].index(st.session_state.topic)
    if st.session_state.topic else 0
)

# Initialize session state for questions if not already present
if "questions" not in st.session_state:
    st.session_state.questions = []

# Function to fetch a new question from the backend
def get_new_question():
    with st.spinner('Fetching question...'):
        try:
            response = requests.post("http://localhost:8000/get_question/", json={"category": st.session_state.topic})
            if response.status_code == 200:
                question_data = response.json()
                question = question_data.get("question", "")
                options = question_data.get("options", [])
                correct_answer = question_data.get("correct_answer", "A")

                # Append the new question to the questions list
                st.session_state.questions.append({
                    "question": question,
                    "options": options,
                    "correct_answer": correct_answer,
                    "selected_option": None,
                    "submitted": False,
                    "feedback": None
                })
            else:
                st.error("Error fetching question. Please try again.")
                return
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return

# Get a Question Button
if st.button('Get Question'):
    get_new_question()

# Display All Questions
for idx, q in enumerate(st.session_state.questions):
    st.write(f"**Question {idx + 1}:**")
    st.markdown(f"> {q['question']}")

    option_labels = [f"{chr(97 + i)})" for i in range(len(q['options']))]
    option_dict = {option_labels[i]: q['options'][i] for i in range(len(q['options']))}

    # Display options using a radio button and persist the user's choice
    selected_option = st.radio(
        f"Select an Answer for Question {idx + 1}:", 
        list(option_dict.keys()),
        index=list(option_dict.keys()).index(q['selected_option']) if q['selected_option'] else 0,
        format_func=lambda x: f"{x} {option_dict[x]}",
        disabled=q['submitted'],
        key=f"radio_{idx}"
    )
    st.session_state.questions[idx]['selected_option'] = selected_option

    # Submit Answer Button
    if not q['submitted'] and st.button(f'Submit Answer for Question {idx + 1}', key=f"submit_{idx}"):
        if selected_option:
            correct_label_index = ord(q['correct_answer'].upper()) - ord('A')
            correct_label = f"{chr(97 + correct_label_index)})"

            if selected_option == correct_label:
                st.session_state.questions[idx]['feedback'] = {
                    "message": f"Correct! {selected_option} {option_dict[selected_option]} is the right answer.",
                    "status": "success"
                }
            else:
                st.session_state.questions[idx]['feedback'] = {
                    "message": f"Incorrect! You selected {selected_option} {option_dict[selected_option]}.",
                    "status": "error"
                }
                st.session_state.questions[idx]['feedback']["info"] = f"The correct answer is: {correct_label} {option_dict[correct_label]}"

            st.session_state.questions[idx]['submitted'] = True

    # Display feedback after submission
    if q['feedback']:
        if q['feedback']["status"] == "success":
            st.success(q['feedback']["message"])
        elif q['feedback']["status"] == "error":
            st.error(q['feedback']["message"])
            if "info" in q['feedback']:
                st.info(q['feedback']["info"])

# Next Question Button to add a new question after the current ones
if st.button('Next Question'):
    get_new_question()

