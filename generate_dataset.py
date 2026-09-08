import random
from pathlib import Path

import pandas as pd


random.seed(42)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "support_tickets.csv"


# ============================================================
# PRODUCT, CATEGORY AND ISSUE INFORMATION
# ============================================================

PRODUCTS = {
    "Mobile App": {
        "category": "Technical",
        "issues": [
            "mobile application is crashing",
            "mobile application is freezing",
            "mobile application is not opening",
            "mobile application shows an error",
            "mobile application stopped working",
        ],
    },
    "Website": {
        "category": "Technical",
        "issues": [
            "website is not loading",
            "website is showing an error",
            "website is not responding",
            "website keeps crashing",
            "website is unavailable",
        ],
    },
    "Internet Service": {
        "category": "Technical",
        "issues": [
            "internet connection is slow",
            "internet connection keeps disconnecting",
            "internet service is unavailable",
            "network connection is failing",
            "wifi connection is not working",
        ],
    },
    "Credit Card": {
        "category": "Billing",
        "issues": [
            "credit card was charged incorrectly",
            "credit card shows an unexpected charge",
            "wrong amount was charged to the credit card",
            "card payment amount is incorrect",
            "credit card billing has an error",
        ],
    },
    "Subscription": {
        "category": "Billing",
        "issues": [
            "subscription payment is incorrect",
            "subscription renewal has an unexpected charge",
            "subscription amount is wrong",
            "subscription billing has an error",
            "subscription payment was charged incorrectly",
        ],
    },
    "Invoice": {
        "category": "Billing",
        "issues": [
            "invoice amount is incorrect",
            "invoice contains an error",
            "invoice payment has a problem",
            "wrong amount is shown on the invoice",
            "billing invoice is incorrect",
        ],
    },
    "User Account": {
        "category": "Account",
        "issues": [
            "cannot access my account",
            "account login is not working",
            "unable to log in to my account",
            "account access is blocked",
            "account sign in is failing",
        ],
    },
    "Password Service": {
        "category": "Account",
        "issues": [
            "password reset is not working",
            "unable to reset my password",
            "forgot password and cannot recover it",
            "password reset link is failing",
            "password recovery is not working",
        ],
    },
    "Bank Transfer": {
        "category": "Fraud",
        "issues": [
            "there is an unauthorized bank transfer",
            "unknown bank transfer appears on my account",
            "suspicious bank transaction was detected",
            "bank transfer was not made by me",
            "fraudulent bank transfer is showing",
        ],
    },
    "Online Payment": {
        "category": "Fraud",
        "issues": [
            "there is an unauthorized online payment",
            "unknown online payment appears on my account",
            "suspicious payment was detected",
            "online payment was not authorized by me",
            "fraudulent online transaction is showing",
        ],
    },
    "General Service": {
        "category": "General Inquiry",
        "issues": [
            "I need information about the service",
            "I have a general question about the product",
            "I would like more information",
            "I need clarification about the service",
            "I have a general service question",
        ],
    },
}


# ============================================================
# PRIORITY-SPECIFIC PHRASES
# ============================================================

PRIORITY_PHRASES = {
    "High": [
        "This is urgent and needs immediate attention.",
        "Please resolve this immediately.",
        "This is a critical issue.",
        "The service is completely unavailable.",
        "I cannot access the service and need urgent help.",
        "This is causing a major service disruption.",
        "Please treat this as an urgent request.",
    ],
    "Medium": [
        "This issue is causing some inconvenience.",
        "Please resolve this problem as soon as possible.",
        "I would appreciate assistance with this issue.",
        "The problem is affecting my normal usage.",
        "Please investigate this issue.",
        "The service is not working correctly.",
        "I need help resolving this problem.",
    ],
    "Low": [
        "I would like some information about this.",
        "This is a general question.",
        "I need some clarification.",
        "This is not urgent.",
        "Please provide more information.",
        "I would like to know more about this service.",
        "I have a simple request.",
    ],
}


# ============================================================
# CUSTOMER PHRASES
# ============================================================

CUSTOMER_PHRASES = [
    "Please help me with this issue.",
    "Could you please assist me?",
    "I would appreciate your help.",
    "Please look into this matter.",
    "Can you help me resolve this?",
    "I need support with this problem.",
    "Please provide assistance.",
]


# ============================================================
# CREATE DATASET
# ============================================================

NUM_TICKETS = 30000

product_names = list(PRODUCTS.keys())
priority_names = ["Low", "Medium", "High"]

rows = []


for ticket_number in range(1, NUM_TICKETS + 1):

    product = random.choice(product_names)

    category = PRODUCTS[product]["category"]

    priority = random.choices(
        priority_names,
        weights=[40, 40, 20],
        k=1,
    )[0]

    issue = random.choice(PRODUCTS[product]["issues"])

    priority_phrase = random.choice(
        PRIORITY_PHRASES[priority]
    )

    customer_phrase = random.choice(
        CUSTOMER_PHRASES
    )

    description = (
        f"{issue}. "
        f"{priority_phrase} "
        f"{customer_phrase}"
    )

    rows.append(
        {
            "Ticket_ID": f"TKT-{ticket_number:05d}",
            "Product_Service_Type": product,
            "Ticket_Description": description,
            "Issue_Category": category,
            "Priority": priority,
        }
    )


df = pd.DataFrame(rows)


# ============================================================
# SAVE DATASET
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False,
)


print()
print("=" * 60)
print("CUSTOMER SUPPORT DATASET CREATED")
print("=" * 60)

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print()
print("Columns:")
for column in df.columns:
    print(f" - {column}")

print()
print("Issue Category distribution:")
print(df["Issue_Category"].value_counts())

print()
print("Priority distribution:")
print(df["Priority"].value_counts())

print()
print(f"Dataset saved to:")
print(OUTPUT_FILE)

print("=" * 60)