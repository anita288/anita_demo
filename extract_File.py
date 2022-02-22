
from unicodedata import digit
import zipfile
import csv
from pathlib import Path
import glob
import ipaddress
import pandas as pd

zf = zipfile.ZipFile("TEST.zip",'r')
zf.extractall("")
# csv_files =zf.namelist()
csv_files = [f for f in glob.glob("TEST/*.csv")]

header =['Source IP','Environment']
filelist =[]



if 'Test/combined.csv' not in csv_files:
    with open('Test/combined.csv', 'w',newline='') as f:
      writer = csv.writer(f)
      writer.writerow(header)
      
      for file in csv_files:
        filename=Path(file).stem
        filename =''.join([i for i in filename if not i.isdigit()])
       
        with open(file,'r') as df:
         data = csv.reader(df)
         for row in data:
           
            filelist.append([row[0],filename])
       
      
      
      m =set(tuple(x) for x in filelist)
      finalFile =[list(x) for x in m]
      
     
      for i in finalFile:
        if i[0] != 'ï»¿Source IP':
       
          writer.writerow(i)

    d1= csv.reader(open("Test/Combined.csv"))
    next(d1)
    d2 = sorted(d1,key= lambda row : (ipaddress.IPv4Address(row[0]),row[1]))
    print(d1)
    d1= open("Test/Combined.csv",'w',newline='')
   
    w = csv.writer(d1)
    w.writerow(header)
    for i in d2:

      w.writerow(i)
    
          






     
   
 

 


























  