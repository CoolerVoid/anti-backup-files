import re
import os

def banner_show():
    print("Anti-backup-files v0.1 \n by github.com/CoolerVoid\n\n")
    print("\tUsage:\n\tpython3 anti-backup-files.py --path repository_name\n\n")

def show_results(bak,doc,ignore):
 print("\nList of backup files:\n")
 for path in bak:
  print(path)
 print("\nList of documents files:\n")
 for path in doc:
  print(path)
 print("\nList of .gitignore files:\n")
 for path in ignore:
  print(path)
 print("\nScore total\n")
 print("Total of possible backup files: %d" % len(bak))
 print("Total of possible leak of document files: %d" % len(doc))
 print("Total of .gitignore files: %d \n" % len(ignore))
         
# recursive dir walk to search backup files n soon
def list_all(directory):
 detect_backup={".dump",".rar",".7z",".zip",".gz",".backup",".bak",".tar","dmp",".tmp~",
                ".old",".swp","conf~",".sql",".db",".tmp",".cache",".log",".velho"}
 detect_documents={".pdf",".xls",".ppt",".odp",".docx",".csv",".doc",".pptx",".dwg","dxf",".dbq"}
 ret_bak=[]
 ret_doc=[]
 ret_gitignore=[]

 for dirpath, dirnames, files in os.walk(directory):
  for name in files:
   if ".gitignore" in name:
    ret_gitignore.append(dirpath+name)
   for extension_bak in detect_backup:
    if name.lower().endswith(extension_bak):
     ret_bak.append(dirpath+name)
   for extension_doc in detect_documents:
    if name.lower().endswith(extension_doc):
     ret_doc.append(dirpath+name)
 show_results(ret_bak,ret_doc,ret_gitignore)
 
    
