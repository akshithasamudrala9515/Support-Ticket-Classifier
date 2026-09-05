import streamlit as st
import pickle
import re
from datetime import datetime
import random


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Support Ticket Desk",
    page_icon="🎫",
    layout="wide"
)


# ---------------- CSS ----------------

st.markdown(
"""
<style>

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}


h1 {
    text-align:center;
    font-size:42px;
}


.subtitle {
    text-align:center;
    color:gray;
}


.stButton button {
    width:100%;
    height:45px;
    font-size:18px;
}


</style>
""",
unsafe_allow_html=True
)



# ---------------- LOAD MODEL ----------------

model = pickle.load(
    open("ticket_classifier.pkl","rb")
)


tfidf = pickle.load(
    open("tfidf_vectorizer.pkl","rb")
)



# ---------------- TEXT CLEANING ----------------

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-z\s]',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()

    return text




# ---------------- URGENCY PREDICTION ----------------

def predict_urgency(text):

    text = text.lower()


    high_keywords = [

        "urgent",
        "critical",
        "cannot use",
        "not working",
        "blocked",
        "lost access",
        "crash",
        "crashing",
        "unable to access",
        "emergency"

    ]


    medium_keywords = [

        "issue",
        "problem",
        "error",
        "failed",
        "payment",
        "charged",
        "refund",
        "billing",
        "transaction"

    ]


    for word in high_keywords:

        if word in text:

            return "High"



    for word in medium_keywords:

        if word in text:

            return "Medium"



    return "Low"




# ---------------- HEADER ----------------


st.markdown(
"""
<h1>🎫 Support Ticket Category Classifier</h1>

<p class="subtitle">
AI-powered NLP system to classify customer support tickets
and predict urgency levels
</p>

""",
unsafe_allow_html=True
)



st.info(
    "Model: Logistic Regression + TF-IDF"
)




# ---------------- CUSTOMER DETAILS ----------------


st.subheader(
    "👤 Customer & Ticket Details"
)



col1,col2,col3 = st.columns(3)


with col1:

    customer_name = st.text_input(
        "Customer Name"
    )


with col2:

    customer_id = st.text_input(
        "Customer ID"
    )


with col3:

    product_name = st.text_input(
        "Product / Service"
    )



col4,col5 = st.columns(2)


with col4:

    customer_email = st.text_input(
        "Email Address"
    )


with col5:

    ticket = st.text_area(
        "Ticket Description",
        height=100
    )





# ---------------- PREDICT BUTTON ----------------


if st.button(
    "🚀 Predict Ticket"
):


    if ticket.strip():


        cleaned_ticket = clean_text(
            ticket
        )


        vector = tfidf.transform(
            [cleaned_ticket]
        )


        category = model.predict(
            vector
        )[0]


        urgency = predict_urgency(
            ticket
        )


        ticket_id = (

            "TKT" +
            str(
                random.randint(
                    1000,
                    9999
                )
            )

        )



        created_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )



       # ---------------- RESULT ----------------
# ---------------- RESULT ----------------

st.markdown("---")

st.subheader("📋 Ticket Summary")


r1, r2, r3, r4 = st.columns(4)


with r1:
    st.success(
        f"""
        🎫

        **Ticket ID**

        {ticket_id}
        """
    )


with r2:
    st.info(
        f"""
        👤

        **Customer**

        {customer_name}
        """
    )


with r3:
    st.success(
        f"""
        📌

        **Category**

        {category}
        """
    )


with r4:
    st.warning(
        f"""
        ⚡

        **Urgency**

        {urgency}
        """
    )


st.markdown(
    f"""
    **Product:** {product_name}  

    **Email:** {customer_email}  

    **Status:** Open  

    **Created:** {created_time}
    """
)


# ---------------- FOOTER ----------------


st.markdown(
"""
<hr>

<center>

<b>Support Ticket Category Classifier</b><br>

Developed by <b>Akshitha Samudrala</b> |
NLP • Machine Learning • Streamlit

</center>

""",
unsafe_allow_html=True
)