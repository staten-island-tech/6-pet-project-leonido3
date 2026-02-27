def occupied(yes, tod):
    res = 0
    list(yes)
    list(tod)
    for i in range(max(len(yes), len(tod))):
        if yes[i] == "c" and yes[i] == tod[i]:
            res +=1
    print(res)
occupied("ccc..", "ccc..")