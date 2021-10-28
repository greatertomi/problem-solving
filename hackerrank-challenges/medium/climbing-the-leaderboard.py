# Problem Link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


# My solution. But there is a better solution
def climbingTheLeaderboard(scores, alice):
    minNum = min(scores)
    maxNum = max(scores)
    scores = sorted(scores, reverse=True)
    ranks = []
    currentRank = 1
    aliceRanks = []
    for i in range(len(scores)):
        if scores[i] == maxNum:
            ranks.append((currentRank, scores[i]))
        elif scores[i] < scores[i-1]:
            currentRank += 1
            ranks.append((currentRank, scores[i]))
        else:
            ranks.append((currentRank, scores[i]))
    print('ranks', ranks)
    print('alice', alice)

    for i in range(len(alice)):
        if alice[i] < minNum:
            aliceRanks.append(currentRank + 1)
        elif alice[i] >= maxNum:
            aliceRanks.append(1)
        elif alice[i] == minNum:
            aliceRanks.append(currentRank)
        else:
            for k in range(len(ranks)):
                if alice[i] >= ranks[k][1]:
                    aliceRanks.append(ranks[k][0])
                    break
    print(aliceRanks)


scores1 = [100, 100, 50, 40, 40, 20, 10]
alice1 = [5, 25, 50, 120]

scores2 = [100, 90, 90, 80, 75, 60]
alice2 = [50, 65, 77, 90, 102]
climbingTheLeaderboard(scores2, alice2)

