# Support Ticket Category Classifier

## Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to automatically classify customer support tickets into different categories and predict ticket urgency levels.

The system helps support teams organize incoming customer issues and improve response efficiency.



## Features

- Customer ticket classification
- Ticket urgency prediction (High / Medium / Low)
- TF-IDF text feature extraction
- LinearSVC machine learning model
- Rule-based ticket priority handling
- Streamlit web application
---

## Ticket Categories

The model predicts the following categories:

- Billing inquiry
- Cancellation request
- Product inquiry
- Refund request
- Technical issue

---

## Machine Learning Approach

### Text Processing:
- Text cleaning
- Lowercase conversion
- Removal of unwanted characters
- TF-IDF vectorization with n-grams

### Model:
- Linear Support Vector Classifier (LinearSVC)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF
- Streamlit

---

## Model Performance

The final model achieved:

Model:
LinearSVC with TF-IDF features

Accuracy:
93.06%

F1 Score:
93.17%

Evaluation was performed using a test dataset with multiple support ticket categories.

---

## Project Structure
Support-Ticket-Classifier/

│── app.py
│── ticket_classifier.pkl
│── tfidf_vectorizer.pkl
│── requirements.txt
│── README.md
│── Support_Ticket_Classifier.ipynb

---

## How to Run

### 1. Clone the repository

### 2. Install dependencies

### 3. Run Streamlit application


---

## Future Improvements

- Add sentiment analysis
- Add prediction confidence score
- Add ticket analytics dashboard
- Deploy application online