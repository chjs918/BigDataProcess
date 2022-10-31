import sys

inF = open(sys.argv[1], "rt")
outF = open(sys.argv[2], "wt")

greCount = dict()
for i in inF:
	splitByColon = i.split("::")
	#print(splitByColon)
	genreList = splitByColon[2].split("|")
	for g in genreList:
		if g.strip() not in greCount:
	   		greCount[g.strip()] = 1
		else:
			greCount[g.strip()] += 1

for key, value in greCount.items():
	#print(key, value)
	outF.write(key + " ")
	outF.write(str(value) + "\n")

