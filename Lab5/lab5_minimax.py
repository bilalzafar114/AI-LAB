import math
leaf = 0
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaf
    if curDepth == targetDepth:
        leaf += 1
        return scores[nodeIndex]
    if maxTurn:
        return max(
minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
)
    else:
        return min(
minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
)

scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))

scores += [0] * (2**treeDepth - len(scores))
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))

print(f"Leafs evaluated-{leaf}")