ouf = open("outfile.txt", "w")
with open("infile.txt") as inf:
    word_list = inf.read().lower().split()
word_dict = dict()
word_max = 0
for i in word_list:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] += 1   
        if word_max < word_dict[i]:
            word_max = word_dict[i]
for i in word_dict:
    if word_dict[i] == word_max:
        print(i, word_dict[i])
        print(word_dict.items() )          
        ouf.write(i)
        ouf.write(" ")
        ouf.write(str(word_dict[i]))
        


ouf.close()
