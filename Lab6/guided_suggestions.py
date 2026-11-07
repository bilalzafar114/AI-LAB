import sys
from guided_chatbot import build_bot

backend = sys.argv[1] if len(sys.argv) > 1 else "tfidf"
query = sys.argv[2] if len(sys.argv) > 2 else "assignment upload"
engine = build_bot(backend)
print(f"Backend: {backend} | Query: {query!r}")
print("Suggested questions:")
for record, score in engine.search(query, k=3):
    if backend == "embedding" or score > 0:
        print(record["question"], f"({score:.3f})")
