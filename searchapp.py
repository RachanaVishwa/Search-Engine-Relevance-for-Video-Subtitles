from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pandas as pd
import re

app = Flask(__name__)

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the subtitle data
subtitle_data = pd.read_csv('embdata.csv')  # Assuming you have a CSV file containing subtitle data

# Function to preprocess the user query
def preprocess_query(query):
    cleaned_query = re.sub(r'[^a-zA-Z\s]', '', query).lower()
    return cleaned_query

# Function to retrieve top-n most relevant documents
def retrieve_documents(user_query, top_n=5):
    processed_query = preprocess_query(user_query)
    query_embedding = model.encode([processed_query])[0]
    document_embeddings = model.encode(subtitle_data['embedding'].tolist())
    similarity_scores = cosine_similarity(query_embedding.reshape(1, -1), document_embeddings)
    top_indices = similarity_scores.argsort()[-top_n:][::-1]
    top_documents = subtitle_data.iloc[top_indices]
    return top_documents

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form['query']
    top_relevant_documents = retrieve_documents(user_query)
    return render_template('search_results.html', query=user_query, documents=top_relevant_documents.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
