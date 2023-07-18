dictstr = []
textstr = []
wordInDict = int(input())
for i in range(wordInDict):
    dictstr += [input().lower()]
wordInext = int(input())
for i in range(wordInext):
    textstr += input().lower().split()
textstr = set(textstr)
differ = textstr - set(dictstr)
print(* differ, sep = "\n")