import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, classification_report
from xgboost import XGBClassifier

# ==========================================
# LOAD DATA
# ==========================================
df = pd.read_csv("customer_product_training.csv")

# Example columns:
# customer_id
# product_id
# product_category
# age
# income
# customer_tenure
# total_products_owned
# category_products_owned
# pct_products_owned_category
# category_review_count
# category_contact_count
# category_spend
# product_price
# product_popularity
# product_avg_rating
# bought

# ==========================================
# FEATURE LIST
# ==========================================
categorical_features = [
    "product_id",
    "product_category"
]

numerical_features = [
    "age",
    "income",
    "customer_tenure",
    "total_products_owned",
    "category_products_owned",
    "pct_products_owned_category",
    "category_review_count",
    "category_contact_count",
    "category_spend",
    "product_price",
    "product_popularity",
    "product_avg_rating"
]

target = "bought"

# ==========================================
# PREPARE X AND y
# ==========================================
X = df[categorical_features + numerical_features]
y = df[target]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================================
# PREPROCESSING
# ==========================================
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numerical_features
        )
    ]
)

# ==========================================
# XGBOOST MODEL
# ==========================================
model = XGBClassifier(
    objective="binary:logistic",
    eval_metric="logloss",
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=5,  # adjust if imbalanced
    random_state=42
)

# ==========================================
# PIPELINE
# ==========================================
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# ==========================================
# TRAIN
# ==========================================
pipeline.fit(X_train, y_train)

# ==========================================
# EVALUATE
# ==========================================
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

print("ROC AUC:", roc_auc_score(y_test, y_prob))
print(classification_report(y_test, y_pred))

# ==========================================
# TOP RECOMMENDATIONS
# ==========================================
customer_id = 1001

candidate_products = X[
    df["customer_id"] == customer_id
].copy()

candidate_products["recommendation_score"] = (
    pipeline.predict_proba(candidate_products)[:, 1]
)

top_recommendations = (
    candidate_products
    .sort_values(
        "recommendation_score",
        ascending=False
    )
    .head(5)
)

print("\nTop Recommendations:")
print(
    top_recommendations[
        ["product_id", "recommendation_score"]
    ]
)
