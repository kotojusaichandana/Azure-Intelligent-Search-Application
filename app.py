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
    query = request.args.get("q")

    if not query:
        return render_template("index.html")

    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

    data["score"] = similarity_scores

    results = data[data["score"] > 0].sort_values(
        by="score", ascending=False
    ).head(5)

    return render_template(
        "index.html",
        results=results.to_dict(orient="records")
    )

# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
