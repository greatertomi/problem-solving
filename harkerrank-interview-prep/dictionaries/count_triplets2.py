from collections import defaultdict

arr = [1, 3, 9, 9, 27, 81]
r = 3
dict1 = defaultdict(int)
dict2 = defaultdict(int)
count = 0
for k in arr:
    count += dict2[k]
    dict2[k * r] += dict1[k]
    dict1[k * r] += 1
print(count)
