def longest_common_subsequence(test_A1, test_B1):
    count = 0
    for i in test_A1:
        if i in test_B1:
            count += 1
            pos = test_B1.index(i)
            test_B1 = test_B1[:pos] + test_B1[pos+1:]
    print(count)


# test1 = "WHOWEEKLY"
# test2 = "HOWONLY"
test1 = "CATSINSPACETWO"
test2 = "DOGSPACEWHO"
longest_common_subsequence(test1, test2)
