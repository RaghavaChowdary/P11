# P11
MapReduce Project
This MapReduce Project is analysis on H1-B visas in the United States. We are completed two MapReduce problems on this data.
MapReduceProblem1: how many H1-B visa are accepted or withdrawn or denied throughout the year 2016.
Input: sample input to the Mapper function is listed below.
Serial_Number	CASE_STATUS	EMPLOYER_NAME	SOC_NAME	JOB_TITLE	FULL_TIME_POSITION	PREVAILING_WAGE	YEAR	WORKSITE	lon	lat
1	CERTIFIED-WITHDRAWN	UNIVERSITY OF MICHIGAN	BIOCHEMISTS AND BIOPHYSICISTS	POSTDOCTORAL RESEARCH FELLOW	N	36067	2016	"ANN ARBOR, MICHIGAN"	-83.7430378	42.2808256
The MApper function takes that input from dataset and produce the intermediate key-vaues pairs like (Case_Status,Year) and these intermediate key -value pairs also sorted my mapper function.
The output of the Mapperfunction is mentioned in the following line.
CASE_STATUS	YEAR
CERTIFIED-WITHDRAWN	2016
CERTIFIED-WITHDRAWN	2016
CERTIFIED-WITHDRAWN	2016
CERTIFIED-WITHDRAWN	2016
WITHDRAWN	2016
DENIED	2016
CERTIFIED	2016
The reducer function takes the Input from the mapper function and reduce the values.The output of the reduce function is:
CASE_STATUS	Total
CERTIFIED	8858
CERTIFIED-WITHDRAWN	776
DENIED	414
WITHDRAWN	434

MapReduceProblem2: Which employer H1-B visas are accepted throughout the year 2016.
The input of second mapper function is laso same as the mapper function. In this mapreduce problem we are going to find the which employer file has been certified. This Mapper function generates the intermediate key-value pairs are (Employer_Name, Case_Status) and these values are sorted by Mapperfunction it self.
The mapper output of this function is:
CASE_STATUS	EMPLOYER_NAME
CERTIFIED	"1 HOTEL SOUTH BEACH, INC."
CERTIFIED	"1-800-FLOWERS.COM, INC."
CERTIFIED	"10X GENOMICS, INC."
CERTIFIED	"180LA, LLC"
CERTIFIED	"180LA, LLC"
CERTIFIED	"2233 PARADISE ROAD, LLC"
CERTIFIED	"22ND CENTURY 
The reducer function takes this and calucate values like which employeer case has been certified. The output of the reducer function is:
EMPLOYER_NAME	Total
"1 HOTEL SOUTH BEACH, INC."	1
"1-800-FLOWERS.COM, INC."	1
"10X GENOMICS, INC."	1
"180LA, LLC"	2
"2233 PARADISE ROAD, LLC"	1
"22ND CENTURY TECHNOLOGIES, INC."	1
"23ANDME, INC."	1
"24X7SYSTEMS, INC."	1
"3.1 PHILLIP LIM, LLC"	1
"33RD STRIKE GROUP, LLC"	3
"360 IT PROFESSIONALS, INC."	1
"360TRAINING.COM, INC."	2
"3I INFOTECH, INC."	4

We are using Python Language for this MapReduce problems. The following commands are used to execute the python files python shell.
If we are using python then we have to create file as filename.py
if you have python version on your local machiene. it easy to execute those files.
The following commands are  useful to executing the python shell.
 step1: Just right click on the file and choose the 'edit with idle'
 step2: it is popup two windows 
 one is where you can edit the code and the second one is used to execute the python files.
Step3: The following command is used to execute the python files.
Command: execfile(‘filename.py’) 
Graphical Representation Results below.
MR1GRAPH: we use bargraph 



