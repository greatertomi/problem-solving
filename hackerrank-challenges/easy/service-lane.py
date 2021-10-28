# Problem Link: https://www.hackerrank.com/challenges/service-lane/problem


def serviceLane(n, cases):
    results = []
    for case in cases:
        results.append(min(n[case[0]: case[1] + 1]))

    return results


lanes1 = [2, 3, 1, 2, 3, 2, 3, 3]
cases1 = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
print(serviceLane(lanes1, cases1))
