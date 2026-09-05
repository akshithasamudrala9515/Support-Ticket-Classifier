import streamlit as st
import pickle
import re


# ---------------- Load Model ----------------

model = pickle.load(
    open("ticket_classifier.pkl", "rb")
)

tfidf = pickle.load(
    open("tfidf_vectorizer.pkl", "rb")
)


# ---------------- Text Cleaning ----------------

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-z0-9\s]',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()

    return text



# ---------------- Category Correction ----------------
def adjust_category(category, text):

    text = text.lower()


    product_keywords = [
        "details",
        "features",
        "availability",
        "available",
        "specifications",
        "specs",
        "information",
        "compare",
        "recommend",
        "price",
        "buy",
        "purchase"
    ]


    technical_keywords = [
        "crash",
        "crashing",
        "not boot",
        "boot failure",
        "system failure",
        "hardware",
        "software error",
        "blue screen",
        "device not working",
        "cannot access files",
        "lost files",
        "computer stopped",
        "laptop stopped",
        "system not working"
    ]


    refund_keywords = [
        "refund",
        "return my money",
        "money back",
        "return"
    ]


    billing_keywords = [
        "charged",
        "payment",
        "transaction",
        "billing",
        "deducted",
        "double charge"
    ]


    cancellation_keywords = [
        "cancel",
        "cancellation",
        "stop order"
    ]


    # Product inquiry first
    if any(word in text for word in product_keywords):
        return "Product inquiry"


    if any(word in text for word in technical_keywords):
        return "Technical issue"


    if any(word in text for word in refund_keywords):
        return "Refund request"


    if any(word in text for word in billing_keywords):
        return "Billing inquiry"


    if any(word in text for word in cancellation_keywords):
        return "Cancellation request"


    return category



# ---------------- Urgency Prediction ----------------

def predict_urgency(text):

    text = text.lower()


    high_keywords = [
        "urgent",
        "immediately",
        "critical",
        "emergency",
        "cannot use",
        "not working",
        "stopped working",
        "crash",
        "crashing",
        "system failure",
        "lost access",
        "cannot access",
        "cannot access files",
        "data loss",
        "lost files",
        "blocked",
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
        "billing",
        "slow"
    ]


    for word in high_keywords:

        if word in text:
            return "High"


    for word in medium_keywords:

        if word in text:
            return "Medium"


    return "Low"



# ---------------- Streamlit UI ----------------

st.title("🎫 Support Ticket Category Classifier")

st.caption(
    "AI-powered NLP system to classify customer support tickets and predict urgency levels"
)

st.info(
    "Model: Logistic Regression + TF-IDF"
)

st.write(
    "Enter a customer support ticket and get predicted category and urgency."
)


ticket = st.text_area(
    "Enter Ticket Description"
)






if st.button("Predict"):


    if ticket.strip():


        # Clean text

        cleaned_ticket = clean_text(ticket)


        # Convert to TF-IDF

        vector = tfidf.transform(
            [cleaned_ticket]
        )


        # Model prediction

        category = model.predict(
            vector
        )[0]


        # Apply correction rules

        category = adjust_category(
            category,
            ticket
        )


        # Urgency

        urgency = predict_urgency(
            ticket
        )


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
# ---------------- Footer ----------------

# ---------------- Footer ----------------

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        text-align: center;
        padding: 8px;
        font-size: 12px;
        border-top: 1px solid #ddd;
    }
    </style>

    <div class="footer">
   Support Ticket Category Classifier | Developed by Akshitha Samudrala | NLP • ML • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)