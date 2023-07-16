numstr = int(input())
comanddict = dict()
for i in range(numstr):
    str = input().split(";")
    comd1 = str[0]
    comd2 = str[2]
    goal1 = int(str[1])
    goal2 = int(str[3])

    if comanddict.get(comd1) is None:
        comanddict[comd1] = [0, 0, 0, 0, 0]
    if comanddict.get(comd2) is None:
        comanddict[comd2] = [0, 0, 0, 0, 0]

    res1 = comanddict[comd1]
    res1[0] += 1
    res2 = comanddict[comd2]
    res2[0] += 1

    if goal1 == goal2:
        res1[2] += 1
        res1[4] += 1  # Point
        res2[2] += 1
        res2[4] += 1  # Point
    elif goal1 > goal2:
        res1[1] += 1
        res1[4] += 3  # Point
        res2[3] += 1
    elif goal2 > goal1:
        res2[1] += 1
        res2[4] += 3  # Point
        res1[3] += 1
for i in comanddict:
     print(f'{i}:', *comanddict[i], end='\n')
