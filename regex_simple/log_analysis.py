#log analysis
#Task: find 404 message on 22 Dec 2017. in logfile logs.txt

import re

#Open the file
    # read line, 
    # look for pattern
    #print
#"192168.4.163 - - [22/Dec/2017:22:32:32 +0300] "GET /oDZI69nQ.do HTTP/1.1" 404 503 "-" "w3af.org""

fd = open("logs.txt")

date_regex = r"\d\d.Dec.2017.*404"
for line in fd.readlines():
    if re.search(date_regex, line) is not None:
        print(line)
