from rag_pipeline import load_documents, retrieve_documents

print("🚀 Starting RAG System...\n")

# Load dataset
documents = load_documents()

# Memory
chat_history = []

print("\n✅ System Ready!")

while True:
    query = input("\n💬 Enter your question (or type 'exit'): ")

    if query.lower() == "exit":
        print("👋 Exiting...")
        break

    # ================================
    # 🔹 Context Resolution ("it")
    # ================================
    if query.lower().strip() in ["it", "explain it", "define it"]:
        if len(chat_history) > 0:
            query = chat_history[-1]
            print(f"👉 Interpreted as: {query}")

    # Store question
    chat_history.append(query)

    # Retrieve
    results = retrieve_documents(documents, query)

    if not results:
        print("\n❌ No relevant information found.")
    else:
        print("\n📌 Retrieved Results:\n")
        for r in results:
            print(r)
            print("\n---\n")

# Show stored questions
print("\n🧠 Stored Questions:")
for q in chat_history:
    print(q)