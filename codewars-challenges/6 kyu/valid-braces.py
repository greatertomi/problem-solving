# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python


def validBraces(string):
    store = []
    val_dict = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
    valid = True
    for char in string:
        if len(store) == 0:
            store.append(val_dict[char])
        else:
            last = store[-1]
            if val_dict[char] == -last:
                if val_dict[char] > last:
                    valid = False
                store.pop()
            elif val_dict[char] < 0 and val_dict[char] != -last:
                valid = False
                break
            else:
                store.append(val_dict[char])
    print(store)
    if len(store) > 0:
        return False
    return valid


string1 = '(((({{'
string2 = ')(}{]['
string3 = '())({}}{()][]['
string4 = '(){}[]'
string5 = '[({})]'
print(validBraces(string3))

