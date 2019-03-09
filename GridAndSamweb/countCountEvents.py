
# Useful script when you fuck up the samweb counting and you need to do it by hand
# from a count events file

# Open the file with read only permit
f = open('countEvents.txt')
line = f.readline()
totalEvents = 0
while line:
    w = line.split()
    secondlastWord = w[len(w)-2]
    print secondlastWord
    totalEvents += int(secondlastWord)
    line = f.readline()

print "Total Number of Events ", totalEvents
f.close()
