# Better solution
def climbingTheLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    print(scores)
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while n > index and i >= scores[index]:
            index += 1
        rank_list.append(n + 1 - index)
    return rank_list


scores1 = [100, 100, 50, 40, 40, 20, 10]
alice1 = [5, 25, 50, 120]

scores2 = [100, 90, 90, 80, 75, 60]
alice2 = [50, 65, 77, 90, 102]
print(climbingTheLeaderboard(scores1, alice1))
