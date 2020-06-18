from collections import defaultdict
def freqQuery(queries):
    array = []
    for query in queries:
        if query[0] == 1:
            array.append(query[1])
        elif query[0] == 2:
            if query[1] in array:
                array.remove(query[1])
        elif query[0] == 3:
            arr_dict = {}
            value_arr = []
            for i in array:
                if i in arr_dict:
                    arr_dict[i] += 1
                else:
                    arr_dict[i] = 1
            for i in arr_dict:
                value_arr.append(arr_dict[i])
            if query[1] in value_arr:
                print("1")
            else:
                print("0")


values = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
values2 = [(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]
values3 = [(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)]
freqQuery(values3)
