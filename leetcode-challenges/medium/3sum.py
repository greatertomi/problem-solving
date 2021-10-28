# Problem Link: https://leetcode.com/problems/3sum

def threeSum(nums):
    Set = set()
    nums.sort()

    n = len(nums)
    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                Set.add((nums[i], nums[j], nums[k]))
                k = k - 1
                j = j + 1

            elif total > 0:
                k = k - 1

            else:
                j = j + 1

    return [list(i) for i in Set]


numsArr1 = [-1, 0, 1, 2, -1, -4]
numsArr2 = [0]
numsArr3 = [1, 2, 3]
print(threeSum(numsArr1))
