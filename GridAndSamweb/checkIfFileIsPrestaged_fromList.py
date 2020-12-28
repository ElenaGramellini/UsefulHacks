import os
import subprocess
import shlex
import argparse



def checkIfPrestaged(path_to_directory, file_name):
   #path_to_directory = "/pnfs/uboone/overlay/uboone/reconstructed/prod_v08_00_00_13/prodgenie_bnb_intrinsic_nue_uboone_overlay_mcc9.0/run3_reco2/"
   #file_name ="PhysicsRun-2017_10_27_17_19_2-0013697-00019_20190208T110950_ext_unbiased_3_gen_20190520T052249_eventweight_20190520T053022_g4_detsim_mix_r1a_r1b_postd_8a4531f2-88ae-43cf-afd5-171199a3d5f1.root"
   # Create list of files by redirecting the samweb commant output to an output file.
   path_to_directory+="/"
   print path_to_directory
   w = file_name.split("\n")
   command = "cat "+path_to_directory+"/\".(get)("+w[0]+")(locality)\""
   print command
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



def main():
   # Take definiton name as input
   parser = argparse.ArgumentParser()
   parser.add_argument("listFile"   , nargs='?', default = 'list', type = str, help="insert fileName")
   args = parser.parse_args()
   fileName = args.listFile

   with open(fileName) as fp:
      line = fp.readline()
      while line:
         file_name         = os.path.basename(line)
         path_to_directory = os.path.dirname (line)
         checkIfPrestaged( path_to_directory, file_name)
         line = fp.readline()
         raw_input()
main()
