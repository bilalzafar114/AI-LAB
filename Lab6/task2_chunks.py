
import re


def word_spans(text):
   
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]


def windows(text, size=40, overlap=10, offset=0):
    
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")
    spans = word_spans(text)
    result = []
    for i in range(0, len(spans), size - overlap):
        j = min(i + size, len(spans))
        result.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return result


def sentence_chunks(text, size=40):
   
    if size <= 0:
        raise ValueError("size must be positive")
    cuts = [0] + [m.end() for m in
                  re.finditer(r"[.!?]\s+", text)] + [len(text)]
    out, pending, count = [], None, 0
    for a, b in zip(cuts, cuts[1:]):
        segment = text[a:b]
        n = len(segment.split())
        if not n:
            continue
        if n > size:
            if pending is not None:
                out.append(pending)
            out.extend(windows(segment, size, 0, a))
            pending, count = None, 0
        elif pending is not None and count + n <= size:
            pending, count = (pending[0], b), count + n
        else:
            if pending is not None:
                out.append(pending)
            pending, count = (a, b), n
    if pending is not None:
        out.append(pending)
    return out


def make_chunks(docs, strategy, size=40):
    
    result = []
    for doc_id, text in docs.items():
        spans = (sentence_chunks(text, size) if strategy == "sentence"
                 else windows(text, size, int(strategy)))
        for i, (a, b) in enumerate(spans):
            result.append(dict(id=f"{doc_id}:{i}", doc=doc_id,
                               start=a, end=b, text=text[a:b]))
    return result



assert windows("") == []
assert sentence_chunks("") == []
assert make_chunks({"empty": ""}, "sentence") == []

assert windows("short text") == [(0, 10)]
assert sentence_chunks("Short text.") == [(0, 11)]

for bad in [(2, 2), (2, 5), (2, -1), (0, 0)]:
    try:
        windows("a b c", *bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Invalid args {bad} were accepted")
try:
    sentence_chunks("a b", 0)
except ValueError:
    pass
else:
    raise AssertionError("size=0 was accepted")

long = " ".join(["word"] * 95) + "."
spans = sentence_chunks(long)
assert len(spans) == 3, spans
assert all(len(long[a:b].split()) <= 40 for a, b in spans)

docs = {"example": "Reset your password. Keep recovery codes private."}
for strategy in ["0", "10", "sentence"]:
    for c in make_chunks(docs, strategy):
        assert c["text"] == docs[c["doc"]][c["start"]:c["end"]]
        assert c["text"].strip()
        print(strategy, c)

t = " ".join(f"w{i}" for i in range(100))
w = windows(t, 40, 10)
first, second = t[w[0][0]:w[0][1]].split(), t[w[1][0]:w[1][1]].split()
assert first[-10:] == second[:10]
print("All task2_chunks tests passed")
