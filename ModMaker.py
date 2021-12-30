import json
import os
import sys

global exportlist
exportlist = []
os.makedirs("export", exist_ok=True)

MUTATIONINPUT = sys.argv[1]
EXPORTFOLDER = "export/" + sys.argv[2]


READINPUT = open(MUTATIONINPUT, mode="r")
WRITEOUTPUT = open(EXPORTFOLDER, mode='w+')


JSONINPUT = json.load(READINPUT)

for x in JSONINPUT:
    currentthresh = x.get("threshreq")
    thresholdtrue = x.get("threshold")
    if currentthresh != None or thresholdtrue != None:
        threshentry = {}
        threshentry["type"] = x.get("type")
        threshentry["id"] = x.get("id")
        threshentry["copy-from"] = x.get("id")
        threshentry["threshreq"] = []
        threshentry["threshold"] = False
        exportlist.append(threshentry)



if len(exportlist) == 0:
    print("No threshold mutations detected in [0]".format(MUTATIONINPUT))
else:
    json.dump(exportlist, WRITEOUTPUT, indent = 4)
        

WRITEOUTPUT.close()
READINPUT.close()

