from pathlib import Path

import joblib
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Support Ticket Classifier",
    page_icon="🎫",
    layout="centered",
)


# ============================================================
# MODEL PATH
# ============================================================

MODEL_DIR = Path("models")


# ============================================================
# LOAD MODELS
# ============================================================

category_vectorizer = joblib.load(
    MODEL_DIR / "category_vectorizer.joblib"
)

category_model = joblib.load(
    MODEL_DIR / "category_model.joblib"
)

priority_vectorizer = joblib.load(
    MODEL_DIR / "priority_vectorizer.joblib"
)

priority_model = joblib.load(
    MODEL_DIR / "priority_model.joblib"
)


# ============================================================
# TITLE
# ============================================================

st.title(
    "🎫 Customer Support Ticket Classifier"
)

st.write(
    "Enter the product or service type and "
    "describe the customer's issue."
)


# ============================================================
# INPUT 1
# ============================================================

product_type = st.text_input(
    "Product / Service Type"
)


# ============================================================
# INPUT 2
# ============================================================

ticket_description = st.text_area(
    "Ticket Description",
    height=180,
)


# ============================================================
# CLASSIFY
# ============================================================

if st.button(
    "Classify Ticket",
    type="primary",
    use_container_width=True,
):

    if not product_type.strip():

        st.warning(
            "Please enter the Product / Service Type."
        )

    elif not ticket_description.strip():

        st.warning(
            "Please enter the Ticket Description."
        )

    else:

        model_text = (
            "Product "
            + product_type.strip()
            + " Product "
            + product_type.strip()
            + " Description "
            + ticket_description.strip()
        )


        # ----------------------------------------------------
        # CATEGORY
        # ----------------------------------------------------

        category_features = (
            category_vectorizer.transform(
                [model_text]
            )
        )

        predicted_category = (
            category_model.predict(
                category_features
            )[0]
        )


        # ----------------------------------------------------
        # PRIORITY
        # ----------------------------------------------------

        priority_features = (
            priority_vectorizer.transform(
                [model_text]
            )
        )

        predicted_priority = (
            priority_model.predict(
                priority_features
            )[0]
        )


        # ----------------------------------------------------
        # DISPLAY
        # ----------------------------------------------------

        st.success(
            "Ticket classified successfully!"
        )

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "Issue Category"
            )

            st.info(
                predicted_category
            )


        with col2:

            st.subheader(
                "Priority"
            )

            st.info(
                predicted_priority
            )