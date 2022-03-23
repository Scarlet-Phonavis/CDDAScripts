#Catapult please, why have a seperate mods folder if you don't understand the concept of overwriting default mods? What sane person just changes the ID, think of the dependents!

import glob
import os 
import json
import sys
import shutil

DEBUGPRINT = 0




#FileInputList = glob.glob("**/*", root_dir="Input\\", recursive=True)


print("Reading files in mod_repo")
ModRepoList = os.listdir("mod_repo\\")
IDLIST = []


for ModFolder in ModRepoList:
	CurrentPath = str("mod_repo\\" + ModFolder + "\\")
	if os.path.isdir(CurrentPath) == False:
		continue
	if os.path.exists(str(CurrentPath + "modinfo.json")) == False:
		continue
	ModInfoReader = open(str(CurrentPath + "modinfo.json"), mode="r")
	JSONMODINFO = json.load(ModInfoReader)
	ModInfoReader.close()
	if DEBUGPRINT:
		print(type(JSONMODINFO))
	if type(JSONMODINFO) == dict:
		JSONMODINFOSTRING = JSONMODINFO 
		JSONMODINFO = []
		JSONMODINFO.append(JSONMODINFOSTRING)
	for x in JSONMODINFO:
		if x.get("type") == "MOD_INFO":
			MODID = x.get("id")
			MODNAME = x.get("name")
			if type(MODID) != str:
				MODID = x.get("ident")
			if DEBUGPRINT:
				print(type(x))
	IDLIST.append(MODID)

	












#For if you just want a list, I guess
#REMOVALIDREADER = open("removeids.txt", mode="r")
#IDLIST = REMOVALIDREADER.readlines()
#REMOVALIDREADER.close()





print("Reading folders in current\\data\\mods\\...")
ModFolderList = os.listdir("current\\data\\mods\\")

for ModFolder in ModFolderList:
	modinfoprebuilt = 0
	patchcount = 0
	CurrentPath = str("current\\data\\mods\\" + ModFolder + "\\")
	if os.path.isdir(CurrentPath) == False:
		continue
	OutputPath = str("Output\\" + ModFolder + "\\")
	ModInfoReader = open(str(CurrentPath + "modinfo.json"), mode="r")
	JSONMODINFO = json.load(ModInfoReader)
	ModInfoReader.close()
	if DEBUGPRINT:
		print(type(JSONMODINFO))
	if type(JSONMODINFO) == dict:
		JSONMODINFOSTRING = JSONMODINFO 
		JSONMODINFO = []
		JSONMODINFO.append(JSONMODINFOSTRING)
	for x in JSONMODINFO:
		if x.get("type") == "MOD_INFO":
			MODID = x.get("id")
			MODNAME = x.get("name")
			if type(MODID) != str:
				MODID = x.get("ident")
			if DEBUGPRINT:
				print(type(x))
	if MODID == "dda":
		continue
	for z in IDLIST:
		if DEBUGPRINT:
			print("Comparing IDLIST {} and MODID {}".format(z.strip(), MODID))
		if z.strip() == MODID:
			shutil.rmtree(CurrentPath, ignore_errors=True)
			print("Deleting {}, mod id {}, mod name {}".format(CurrentPath, MODID, MODNAME))
			

	
