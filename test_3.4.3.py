counter = summath = sumphisic = sumrusian = 0
ouf = open("outfile.txt", "w")
with open("infile.txt") as inf:
    for line in inf:
        # if line != "EOF":
        [sname, smath, sphisic, srusian] = line.split(";")
        aver = (int(smath) + int(sphisic) + int(srusian)) / 3
        ouf.write(str(aver) + "\n")
        counter += 1
        summath += int(smath)
        sumphisic += int(sphisic)
        sumrusian += int(srusian)

    ouf.write(str(summath/counter) + " ")
    ouf.write(str(sumphisic/counter) + " ")
    ouf.write(str(sumrusian/counter))


ouf.close()
