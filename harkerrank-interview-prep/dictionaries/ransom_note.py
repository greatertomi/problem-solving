def check_magazine(magazine, note):
    magazineArr = magazine.split()
    noteArr = note.split()
    status = "No"
    for word in noteArr:
        if word in magazineArr:
            status = "Yes"
            magazineArr.remove(word)
        else:
            status = "No"
            break

    return status


word1 = "ive got a lovely bunch of coconuts"
word2 = "ive got some coconuts"
print(check_magazine(word1, word2))
