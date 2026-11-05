#Task 2 Adding leaf evaluation counter to both algorithms
#-----------------------
#1-Minimax
import math
leaf = 0
# Maximizing player can get
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaf
# Base case: targetDepth reached
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
# Driver code
scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
# Pad scores to make a complete binary tree
scores += [0] * (2**treeDepth - len(scores))
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))

print(f"Leafs evaluated-{leaf}")

#output
#The optimal value is: 5
#Leafs evaluated-8

#-------------------------------------------------------------------------------------------
#2-Alpha beta pruning

import math
leaf=0
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global leaf
    if depth == target:
        leaf+=1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth+1, index*2+i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth+1, index*2+i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))

print(f"Value:{alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf'))}")
print(f"leaf:{leaf}")

#output
#Value:5
#leaf:6

#==============================================================================
#Task3 Changing branch order

#1-Minimax 
import math
leaf = 0
# Maximizing player can get
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaf
# Base case: targetDepth reached
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
# Driver code
scores =[3 ,9,5,7,2,0,0,0]
treeDepth = math.ceil(math.log2(len(scores)))
# Pad scores to make a complete binary tree
scores += [0] * (2**treeDepth - len(scores))
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))

print(f"Leafs evaluated-{leaf}")


#output
#The optimal value is: 7
#Leafs evaluated-8


#2-Alpha beta pruning
import math
leaf=0
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global leaf
    if depth == target:
        leaf+=1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth+1, index*2+i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth+1, index*2+i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
scores =[3 ,9,5,7,2,0,0,0]
depth = int(math.log2(len(scores)))

print(f"Value:{alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf'))}")
print(f"leaf:{leaf}")

#output
#Value:7
#leaf:6
