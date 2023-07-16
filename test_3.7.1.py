numstr = int(input())
comanddict = dict()
for i in range(numstr):
    str = input().split(";")
    comd1, goal1, comd2, goal2 = str

    if comanddict.get(comd1) is None:
        comanddict[comd1] = [0] * 5
    if comanddict.get(comd2) is None:
        comanddict[comd2] = [0] * 5

    res1 = comanddict[comd1]
    res1[0] += 1
    res2 = comanddict[comd2]
    res2[0] += 1

    if goal1 == goal2:
        res1[2] += 1
        res2[2] += 1
    elif goal1 > goal2:
        res1[1] += 1
        res2[3] += 1
    elif goal2 > goal1:
        res2[1] += 1
        res1[3] += 1
for i in comanddict:
    comanddict[i][4] = comanddict[i][1] * 3 + comanddict[i][2] * 1        
    print(f'{i}:', *comanddict[i], end='\n')
