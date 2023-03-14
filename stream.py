import streamlit as st
import random

def generate_question(context):
    # Generate a question based on the given context
    # Replace this with your own question generation logic
    questions = [
        f"{context} is a city in the United States.",
        f"Most people in {context} speak Spanish.",
        f"The weather in {context} is usually sunny.",
        f"{context} is known for its beautiful beaches.",
        f"{context} is a popular tourist destination.",
    ]
    question = random.choice(questions)
    answer = random.choice([True, False])
    return question, answer

def main():
    st.title("True/False Answer Generation App")

    # Prompt the user to enter a context
    context = st.text_input("Enter a context:")

    # When the user clicks the submit button, generate a question based on the context
    if st.button("Submit"):
        if context:
            question, answer = generate_question(context)
            st.write(f"Question: {question}")
            user_answer = st.radio("Your answer:", options=["True", "False"])
            if user_answer == str(answer):
                st.write("Correct!")
            else:
                st.write("Incorrect!")
                st.write(f"The correct answer is: {answer}")
        else:
            st.write("Please enter a context.")

if __name__ == "__main__":
    main()