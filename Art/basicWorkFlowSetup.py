import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("workName"     , nargs='?', default = "analysis", type = str, help="insert name of the analysis")

args       = parser.parse_args()
workName   = args.workName


command1 = "mkdir -p $MRB_TOP/"+workName+"/fcl"
command2 = "mkdir -p $MRB_TOP/"+workName+"/macro"
command3 = "mkdir -p $MRB_TOP/"+workName+"/xml"


print command1
print command2
print command3



os.system(command1)
os.system(command2)
os.system(command3)
