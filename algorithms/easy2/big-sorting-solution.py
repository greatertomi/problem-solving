n = int(input().strip())
unsorted = []
for i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
for i in sorted(unsorted, key=int):
    print(i)
