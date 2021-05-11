import random

# 推計統計学とシュミレーション
def flip(numFlips):
    """
    numFlipsは正の整数
    """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T'))=='H':
            heads += 1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    """
    numFlipsPerTrial、numTrialsは正の整数
    """
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean

print(flipSim(100, 10000))
print(flipSim(100, 10000))