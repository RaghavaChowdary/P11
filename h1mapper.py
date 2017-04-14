f = open("sampleH1.txt","r")  # open file, read-only raw data
o = open("h1mapper_output.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("\t") 
    #print data
    print len(data)
    if len(data) == 11:
        Serial_Number, CASE_STATUS, EMPLOYER_NAME, SOC_NAME, JOB_TITLE, FULL_TIME_POSITION, PREVAILING_WAGE, YEAR, WORKSITE, lon, lat = data
        print "{0}\t{1}".format(CASE_STATUS, EMPLOYER_NAME)
        o.write("{0}\t{1}\n".format(CASE_STATUS, EMPLOYER_NAME))
f.close()
o.close()
n = open("h1mapper_output.txt","r")  # open file, read-only
s = open("h1map_sorted.txt", "w") # open file, write
lines = n.readlines()
lines.sort()
print(lines)
for line in lines:
	s.write(line)
n.close()
s.close()