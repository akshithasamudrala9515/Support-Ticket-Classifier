# Customer Support Ticket Classifier

A machine learning application that automatically classifies customer support tickets based on the **Product / Service Type** and **Ticket Description**.

The application predicts two things:

1. **Issue Category**
2. **Priority**

The project uses Python, Scikit-learn, and Streamlit.

---

## Features

- Classifies customer support tickets automatically
- Predicts the issue category
- Predicts ticket priority
- Uses Product / Service Type as an input feature
- Uses Ticket Description as an input feature
- Simple Streamlit web interface
- No confidence score displayed to the user
- Priority levels are limited to:
  - Low
  - Medium
  - High

---

## Issue Categories

The classifier predicts one of the following categories:

- Technical
- Billing
- Account
- Fraud
- General Inquiry

---

## Priority Levels

The classifier predicts:

- Low
- Medium
- High

Critical priority is not used in this project.

---

## Project Structure

```text
support_ticket_classifier/
│
├── app.py
├── train.py
├── generate_dataset.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── support_tickets.csv
│
├── models/
│   ├── category_model.joblib
│   ├── category_vectorizer.joblib
│   ├── priority_model.joblib
│   └── priority_vectorizer.joblib
│
└── reports/
    ├── category_metrics.json
    └── priority_metrics.json
Dataset

The project uses a generated customer support ticket dataset containing 30,000 tickets.

Each ticket contains:

Ticket ID
Product / Service Type
Ticket Description
Issue Category
Priority

The dataset was generated with consistent category and priority patterns so that the machine learning models can learn the classification task effectively.

The dataset is used locally and is excluded from GitHub using .gitignore.

Machine Learning Approach

The project uses Natural Language Processing (NLP) to convert ticket descriptions into numerical features.

Text Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert text into numerical features.

The model uses:

Unigrams
Bigrams
Lowercase text
Unicode accent handling
Sublinear TF scaling

The Product / Service Type is also included as part of the model input.

Classification Algorithm

Logistic Regression is used for both classification tasks:

Issue Category Classification
Priority Classification

The dataset is divided into:

80% training data
20% testing data

A fixed random state is used to make the experiment reproducible.

Model Evaluation

The models are evaluated using:

Accuracy
Weighted F1 Score
Precision
Recall
Current Test Results

The current held-out test set contains 6,000 tickets.

Issue Category
Accuracy : 100%
F1 Score : 100%
Priority
Accuracy : 100%
F1 Score : 100%

All five issue categories achieved:

Precision : 1.00
Recall    : 1.00
F1 Score  : 1.00

The Low, Medium, and High priority classes also achieved:

Precision : 1.00
Recall    : 1.00
F1 Score  : 1.00

These results are based on the generated dataset and the held-out test split.

How the Application Works

The user provides two inputs:

1. Product / Service Type

Example:

Mobile App
2. Ticket Description

Example:

My mobile application is crashing and is completely unavailable.
Please resolve this immediately.

The application processes the input using the trained TF-IDF vectorizers and classification models.

The result is displayed as:

Issue Category: Technical
Priority: High
Installation

Clone the repository:

git clone https://github.com/akshithasamudrala9515/Support-Ticket-Classifier.git

Move into the project directory:

cd Support-Ticket-Classifier

Install the required Python packages:

python -m pip install -r requirements.txt
Generate the Dataset

Run:

python generate_dataset.py

This creates:

data/support_tickets.csv

with 30,000 customer support tickets.

Train the Models

Run:

python train.py

This trains both classifiers and creates:

models/category_model.joblib
models/category_vectorizer.joblib
models/priority_model.joblib
models/priority_vectorizer.joblib

Evaluation reports are saved in:

reports/
Run the Streamlit Application

Start the application using:

python -m streamlit run app.py

The Streamlit application will open in your web browser.

Example
Input

Product / Service Type

Mobile App

Ticket Description

My mobile application is crashing and is completely unavailable.
Please resolve this immediately.
Output
Issue Category: Technical
Priority: High
Technologies Used
Python
Pandas
Scikit-learn
TF-IDF
Logistic Regression
Joblib
Streamlit
Model Workflow
Customer Support Ticket
          |
          v
Product / Service Type
          +
Ticket Description
          |
          v
       TF-IDF
          |
          v
   Feature Representation
          |
          +----------------------+
          |                      |
          v                      v
 Category Classifier      Priority Classifier
          |                      |
          v                      v
 Issue Category             Priority
          |                      |
          +----------+-----------+
                     |
                     v
              Final Prediction
Results

The current experiment achieved:

Model	Accuracy	F1 Score
Issue Category	100%	100%
Priority	100%	100%

The evaluation was performed on a separate 20% test set containing 6,000 tickets.

Important Note

The reported 100% performance applies to the generated dataset used for this project and its held-out test split. Performance on real-world customer support tickets may be lower because real tickets can contain ambiguous, incomplete, or inconsistent descriptions.

Future Improvements

Possible improvements include:

Use a larger real-world customer support dataset
Add multilingual ticket support
Add model comparison
Add cross-validation
Add confusion matrix visualizations
Deploy the Streamlit application online
Add automated model retraining
Improve handling of previously unseen products and issues
Author

Akshitha Samudrala

Customer Support Ticket Classifier
Machine Learning + NLP + Streamlit