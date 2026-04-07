from datasets import load_dataset


# ================================
# 🔹 Load Dataset
# ================================
def load_documents():

    print("📊 Loading SQuAD dataset...")

    dataset = load_dataset("squad", split="train[:50]")

    documents = [item["context"] for item in dataset]

    print(f"✅ Loaded {len(documents)} documents")

    return documents


# ================================
# 🔹 Simple Retrieval (Keyword-based)
# ================================
def retrieve_documents(documents, query):

    stopwords = {"what", "is", "an", "the", "a", "of", "in", "on", "at", "to"}

    query_words = [
        word.lower() for word in query.split()
        if word.lower() not in stopwords
    ]

    results = []

    for doc in documents:
        score = 0
        doc_lower = doc.lower()

        for word in query_words:
            if word in doc_lower:
                score += 1

        if score > 0:
            results.append((score, doc))

    # Sort by relevance (highest score first)
    results.sort(reverse=True, key=lambda x: x[0])

    # Return top 3 documents
    return [doc for score, doc in results[:3]]