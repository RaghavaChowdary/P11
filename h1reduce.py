sorted = open("h1map_sorted.txt","r")   
results = open("reducer_output.txt", "w")   

CASE_STATUS = 0        
YEAR = None    
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisYear, thisCaseStatus = datalist  # read into variables
    if YEAR and YEAR != thisYear:        
        results.write("{0}\t{1}\n".format(YEAR, CASE_STATUS))
        YEAR = thisYear;
        CASE_STATUS = 0

    YEAR = thisYear            
    CASE_STATUS += 1   

if YEAR != None: 
    results.write("{0}\t{1}\n".format(YEAR, CASE_STATUS))

sorted.close() 
results.close() 
