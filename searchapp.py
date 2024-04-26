from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Initialize Flask app
app = Flask(__name__)

# Load the data
df = pd.read_csv('/Users/rachusarang/Downloads/embdata.csv')

# Load SBERT model
sbert_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Create document embeddings
def create_document_embeddings(texts):
    embeddings = sbert_model.encode(texts)
    normalized_embeddings = embeddings / (embeddings**2).sum(axis=1, keepdims=True)**0.5
    return normalized_embeddings

# Calculate similarity scores
def calculate_similarity(query_embedding, document_embeddings):
    similarity_scores = cosine_similarity(query_embedding.reshape(1, -1), document_embeddings)[0]
    return similarity_scores

# Homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        if query:
            # Create query embedding
            query_embedding = sbert_model.encode(query)
            # Calculate similarity scores
            similarity_scores = calculate_similarity(query_embedding, document_embeddings)
            # Add similarity scores to DataFrame
            df['similarity_score'] = similarity_scores
            # Sort documents based on similarity scores
            df_sorted = df.sort_values(by='similarity_score', ascending=False)
            # Retrieve top N most similar documents
            top_n = 10
            top_similar_documents = df_sorted.head(top_n)
            # Pass top similar documents to HTML template
            return render_template('search_results.html', query=query, documents=top_similar_documents)
    return render_template('index.html')

if __name__ == '__main__':
    # Create document embeddings
    document_embeddings = create_document_embeddings(df['clean_file_content'])
    # Run the app
    app.run(debug=True)
