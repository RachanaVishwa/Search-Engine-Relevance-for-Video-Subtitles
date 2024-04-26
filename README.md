# Search-Engine-Relevance-for-Video-Subtitles
Enhancing Search Engine Relevance for Video Subtitles

# step by step process

Part 1: Ingesting Documents
1. Read the given data.
    1. Observe that the given data is a database file.
    2. Go through the README.txt to understand what is there inside the database.
    3. Take care of decoding the files inside the database.
    4. If you have limited compute resources, you can take a random 30% of the data.
2. Apply appropriate cleaning steps on subtitle documents (whatever is required)
3. Experiment with the following to generate text vectors of subtitle documents:
    1. BOW / TFIDF to generate sparse vector representations. Note that this will only help you to build a Keyword Based Search Engine.
    2. BERT based “SentenceTransformers” to generate embeddings which encode semantic information. This can help us build a Semantic Search Engine.
4. (Must Implement) A very important step to improve the performance: Document Chunker.
    1. Consider the challenge of embedding large documents: Information Loss.
    2. It is often not practical to embed an entire document as a single vector, particularly when dealing with long documents.
    3. Solution: Divide a large document into smaller, more manageable chunks for embedding.
    4. Another Problem: Let’s say we set the token window to be 500, then we’d expect each chunk to be just below 500 tokens. One common concern of this method is that we might accidentally cut off some important text between chunks, splitting up the context. To mitigate this, we can set overlapping windows with a specified amount of tokens to overlap so we have tokens shared between chunks.
5. Store embeddings in a ChromaDB database. 

Part 2: Retrieving Documents
1. Take the user's search query.
2. Preprocess the query (if required).
3. Create query embedding.
4. Using cosine distance, calculate the similarity score between embeddings of documents and user search query embedding.
5. These cosine similarity scores will help in returning the most relevant candidate documents as per user’s search query.


# Results - 

<img width="460" alt="127 0 0 15000" src="https://github.com/RachanaVishwa/Search-Engine-Relevance-for-Video-Subtitles/assets/161026961/e1bb1281-d406-4f56-aaa0-586251dfb553">

![Search Results for All the best!](https://github.com/RachanaVishwa/Search-Engine-Relevance-for-Video-Subtitles/assets/161026961/dafe94f1-0b58-41dc-a704-85fd99cad667)


<img width="462" alt="Search Engine" src="https://github.com/RachanaVishwa/Search-Engine-Relevance-for-Video-Subtitles/assets/161026961/524ca4fa-b100-42c8-ac2d-281611334390">


![Search Results for You are a sweetheart!](https://github.com/RachanaVishwa/Search-Engine-Relevance-for-Video-Subtitles/assets/161026961/d4c800db-03ba-4321-bbf4-d505cd621681)
