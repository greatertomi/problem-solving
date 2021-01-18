# Problem Link: https://www.hackerrank.com/challenges/common-child/problem
# This is the longest subsequence problem. This https://www.youtube.com/watch?v=FWyANT-7iq8 helped.


def commonChild(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0]*(m+1) for z in range(n+1)]
    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[-1][-1]


print(commonChild('HARRY', 'SALLY'))
print(commonChild('AA', 'BB'))
print(commonChild('SHINCHAN', 'NOHARAAA'))
print(commonChild('ABCDEF', 'FBDAMN'))
