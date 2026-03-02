""" def occupied(yes, tod):
    res = 0
    list(yes)
    list(tod)
    for i in range(max(len(yes), len(tod))):
        if yes[i] == "c" and yes[i] == tod[i]:
            res +=1
    print(res)
occupied("ccc..", "ccc..") """

""" 
def langfind(phrase):
    numt = 0
    nums = 0
    phrase = list(phrase)
    for i in range(len(phrase)):
        if phrase[i] == "t" or phrase[i] == "T":
            numt += 1
        elif phrase[i] == "s" or phrase[i] == "S":
            nums += 1
    if nums > numt:
        print("french")
    elif numt > nums:
        print("english")
    elif nums == numt:
        print("french")
langfind("3Lorsque j'avais six ans j'ai vu, une fois,une magnifique image,dans un livre") """

def honifind(string):
    honiblock = []
    string = list(string)
    for i in range(len(string)):
        if i == "H":
            honiblock.append(i)
        elif i == "O":
            honiblock.append(i)
        elif i == "N":
            honiblock.append(i)
        elif i == "I":
            honiblock.append(i)
    honiblock = str(honiblock)
    res = honiblock.count("HONI")
    print(res)
honifind("PROHODNIHODNIK")