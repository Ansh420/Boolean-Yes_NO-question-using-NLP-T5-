# Boolean-Yes_NO-question-using-NLP-T5-

## Project Overview
This repository contains a Python application built using **NLP** and the **T5 transformer** model to answer **yes/no** questions. The application takes a question as input and provides a **boolean response** (yes or no) based on its understanding of the query.

## Prerequisites
Before you can run this application, ensure you have the following installed:

- **Python**: Version 3.6 or later 

## Required Libraries:
- Transformers.
- Streamlit.
- Pandas.
- Numpy.


## Usage
**Prepare Your Data**:

- Create a **CSV** file (e.g., data.csv) with two columns: question and answer.
- Populate the file with your question-answer pairs.

## Train the Model:

Run the training script:
**Bash**
python **train.py** --data_file **data.csv**

 -The trained model will be saved in the models directory.
# Start the Streamlit App:

Bash
- streamlit run **app.py**
- Open your web browser and navigate to **http://localhost:8501/**.

  
## How the Application Works
- **Input**: The user enters a question in the Streamlit interface.
- **Preprocessing**: The question is tokenized and converted into a format suitable for the T5 model.
- **Inference**: The T5 model processes the input and generates a predicted answer.
- **Output**: The application displays the predicted answer **(yes or no)** to the user.
  
## Deployment
You can deploy this application to a cloud platform like **Heroku or AWS** for wider accessibility. Follow the specific deployment instructions for your chosen platform.
