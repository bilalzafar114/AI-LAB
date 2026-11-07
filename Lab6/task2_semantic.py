
import sys

from lab6_search import Retriever
from task2_chunks import make_chunks
from task2_docs import DOCS, EVIDENCE

STRATEGY = sys.argv[1] if len(sys.argv) > 1 else "sentence"
EV = {e["id"]: e for e in EVIDENCE}

QUERIES = [
    ("The website was down just before the deadline, what should I do?",
     "portal_outage"),
    ("My account is blocked after typing the wrong password too often",
     "lockout_exception"),
    ("I have a scholarship, do I still pay a penalty for paying late?",
     "scholarship_exception"),
]

records = make_chunks(DOCS, STRATEGY)
print(f"Strategy: {STRATEGY}; {len(records)} chunks from {len(DOCS)} docs")

backends = ["tfidf", "embedding"]
for backend in backends:
    print("\n" + "=" * 72)
    print("BACKEND:", backend)
    print("=" * 72)
    try:
        engine = Retriever(records, backend)
    except Exception as exc:
        print(f"SKIPPED ({type(exc).__name__}: {exc}).")
        print("Install sentence-transformers and rerun; no vectors are "
              "invented as a substitute.")
        continue
    hit_count = 0
    for query, ev_id in QUERIES:
        ev = EV[ev_id]
        hits = engine.search(query, k=3)
        print(f"\nQuery: {query}")
        print(f"Target evidence ({ev_id}, doc={ev['doc']}):")
        print("   ", ev["evidence"])
        if not hits:
            print("  No matching records (no shared vocabulary).")
        found_rank = None
        for rank, (r, score) in enumerate(hits, 1):
            full = r["doc"] == ev["doc"] and ev["evidence"] in r["text"]
            if full and found_rank is None:
                found_rank = rank
            print(f"  #{rank} {r['id']:<16} score={score:.3f} "
                  f"chars {r['start']}-{r['end']}  "
                  f"full evidence in chunk: {'YES' if full else 'no'}")
            print("     ", r["text"])
        hit_count += found_rank is not None
        print("  -> evidence retrieved at rank:", found_rank)
    print(f"\n{backend} summary: {hit_count}/{len(QUERIES)} queries had the "
          f"complete evidence in the top 3")
