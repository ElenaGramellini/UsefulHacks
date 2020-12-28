import os
import subprocess
import shlex
import argparse

# This code takes as an argument the definition name and creates a txt file with the list of locations on SamWeb 
# Beware: if the definition contains many many files, this simple hack is going to take a long time to run


# Take definiton name as input
parser = argparse.ArgumentParser()
parser.add_argument("fileListName"   , nargs='?', default = 'MCC8.20-CCpi0_bnb', type = str, help="insert fileName")

args = parser.parse_args()
fileListName     = args.fileListName


# Now we have created a file with all the names of the files
# But the location is still missing!
# Let's find it!

# Open txt files: both the (now) input and the output    
listName    = fileListName
outFileName = fileListName[:-5]+"_withPath.list"
fileHandler = open (listName, "r")
outFile = open(outFileName,"w") 


# Get list of all lines in file
listOfLines = fileHandler.readlines()


for fileRoot in listOfLines:
    #Find them!
    command = "samweb locate-file "+ fileRoot + "-e uboone"
    command = shlex.split(command)
    magick_call = subprocess.Popen(command, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dimensions,error = magick_call.communicate()
    print fileRoot, dimensions
    # Pad them in the correct form
    path =  (dimensions.split(":"))[1].split("(")[0]
    outFile.write( path+"/"+fileRoot)



fileHandler.close()

