# 🎫 Support Ticket Category Classifier

## 🚀 AI-Powered Customer Support Ticket Classification System

An intelligent machine learning application that automatically analyzes customer support tickets and classifies them into appropriate categories.

The system uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to help support teams organize customer issues, prioritize requests, and improve response efficiency.

The project includes a complete ML pipeline and an interactive **Streamlit web application** where users can enter customer details and receive instant ticket predictions.

---

# 📌 Project Overview

Customer support teams receive thousands of tickets every day. Manually categorizing these requests is time-consuming and can delay customer responses.

This project solves that problem by automatically predicting the category of a customer ticket based on its description.

The application can identify:

- Billing issues
- Cancellation requests
- Product inquiries
- Refund requests
- Technical problems

It also predicts ticket urgency using keyword-based analysis.

---

# ✨ Features

## 👤 Customer Management

The application collects customer information:

- Customer Name
- Email Address
- Customer ID
- Product / Service details


## 🎫 Ticket Classification

Automatically predicts ticket category:

- 💳 Billing Inquiry
- ❌ Cancellation Request
- 📦 Product Inquiry
- 💰 Refund Request
- 🛠 Technical Issue


## ⚡ Ticket Urgency Prediction

The system identifies urgency levels:

### High Priority
Examples:
- urgent
- critical
- cannot access
- not working
- crash


### Medium Priority

Examples:
- issue
- error
- payment problem
- refund problem


### Low Priority

General information and product-related queries


---

# 🧠 Machine Learning Approach

## 1. Data Preprocessing

Customer ticket text is processed using:

- Lowercase conversion
- Text cleaning
- Removal of unwanted characters
- Combining ticket subject and description
- Stop word removal


---

## 2. Feature Extraction

### TF-IDF Vectorization

The textual information is converted into numerical features using:

**TF-IDF (Term Frequency - Inverse Document Frequency)**


This helps the model understand important words and patterns in customer requests.


---

## 3. Classification Model

Machine Learning algorithm used:
**Logistic Regression**


The model learns from previous customer tickets and predicts the most suitable support category.

---

# 📊 Model Performance

Final Model:
Algorithm:
Logistic Regression

Feature Extraction:
TF-IDF Vectorization
Performance:


Accuracy: 95%

Weighted F1 Score: 95%


The model provides reliable classification across multiple customer support categories.

---

# 🛠 Technologies Used

## Programming Language

- Python


## Machine Learning

- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer


## Data Processing

- Pandas
- NumPy


## Application Development

- Streamlit


## Development Tools

- Google Colab
- VS Code
- GitHub

---

# 📂 Project Structure


Support-Ticket-Classifier/

│
├── app.py
│
├── ticket_classifier.pkl
│
├── tfidf_vectorizer.pkl
│
├── requirements.txt
│
├── README.md
│
├── Support_Ticket_Classifier.ipynb
│
└── screenshots/
│
├── app_home.png
│
└── prediction_result.png


---

# 🖥 Application Preview

## Streamlit Interface

The application provides:

- Customer information input
- Ticket description input
- Category prediction
- Urgency prediction
- Ticket summary generation


### Example Prediction


Customer:
Akshitha

Product:
Laptop

Ticket:
"My laptop is not working and crashes frequently"

Prediction:

Category:
Technical Issue

Urgency:
High


---

# ⚙️ Installation and Setup

## 1. Clone Repository

```bash
git clone https://github.com/akshithasamudrala9515/Support-Ticket-Classifier.git
2. Navigate to Project Folder
cd Support-Ticket-Classifier
3. Install Dependencies
pip install -r requirements.txt
4. Run Streamlit Application
streamlit run app.py

The application will open in your browser.

📌 Sample Ticket Inputs
Technical Issue
My laptop is not working and the application crashes when opened.
Refund Request
I want a refund for my recent purchase.
Billing Inquiry
I was charged incorrectly for my payment.
Cancellation Request
I want to cancel my subscription.
Product Inquiry
I need information about product features.
🔮 Future Improvements

Future enhancements planned:

Add sentiment analysis
Add deep learning models
Add multilingual ticket support
Add automated ticket routing
Add analytics dashboard
Deploy application using cloud services
Integrate with customer support platforms
👩‍💻 Developer

Akshitha Samudrala

Computer Science and Engineering

Project:

Support Ticket Category Classifier

Technologies:

Python | NLP | Machine Learning | Streamlit

Model:

TF-IDF + Logistic Regression
⭐ Project Highlights

✅ End-to-end Machine Learning workflow
✅ NLP-based text classification
✅ Real-time Streamlit prediction system
✅ Customer details integration
✅ Automated ticket categorization
✅ GitHub-ready project structure

📜 License

This project is developed for educational and portfolio purposes.


### Small GitHub improvement:
Create this folder:


screenshots/


and add:


app_home.png
prediction_result.png


Then your repository will look like a professional ML portfolio project. ✅
