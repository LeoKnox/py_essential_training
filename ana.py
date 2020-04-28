def isana(word, item):
    newword = word
    for l in word:
        if l in item:
            print(l)
            newword = item.replace(l,"")
    print(item)


list = ["code", "doce", "code"]
isana("one", "two")
