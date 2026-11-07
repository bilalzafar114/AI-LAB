"""Task 1 (Beginner): whitespace vs Unicode word-like regex tokens.

Run: python task1_tokens.py
The model-tokenizer comparison is optional: it needs sentence-transformers
and a one-time model download. If unavailable, that part is skipped.
"""
import re

samples = [
    ("punctuation", "AI, search!"),
    ("contraction", "I can't log in."),
    ("email", "help@example.com"),
    ("identifier", "CS4944"),
    ("empty string", ""),
    ("Urdu", "یہ ایک مثال ہے"),
    ("mixed", "Submit CS4944 late? No!"),
]

print("=" * 70)
print("TOKEN COMPARISON: whitespace split vs word-like regex")
print("=" * 70)
for label, text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(f"[{label}]")
    print("  original   :", repr(text))
    print("  whitespace :", ws, "->", len(ws))
    print("  word-like  :", words, "->", len(words))

assert re.findall(r"\b\w+\b", "") == []
assert "I can't log in.".split() == ["I", "can't", "log", "in."]
assert re.findall(r"\b\w+\b", "I can't log in.") == ["I", "can", "t", "log", "in"]
assert len("AI, search!".split()) == 2
assert len(re.findall(r"\b\w+\b", "AI, search!")) == 2

print()
print("=" * 70)
print("MODEL SUB-WORD TOKENIZER (all-MiniLM-L6-v2)")
print("=" * 70)
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    for text in ["I can't log in.", "CS4944"]:
        pieces = model.tokenizer.tokenize(text)
        print(repr(text), "->", pieces, len(pieces))
except Exception as exc:
    print("Model tokenizer skipped:", type(exc).__name__, "-", exc)
    print("(Install sentence-transformers and rerun to record sub-word lists.)")

