#Backtracking algorithm
#Game playing
# A simple Python3 program to find maximum score that maximizing player can get

import math
def minimax (curDepth, nodeIndex,maxTurn,scores,targetDepth):
# base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,False, scores, targetDepth),minimax(curDepth + 1, nodeIndex * 2 + 1,False, scores, targetDepth))
    else:
       return min(minimax(curDepth + 1, nodeIndex * 2,True, scores, targetDepth),minimax(curDepth + 1, nodeIndex * 2 + 1,True, scores, targetDepth))
# Driver code
scores = [23, 25, 7, 9, 12, 15, 33, 13]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))