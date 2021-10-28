# Problem Link: https://www.hackerrank.com/challenges/queens-attack-2/problem


def queenAttack(n, k, qRow, qCol, obstacles):
    left = qCol - 1
    right = n - qCol
    up = n - qRow
    down = qRow - 1
    right_up = min(right, up)
    right_down = min(right, down)
    left_up = min(left, up)
    left_down = min(left, down)
    for obstacle in obstacles:
        if obstacle[1] == qCol:
            if obstacle[0] < qRow:
                down = min(down, qRow - 1 - obstacle[0])
            else:
                up = min(up, obstacle[0] - qRow - 1)
        elif obstacle[0] == qRow:
            if obstacle[1] < qCol:
                left = min(left, qCol - 1 - obstacle[1])
            else:
                right = min(right, obstacle[1] - qCol - 1)
        elif abs(obstacle[0] - qRow) == abs(obstacle[1] - qCol):
            if obstacle[1] > qCol:
                if obstacle[0] > qRow:
                    right_up = min(right_up, obstacle[1] - qCol - 1)
                else:
                    right_down = min(right_down, obstacle[1] - qCol - 1)
            else:
                if obstacle[0] > qRow:
                    left_up = min(left_up, qCol - 1 - obstacle[1])
                else:
                    left_down = min(left_down, qCol - 1 - obstacle[1])

    return left + right + up + down + left_up + left_down + right_up + right_down


n1 = 4
k1 = 0
rq1 = 4
cq1 = 4
obstacles1 = []

n2 = 5
k2 = 3
rq2 = 4
cq2 = 3
obstacles2 = [(5, 5), (4, 2), (2, 3)]

n3 = 1
k3 = 0
rq3 = 1
cq3 = 1
obstacles3 = []

print(queenAttack(n2, k2, rq2, cq2, obstacles2))
