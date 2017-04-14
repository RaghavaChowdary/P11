sorted = open("h1map_sorted.txt","r")     
results = open("reducer_output.txt", "w")   

CASE_STATUS = 0        
EMPLOYER_NAME = None    
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisCase, thisEmpoyer  = datalist  # read into variables
    if EMPLOYER_NAME and EMPLOYER_NAME != thisEmpoyer:        
        results.write("{0}\t{1}\n".format(EMPLOYER_NAME, CASE_STATUS))
        EMPLOYER_NAME = thisEmpoyer;
        CASE_STATUS = 0

    EMPLOYER_NAME = thisEmpoyer            
    CASE_STATUS += 1   

if EMPLOYER_NAME != None: 
    results.write("{0}\t{1}\n".format(EMPLOYER_NAME, CASE_STATUS))

sorted.close() 
results.close() 
