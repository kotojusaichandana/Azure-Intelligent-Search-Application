from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# -------------------------------
# Load Dataset
# -------------------------------
data = pd.read_csv("data/documents.csv")

# Combine title and content for better search
data["combined_text"] = data["title"] + " " + data["content"]

# -------------------------------
# Train TF-IDF Model
# -------------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["combined_text"])

# -------------------------------
# Home Page Route
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Search Route
# -------------------------------
@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()

    if not query:
        return render_template("index.html")

    # STRICT TITLE-ONLY SEARCH
    results = data[
        data["title"].str.lower().str.split().apply(
            lambda words: query in words
        )
    ]

    return render_template(
        "index.html",
        results=results.to_dict(orient="records"),
        query=query
    )




# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
