# get data of earthquakes from file, make new file with places,dates,magnitude

# open and read file
earthquakeFile = open('Lab 1/earthquake.txt', "r")
earthquakes = earthquakeFile.read()
earthquakeFile.close()
quakeStats = earthquakes.splitlines() #split files by line

# split the magnitude, dates, and places of the earthquakes into different arrays
magnitudeArr, dateArr, placeArr = [], [], []
for i in quakeStats:
    temp = i.split()
    magnitudeArr.append(temp[0])
    dateArr.append(temp[1])
    placeArr.append(temp[len(temp) - 1])
# make an array for the output that stores each unique name with all the dates
# and magnitudes of the earthquakes that happened
outputArr = []
counter = 0
outputArr.append([placeArr.pop(0)])
outputArr[len(outputArr) - 1].append("[" + dateArr[0] + "," + magnitudeArr[0] + "]")
dateArr.pop(0)
magnitudeArr.pop(0)
while len(placeArr) > 0:
    notIn = True
    for i in outputArr:
        if placeArr[0] in i:
            notIn = False
    if notIn:
        outputArr.append([placeArr.pop(0)])
        outputArr[len(outputArr) - 1].append("[" + dateArr[0] + "," + magnitudeArr[0] + "]")
        dateArr.pop(0)
        magnitudeArr.pop(0)
    else:
        for j in outputArr:
            if placeArr[0] in j:
                j.append("[" + dateArr[0] + ", " + magnitudeArr[0] + "]")
                placeArr.pop(0)
                dateArr.pop(0)
                magnitudeArr.pop(0)
outputFile = open('Lab 1/earthquakefmt.txt', "w")
for i in outputArr:
    outputFile.write(str(i).replace("'", '') + "\n\n")
outputFile.close()
