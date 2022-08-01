import os
import argparse
from util import utils

def arguments():
 parser = argparse.ArgumentParser(description = utils.banner_show())
 parser.add_argument('-p', '--path', action = 'store', dest = 'path',default='txt',required = True, help = 'Please pass first argv --path name_rdirectory')
 args = parser.parse_args()
 return args.path

def search_backups():
 path = arguments()
 utils.list_all(path)

def main():
 try:
  search_backups()
 except Exception as e:
  print(" log error : "+str(e))
  exit(0)

if __name__=="__main__":
 main()
