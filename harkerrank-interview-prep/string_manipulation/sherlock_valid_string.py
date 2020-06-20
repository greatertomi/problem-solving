from collections import Counter

string = "abcdefghhgfedecba"
string_dict = {}
for char in string:
    if char in string_dict:
        string_dict[char] += 1
    else:
        string_dict[char] = 1
print(string_dict)
dict_set = set(string_dict.values())
if len(dict_set) == 1:
    print("Yes")
else:
    dict_values = string_dict.values()
    nums = Counter(dict_values)
    print(nums)
    if len(nums) > 2:
        print('No')


