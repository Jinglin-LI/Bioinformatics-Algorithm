'''
DNA Alignment
Smith-Waterman Exercises (Local Alignments)

1. Two random sequences must be provided to the students.
2. A standard scoring system needs to be shown to the students. Example: +2 for a match, -1 for a mismatch, -2 for a gap.
'''
# Python 2.7

class interface(object):
    def sequenceAlign(self):
        pass
    def getScore(self):
        pass
    def getSign(self):
        pass
    
DNA = {'G': { 'G':2, 'C':-1, 'A':-1, 'T':-1 },
       'C': { 'G':-1, 'C':2, 'A':-1, 'T':-1 },
       'A': { 'G':-1, 'C':-1, 'A':2, 'T':-1 },
       'T': { 'G':-1, 'C':-1, 'A':-1, 'T':2 }}
gapPenalty = -2                                         # -2 for gap


class SmithWater(interface):
    def _init_(self):
        pass
    
    def sequenceAlign(seqA, seqB, simMatrix = DNA):
        numI = len(seqA) + 1
        numJ = len(seqB) + 1
        scoreMatrix = [[0] * numJ for x in range(numI)]             # Initiate scoreMatrix and routeMatrix, all 0
        routeMatrix = [[0] * numJ for x in range(numI)]
        
        maxN = 0                                                    # Find the max number in the matrix
        for i in range(1, numI):
            for j in range(1, numJ):                                     
                similarity = simMatrix[seqA[i - 1]][seqB[j - 1]]          # +2 for match, -1 for dismatch
                paths = [scoreMatrix[i - 1][j - 1] + similarity,
                         scoreMatrix[i - 1][j] + gapPenalty,
                         scoreMatrix[i][j - 1] + gapPenalty]
                best = max(paths)
                route = paths.index(best)
                scoreMatrix[i][j] = max(best, 0)

                if scoreMatrix[i][j] >= maxN:
                    maxN = scoreMatrix[i][j]                        # store the index of the max Number in the scoreMatrix
                    k = i
                    m = j
                routeMatrix[i][j] = route

        alignA = []
        alignB = []
        
        while (k > 0 or m > 0) and scoreMatrix[k][m] != 0:          # Traceback
            route = routeMatrix[k][m]
            if route == 0:                                          # that score comes from diagonal
                alignA.append(seqA[k - 1])
                alignB.append(seqB[m - 1])
                k -= 1
                m -= 1
            if route == 1:                                          # that score comes from horizon, gap in seqB
                alignA.append(seqA[k - 1])
                alignB.append('-')
                k -= 1
            if route == 2:                                          # that score comes from vertical, gap in seqA
                alignA.append('-')
                alignB.append(seqB[m - 1])
                m -= 1
        alignA.reverse()
        alignB.reverse()
        alignA = ''.join(alignA)
        alignB = ''.join(alignB)
        return alignA, alignB
    alignA, alignB = sequenceAlign('GGCTCAATCA', 'ACCTAAGG')


    def getScore(alignA, alignB, score = 0):
        for i in range(0, len(alignA)):
            if alignA[i] == alignB[i]:
                score = score + 2
            else:
                score = score - 2
        return score
    getAlignScore = getScore(alignA, alignB)


    def getSign(alignA, alignB, sign = []):         # print the '|' sign for alignment link
        for i in range(0, len(alignA)):
            if alignA[i] == alignB[i]:
                sign.append('|')
            else:
                sign.append(' ')
        sign = ''.join(sign)
        return sign
    getAlignSign = getSign(alignA, alignB)

 '''
    then the output of the sequence 'GGCTCAATCA', 'ACCTAAGG' and their score were shown
 '''
    print('The alignment is:')
    print(alignA) 
    print(getAlignSign)
    print(alignB)
    print("The score is:")
    print(getAlignScore)

        
