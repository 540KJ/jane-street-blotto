import random

TOTALNUM = 1000

# Finds n random numbers that sum up to total
def constrainedSumSamplePos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
    
# Finds standard's score when battling against toCompare
def hasStandardWon(standard, toCompare):
    wins = []
    losts = []
    consecutiveWins = 0
    consecutiveLoses = 0
    for i in range(10):
        if (consecutiveWins == 3):
            return sum(wins) + sum(range(i+1, 11))
        if (consecutiveLoses == 3):
            return sum(wins)
        if (standard[i] > toCompare[i]):
            consecutiveWins += 1
            consecutiveLoses = 0
            wins.append(i+1)
        elif (standard[i] < toCompare[i]):
            losts.append(i+1)
            consecutiveWins = 0
            consecutiveLoses += 1
        elif (standard[i] == toCompare[i]):
            consecutiveWins = 0
            consecutiveLoses = 0
    return sum(wins)

# Finds the most successful castle arrangement by battling each entry with all other entries
def findEfficientSolution():
    tentets = [[33, 33, 34, 0, 0, 0, 0, 0, 0, 0]]
    while (len(tentets) < TOTALNUM):
        tentets.append(constrainedSumSamplePos(10, 100))
    
    probabs = []
    
    for i in range(TOTALNUM):
        totalScores = 0
        for j in range(TOTALNUM):
            if (i != j):
                totalScores += hasStandardWon(tentets[i], tentets[j])
        probabs.append([tentets[i], totalScores / (TOTALNUM - 1)])

    probabs.sort(key=lambda x: x[1])
    return probabs[-1]

# Battles 100 'cream-of-the-crop' castle arrangements against each other
optimalSolutions = []

for i in range(100):
    optimalSolutions.append(findEfficientSolution())

optimalSolutions.sort(key=lambda x:x[1])
print(optimalSolutions[0])
print(optimalSolutions[-1])

tentets = 30*[[33, 33, 34, 0, 0, 0, 0, 0, 0, 0]]

for solution in optimalSolutions:
    tentets.append(solution[0])
    
probabs = []

for i in range(len(tentets)):
    totalScores = 0
    for j in range(len(tentets)):
        if (i != j):
            totalScores += hasStandardWon(tentets[i], tentets[j])
    probabs.append([tentets[i], totalScores / (len(tentets) - 1)])
    
probabs.sort(key=lambda x: x[1])
print(probabs[-10:])
