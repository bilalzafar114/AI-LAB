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