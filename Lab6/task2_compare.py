
import re
import statistics

from task2_chunks import make_chunks, sentence_chunks
from task2_docs import DOCS, EVIDENCE

STRATEGIES = ["0", "10", "sentence"]
LABEL = {"0": "window overlap=0", "10": "window overlap=10",
         "sentence": "sentence-aware"}
original_words = sum(len(t.split()) for t in DOCS.values())

print("Corpus:", {d: len(t.split()) for d, t in DOCS.items()},
      "total words =", original_words)

print("\n=== 1. Counts, sizes and repeated text ===")
header = f"{'strategy':<20}{'chunks':>7}{'min':>5}{'mean':>7}{'max':>5}" \
         f"{'emitted':>9}{'duplicate':>11}"
print(header)
all_chunks = {}
for s in STRATEGIES:
    chunks = make_chunks(DOCS, s)
    all_chunks[s] = chunks
    sizes = [len(c["text"].split()) for c in chunks]
    emitted = sum(sizes)
    print(f"{LABEL[s]:<20}{len(chunks):>7}{min(sizes):>5}"
          f"{statistics.mean(sizes):>7.1f}{max(sizes):>5}"
          f"{emitted:>9}{emitted - original_words:>11}")
    for c in chunks:
        assert c["text"] == DOCS[c["doc"]][c["start"]:c["end"]]
        assert len(c["text"].split()) <= 40
print("(duplicate = total emitted words - original words)")

print("\n=== 2. Does each rule + exception survive in ONE chunk? ===")
print(f"{'evidence':<24}{'words':>6}  " +
      "  ".join(f"{LABEL[s]:<18}" for s in STRATEGIES))
survival = {s: 0 for s in STRATEGIES}
for ev in EVIDENCE:
    row = []
    for s in STRATEGIES:
        ok = any(c["doc"] == ev["doc"] and ev["evidence"] in c["text"]
                 for c in all_chunks[s])
        survival[s] += ok
        row.append(f"{'YES' if ok else 'NO':<18}")
    print(f"{ev['id']:<24}{len(ev['evidence'].split()):>6}  " + "  ".join(row))
print(f"{'TOTAL kept intact':<30}  " + "  ".join(
    f"{survival[s]}/{len(EVIDENCE)}".ljust(18) for s in STRATEGIES))
too_long = [e["id"] for e in EVIDENCE if len(e["evidence"].split()) > 40]
print(f"Over the 40-word budget (cannot survive in one chunk under ANY "
      f"strategy here): {too_long}")

print("\nWhere is each evidence span cut? (chunk IDs that overlap it)")
for ev in EVIDENCE:
    text = DOCS[ev["doc"]]
    a = text.index(ev["evidence"])
    b = a + len(ev["evidence"])
    for s in STRATEGIES:
        parts = [c["id"] for c in all_chunks[s]
                 if c["doc"] == ev["doc"] and c["start"] < b and c["end"] > a]
        print(f"  {ev['id']:<22}{LABEL[s]:<20}{parts}")

print("\n=== 3. Boundary tests ===")
from task2_chunks import windows
print("empty text, windows       :", windows(""))
print("empty text, sentence      :", sentence_chunks(""))
short = "Short rule. One exception."
print("short doc (<budget)       :", sentence_chunks(short),
      "->", len(sentence_chunks(short)), "chunk")
try:
    windows("a b c", 5, 5)
except ValueError as e:
    print("invalid overlap (5,5)     : ValueError:", e)
long_doc = DOCS["it_help"]
long_sentence = max(re.split(r"(?<=[.!?])\s+", long_doc),
                    key=lambda s: len(s.split()))
spans = sentence_chunks(long_sentence, 40)
print(f"sentence of {len(long_sentence.split())} words (> budget 40) "
      f"-> fallback windows:")
for a, b in spans:
    print(f"   chars {a}-{b}: {len(long_sentence[a:b].split())} words, "
          f"starts {long_sentence[a:b].split()[0]!r}, "
          f"ends {long_sentence[a:b].split()[-1]!r}")

print("\n=== 4. Where sentence splitting fails (abbreviations) ===")
doc = DOCS["assessment"]
cuts = [m.end() for m in re.finditer(r"[.!?]\s+", doc)]
pieces = [doc[a:b].strip() for a, b in zip([0] + cuts, cuts + [len(doc)])]
for p in pieces:
    if p.split()[-1] in {"e.g.", "Dr."} or p.startswith(("a previous", "Khan")):
        print("  fragment:", repr(p[:70] + ("..." if len(p) > 70 else "")))
