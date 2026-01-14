Project Overview :

The AI Intelligent Search Application is a web-based system that enables users to search internal organizational documents using natural language queries. Unlike traditional keyword-based search systems, this application uses Artificial Intelligence and Machine Learning techniques to understand user intent and retrieve the most relevant documents.

The project is implemented using Python and Flask and provides a clean, user-friendly web interface where search results are displayed in a structured and readable format.

🎯 Objectives

To develop an AI-powered document search system

To support natural language-based search queries

To apply NLP and Machine Learning techniques for semantic matching

To improve document retrieval accuracy

To provide a clean and professional web-based interface

✨ Key Features

Natural language document search

AI-based relevance matching using TF-IDF and cosine similarity

Filters out irrelevant documents automatically

Displays search results line-by-line in a user-friendly format

Simple and professional web interface using Flask templates

🏗️ System Architecture

Flow of the System:

User
 ↓
Web Browser
 ↓
Flask Application
 ↓
NLP & Machine Learning Model
 ↓
Document Dataset


The Flask application processes user queries, applies NLP techniques to compute similarity, and renders the search results using HTML templates for better readability.

🛠️ Technologies Used
Programming Language

Python

Framework

Flask

Libraries

Pandas

Scikit-learn

Techniques

Natural Language Processing (NLP)

TF-IDF Vectorization

Cosine Similarity

Frontend

HTML (Jinja2 Templates)

📁 Project Folder Structure
AI_Search_Project
│
├── app.py
│
├── data
│   └── documents.csv
│
└── templates
    └── index.html

⚙️ Installation & Setup
Step 1: Install Required Libraries
python -m pip install flask pandas scikit-learn

Step 2: Run the Application
python app.py

Step 3: Open in Browser

Open your web browser and go to:

 http://127.0.0.1:5000

🔍 How the Application Works

User enters a natural language query in the search box

The query is converted into numerical vectors using TF-IDF

Cosine similarity is used to measure relevance between query and documents

Documents with zero similarity are filtered out

Relevant results are displayed neatly on the web page

📊 Output

The application displays search results in a clear and structured format showing:

Document Title

Content

Department

Relevance Score

Only relevant documents are displayed, ensuring better accuracy and readability.

🎓 Academic Use

This project is suitable for:

AI / ML Mini Project

Internship Project

Laboratory Submission

Beginner-level AI implementation

🚀 Future Enhancements

Deploy the application on cloud platforms (Azure)

Use deep learning-based semantic embeddings

Add user authentication and role-based access

Enhance UI with CSS and advanced filtering

📚 References

Python Documentation: https://docs.python.org

Flask Documentation: https://flask.palletsprojects.com

Scikit-learn Documentation: https://scikit-learn.org

Pandas Documentation: https://pandas.pydata.org

👤 Author

Name: KOTOJU SAI CHANDANA
Admission Number: 23CSE1004
Department: Computer Science and Engineering

University: CHAITANYA DEEMED TO BE UNIVERSITY 
