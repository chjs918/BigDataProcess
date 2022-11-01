import sys
from datetime import datetime, date

def dayOfWeek(date):
	days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
	day = date.weekday()
	return days[day]

inF = open(sys.argv[1], "rt")
outF = open(sys.argv[2], "wt")

uberV = dict()
uberT = dict()
for i in inF:
	infoList = i.split(",")
	month = infoList[1].split("/")[0]
	day = infoList[1].split("/")[1]
	year = infoList[1].split("/")[2]
	#print(dayOfWeek(date(int(year), int(month), int(day))))	
	#infoList[2]
	toDay = date(int(year), int(month), int(day))
	region = infoList[0]
	vehicles = int(infoList[2])
	trips = int(infoList[3])
	#print("%s,%s %s,%s" % (region, dayOfWeek(toDay), vehicles, trips))
	reDay = region + "," + dayOfWeek(toDay)
	if reDay not in uberV:
		uberV[reDay] = vehicles
		uberT[reDay] = trips
	else:
		uberV[reDay] += vehicles
		uberT[reDay] += trips

for i in uberV:
	outF.write(i + " ")
	outF.write(str(uberV[i]) + ",")
	outF.write(str(uberT[i]) + "\n")

inF.close()
outF.close()
