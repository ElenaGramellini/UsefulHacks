import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fclName"     , nargs='?', default = "puppa1.root", type = str, help="insert first  FileName")
args     = parser.parse_args()
fclName  = args.fclName



paths = os.environ['FHICL_FILE_PATH'].split(":")

for p in paths:
    if os.path.isfile(p+"/"+fclName):
        print p+"/"+fclName


