import os
import subprocess
import shlex
import argparse

# This code takes as an argument the definition name and creates a txt file with the list of locations on SamWeb 
# Beware: if the definition contains many many files, this simple hack is going to take a long time to run


# Take definiton name as input
parser = argparse.ArgumentParser()
parser.add_argument("path_to_directory"   , nargs='?', default = '/pnfs/uboone/data/uboone/reconstructed/prod_v08_00_00_01/data_bnb_reco1_mcc9/bnb_G1/00/01/75/57/', type = str, help="insert fileName")
parser.add_argument("file_name"   , nargs='?', default = 'PhysicsRun-2018_7_6_1_31_25-0017557-00174_20180715T184921_bnb_3_20181207T044618_optfilter_20181224T115826_reco1_postwcct_postdl_20181224T120052.root', type = str, help="insert fileName")

args = parser.parse_args()
path_to_directory = args.path_to_directory
file_name         = args.file_name


# Create list of files by redirecting the samweb commant output to an output file.
command = "cat "+path_to_directory+"/\".(get)("+file_name+")(locality)\""
command = shlex.split(command)
#print command
print 
print "|------------------------------------------------------|"
print "| LEGEND                                               |"
print "| ONLINE or ONLINE_AND_NEARLINE: the file is prestaged |"
print "| NEARLINE: the file is NOT prestaged, only on tape    |"
print "|------------------------------------------------------|"
print
print "And this is what happens for file ", file_name
magick_call = subprocess.Popen(command, stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
dimensions,error = magick_call.communicate()
print dimensions



