import re
import os
import enum

def banner_show():
    print("Anti-backup-files v0.1 \n by github.com/CoolerVoid\n\n")
    print("\tUsage:\n\tpython3 anti-backup-files.py --path repository_name\n\n")

class size_types(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4

def byte_entropy(sizeInBytes, unit):
    if unit == size_types.KB:
        return sizeInBytes/1024
    elif unit == size_types.MB:
        return sizeInBytes/1048576
    elif unit == size_types.GB:
        return sizeInBytes/1073741824
    else:
        return sizeInBytes

def pathsize(filePath, size_type):
    try:
     size = os.path.getsize(filePath)
     return "%.6f" % (byte_entropy(size, size_type))
    except Exception as e:
     print(" log error : "+str(e))
     return "0"

def view_info(inlist):
     lists = sorted(inlist, key=lambda k: k['sizebytes'],reverse=True)
     for item in lists:
         print("Path: %s Size: %s MB" % (item['path'],item['sizebytes']))
         
def show_results(bak,doc,ignore):
 print("\nList of backup files:\n")
 view_info(bak)
 print("\nList of documents files:\n")
 view_info(doc)
 print("\nList of .gitignore files:\n")
 view_info(ignore)
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
   path=dirpath+"/"+name
   if ".gitignore" in name:
       ret_gitignore.append( {"path":path, "sizebytes" : pathsize(path,size_types.MB) } )
   for extension_bak in detect_backup:
    if name.lower().endswith(extension_bak):
     ret_bak.append( {"path":path, "sizebytes" : pathsize(path,size_types.MB)}  )
   for extension_doc in detect_documents:
    if name.lower().endswith(extension_doc):
     ret_doc.append( {"path":path, "sizebytes" : pathsize(path,size_types.MB)} )
 show_results(ret_bak,ret_doc,ret_gitignore)
 
    
