import json
from pathlib import Path

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
)
from sklearn.model_selection import train_test_split


# ============================================================
# PATHS
# ============================================================

DATA_FILE = Path("data/support_tickets.csv")

MODEL_DIR = Path("models")
REPORT_DIR = Path("reports")

MODEL_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 60)
print("CUSTOMER SUPPORT TICKET CLASSIFIER")
print("=" * 60)

print("\nLoading dataset...")

df = pd.read_csv(DATA_FILE)

print(f"Dataset shape: {df.shape}")


# ============================================================
# CHECK COLUMNS
# ============================================================

required_columns = [
    "Product_Service_Type",
    "Ticket_Description",
    "Issue_Category",
    "Priority",
]

for column in required_columns:

    if column not in df.columns:
        raise ValueError(
            f"Required column missing: {column}"
        )


# ============================================================
# CLEAN DATA
# ============================================================

df = df.dropna(
    subset=required_columns
).copy()


for column in [
    "Product_Service_Type",
    "Ticket_Description",
    "Issue_Category",
    "Priority",
]:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# ============================================================
# CREATE MODEL TEXT
# ============================================================

# Product is repeated so the classifier gets a strong
# signal from the Product / Service Type input.

df["model_text"] = (
    "Product "
    + df["Product_Service_Type"]
    + " Product "
    + df["Product_Service_Type"]
    + " Description "
    + df["Ticket_Description"]
)


X = df["model_text"]

y_category = df["Issue_Category"]

y_priority = df["Priority"]


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

indices = df.index


train_indices, test_indices = train_test_split(
    indices,
    test_size=0.20,
    random_state=42,
    stratify=y_category,
)


X_train = X.loc[train_indices]
X_test = X.loc[test_indices]

y_category_train = y_category.loc[train_indices]
y_category_test = y_category.loc[test_indices]

y_priority_train = y_priority.loc[train_indices]
y_priority_test = y_priority.loc[test_indices]


print()
print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))


# ============================================================
# CATEGORY VECTORIZER
# ============================================================

print()
print("Training Issue Category model...")


category_vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    min_df=1,
    sublinear_tf=True,
    strip_accents="unicode",
)


X_category_train = (
    category_vectorizer.fit_transform(
        X_train
    )
)


X_category_test = (
    category_vectorizer.transform(
        X_test
    )
)


# ============================================================
# CATEGORY MODEL
# ============================================================

category_model = LogisticRegression(
    max_iter=3000,
    C=10.0,
)


category_model.fit(
    X_category_train,
    y_category_train,
)


category_predictions = (
    category_model.predict(
        X_category_test
    )
)


category_accuracy = accuracy_score(
    y_category_test,
    category_predictions,
)


category_f1 = f1_score(
    y_category_test,
    category_predictions,
    average="weighted",
)


# ============================================================
# PRIORITY VECTORIZER
# ============================================================

print("Training Priority model...")


priority_vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    min_df=1,
    sublinear_tf=True,
    strip_accents="unicode",
)


X_priority_train = (
    priority_vectorizer.fit_transform(
        X_train
    )
)


X_priority_test = (
    priority_vectorizer.transform(
        X_test
    )
)


# ============================================================
# PRIORITY MODEL
# ============================================================

priority_model = LogisticRegression(
    max_iter=3000,
    C=10.0,
)


priority_model.fit(
    X_priority_train,
    y_priority_train,
)


priority_predictions = (
    priority_model.predict(
        X_priority_test
    )
)


priority_accuracy = accuracy_score(
    y_priority_test,
    priority_predictions,
)


priority_f1 = f1_score(
    y_priority_test,
    priority_predictions,
    average="weighted",
)


# ============================================================
# PRINT RESULTS
# ============================================================

print()
print("=" * 60)
print("CATEGORY RESULTS")
print("=" * 60)

print(
    f"Accuracy : {category_accuracy:.4f}"
)

print(
    f"F1 Score : {category_f1:.4f}"
)

print()
print(
    classification_report(
        y_category_test,
        category_predictions,
    )
)


print()
print("=" * 60)
print("PRIORITY RESULTS")
print("=" * 60)

print(
    f"Accuracy : {priority_accuracy:.4f}"
)

print(
    f"F1 Score : {priority_f1:.4f}"
)

print()
print(
    classification_report(
        y_priority_test,
        priority_predictions,
    )
)


# ============================================================
# SAVE MODELS
# ============================================================

joblib.dump(
    category_vectorizer,
    MODEL_DIR / "category_vectorizer.joblib",
)

joblib.dump(
    category_model,
    MODEL_DIR / "category_model.joblib",
)

joblib.dump(
    priority_vectorizer,
    MODEL_DIR / "priority_vectorizer.joblib",
)

joblib.dump(
    priority_model,
    MODEL_DIR / "priority_model.joblib",
)


# ============================================================
# SAVE METRICS
# ============================================================

category_metrics = {
    "accuracy": round(
        float(category_accuracy),
        4,
    ),
    "weighted_f1": round(
        float(category_f1),
        4,
    ),
}


priority_metrics = {
    "accuracy": round(
        float(priority_accuracy),
        4,
    ),
    "weighted_f1": round(
        float(priority_f1),
        4,
    ),
}


with open(
    REPORT_DIR / "category_metrics.json",
    "w",
    encoding="utf-8",
) as file:

    json.dump(
        category_metrics,
        file,
        indent=4,
    )


with open(
    REPORT_DIR / "priority_metrics.json",
    "w",
    encoding="utf-8",
) as file:

    json.dump(
        priority_metrics,
        file,
        indent=4,
    )


# ============================================================
# FINISHED
# ============================================================

print()
print("=" * 60)
print("TRAINING COMPLETE")
print("=" * 60)

print()
print("Models saved:")
print(
    " - models/category_vectorizer.joblib"
)
print(
    " - models/category_model.joblib"
)
print(
    " - models/priority_vectorizer.joblib"
)
print(
    " - models/priority_model.joblib"
)

print()
print("Reports saved:")
print(
    " - reports/category_metrics.json"
)
print(
    " - reports/priority_metrics.json"
)