import streamlit as st
import pickle
import re


# Load saved model
model = pickle.load(
    open("ticket_classifier.pkl", "rb")
)

# Load TF-IDF vectorizer
tfidf = pickle.load(
    open("tfidf_vectorizer.pkl", "rb")
)


# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# Urgency prediction

def predict_urgency(text):

    text = text.lower()


    high_keywords = [
        "urgent",
        "immediately",
        "critical",
        "emergency",
        "cannot use",
        "not working",
        "blocked",
        "lost access",
        "multiple charges"
    ]


    medium_keywords = [
        "problem",
        "issue",
        "error",
        "failed",
        "payment",
        "charged",
        "deducted",
        "refund",
        "transaction",
        "billing"
    ]


    for word in high_keywords:
        if word in text:
            return "High"


    for word in medium_keywords:
        if word in text:
            return "Medium"


    return "Low"
    

    for word in high_keywords:
        if word in text:
            return "High"

    for word in medium_keywords:
        if word in text:
            return "Medium"

    return "Low"



# ---------------- UI ----------------

st.title("🎫 Support Ticket Category Classifier")

st.write(
    "Enter a customer support ticket and get the predicted category and urgency."
)


ticket = st.text_area(
    "Enter Ticket Description"
)


if st.button("Predict"):

    if ticket.strip():

        # Clean text
        cleaned_ticket = clean_text(ticket)


        # Convert text to TF-IDF
        vector = tfidf.transform(
            [cleaned_ticket]
        )


        # Predict category
        category = model.predict(
            vector
        )[0]


        # Predict urgency
        urgency = predict_urgency(ticket)


        st.success(
            f"Predicted Category: {category}"
        )

        st.warning(
            f"Urgency Level: {urgency}"
        )

    else:
        st.error(
            "Please enter a ticket description"
        )