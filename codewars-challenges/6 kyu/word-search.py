# Problem Link: https://www.codewars.com/kata/5f05e334a0a6950011e72a3a


def wordSearch(target, words):
    length = len(words)//10
    g1 = words[0:length]
    g2 = words[length: length*2]
    g3 = words[length*2: length*3]
    g4 = words[length*3: length*4]
    g5 = words[length*4: length*5]
    g6 = words[length*5: length*6]
    g7 = words[length*6: length*7]
    g8 = words[length*7: length*8]
    g9 = words[length*8: length*9]
    g10 = words[length*9: length*10]
    print(g1)
    try:
        if target in g1:
            return g1.index(target)
        elif target in g2:
            return g2.index(target) + length
        elif target in g3:
            return g3.index(target) + length * 2
        elif target in g4:
            return g4.index(target) + length * 3
        elif target in g5:
            return g5.index(target) + length * 4
        elif target in g6:
            return g6.index(target) + length * 5
        elif target in g7:
            return g7.index(target) + length * 6
        elif target in g8:
            return g8.index(target) + length * 7
        elif target in g9:
            return g9.index(target) + length * 8
        else:
            return g10.index(target) + length * 9
    except ValueError:
        pass


words1 = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars']
target1 = 'codewars'

words2 = ['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj']
target2 = 'akC'

print(wordSearch(target1, words1))
