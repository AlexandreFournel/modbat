import sys
import re
import os
##debug
def main(file1,file2):
    if os.path.isfile(file1+".debug") and os.path.isfile(file2+".debug"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                debug=value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".debug")==False and os.path.isfile(file2+".debug")==False:
        error="- Do not exist -"
    else:
        debug=0

    ##info
    if os.path.isfile(file1+".info") and os.path.isfile(file2+".info"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                info=value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".info")==False and os.path.isfile(file2+".info")==False:
        error="- Do not exist -"
    else:
        info=0

    if os.path.isfile(file1+".error") and os.path.isfile(file2+".error"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                error=value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".error")==False and os.path.isfile(file2+".error")==False:
        error="- Do not exist -"
    else:
        error=0

    if os.path.isfile(file1+".warning") and os.path.isfile(file2+".warning"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                warning=value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".warning")==False and os.path.isfile(file2+".warning")==False:
        warning="Do not exist"
    else:
        warning=0

    if os.path.isfile(file1+".fine") and os.path.isfile(file2+".fine"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                fine=value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".fine")==False and os.path.isfile(file2+".fine")==False:
        error="- Do not exist -"
    else:
        fine=0

    if os.path.isfile(file1+".raw") and os.path.isfile(file2+".raw"):
        for line in open("2_gram/modbat/Ranking", "r"):
            if file1 in line and file2 in line:
                raw=value=float (int( re.sub(r"^([0-9]+)\.[0-9]+$", "\\1", line.split("__")[0][:-1].replace(".","")),10)/10)
    elif os.path.isfile(file1+".raw")==False and os.path.isfile(file2+".raw")==False:
        error="- Do not exist -"
    else:
        raw=0


    print (debug, info, fine, error, warning, raw)
    return