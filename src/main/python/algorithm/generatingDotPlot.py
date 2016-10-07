# Python 3.5

import numpy as np
import matplotlib.pyplot as plt

##generates a score matrix to see which characters in seq1 are similar to seq2
def compareTwoSeq(seq1, seq2):
    lengthSeq1 = len(seq1)
    lengthSeq2 = len(seq2)

    scoreMatrix = [[0] * lengthSeq2 for x in range(lengthSeq1)]

    for i in range(lengthSeq1):
        for j in range(lengthSeq2):
            if(seq1[i] == seq2[j]):
                scoreMatrix[i][j] = 1

    return scoreMatrix

##converts the score matrix from compareTwoSeq into another matrix for plotting
def generatePlotArray(scoreMatrix):
    lengthSeq1 = len(scoreMatrix)
    lengthSeq2 = len(scoreMatrix[0])

    graphMatrix = [[0] * lengthSeq2 for x in range(lengthSeq1)]

    for i in range(lengthSeq1):
        for j in range(lengthSeq2):
            if(scoreMatrix[i][j] == 1):
                graphMatrix[i][j] = lengthSeq2-j ##to display seq2 in a top to bottom manner
            elif(scoreMatrix[i][j] == 0):
                graphMatrix[i][j] = float('nan') ##this is to remove the '0' values
                
    return graphMatrix

##this is to help generate a float range array for visualisation purposes later
def generateFloatRange(start, end):
    x = list()
    x.append(start)

    while(x[len(x) - 1] < end):
        x.append(x[len(x) - 1] + 1)

    return x

##example sequence
##seq1 = 'GGCTCAATCA'
##seq2 = 'GGCTCAATCA'

seq1 = input('seq1: ')
seq2 = input('seq2: ')

length1 = len(seq1)
length2 = len(seq2)

scoreMatrix = compareTwoSeq(seq1, seq2)
graphMatrix = generatePlotArray(scoreMatrix)

generateXDotted = generateFloatRange(-0.5, length1 - 0.5)
generateYDotted = generateFloatRange(0.5, length2 - 0.5)

################## plotting #####################
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xticks(generateXDotted, minor = True)
ax.set_yticks(generateYDotted, minor = True)
ax.xaxis.grid(True, which = 'minor')
ax.yaxis.grid(True, which = 'minor')

ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
ax.plot(graphMatrix, 'o', markersize = 15, color = 'black')

##to replace numeric values with the sequence 
plt.xticks(range(0, length1), seq1)
plt.yticks(list(reversed(range(1, length2 + 1))), seq2)

plt.xlabel('Sequence 1')
plt.ylabel('Sequence 2')

plt.xlim([-0.5, length1 - 0.5])
plt.ylim([0.5, length2 + 0.5])

plt.show()

