def rule_based(score, documents_complete, fee_paid, interview_score):
    return "Review" if (documents_complete and score >= 70 and fee_paid and interview_score >= 50) else "Hold"


cases = [
    {"name": "Pass All", "score": 85, "docs": True, "fee": True, "interview": 75, "expected": "Review", "reason": "All conditions met"},
    {"name": "Fail Fee", "score": 80, "docs": True, "fee": False, "interview": 60, "expected": "Hold", "reason": "Failed new condition 1: fee not paid"},
    {"name": "Fail Interview", "score": 90, "docs": True, "fee": True, "interview": 40, "expected": "Hold", "reason": "Failed new condition 2: interview < 50"},
    {"name": "Boundary", "score": 70, "docs": True, "fee": True, "interview": 50, "expected": "Review", "reason": "Meets exact threshold boundaries"}
]

print("Thresholds are synthetic lab assumptions.\n")
for c in cases:
    actual = rule_based(c["score"], c["docs"], c["fee"], c["interview"])
    print(f"Input: Score={c['score']}, Docs={c['docs']}, Fee={c['fee']}, Interview={c['interview']}")
    print(f"Expected: {c['expected']} | Actual: {actual}")
    print(f"Reason: {c['reason']}\n")