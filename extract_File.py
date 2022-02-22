
from unicodedata import digit
import zipfile
import csv
from pathlib import Path
import glob

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
      finalFile.sort()
     
      for i in finalFile:
        if i[0] != 'ï»¿Source IP':
       
          writer.writerow(i)






     
   
 

 






















# zf = zipfile.ZipFile("MYFILE.zip",'w',compression=zipfile.ZIP_DEFLATED)
# zf.write('a.txt')
# zf.write('b.txt')
# zf.close()

  # if you want to see all files inside zip folder
  #  zf.namelist() 
  # now read your csv file 
#   df = pd.read_csv(zf.open('prod1.csv'))






    # print('Extract all files in ZIP to current directory')
    # # Create a ZipFile Object and load sample.zip in it
    # with ZipFile('Engineering Test Files.zip', 'r') as zipObj:
    #    # Extract all the contents of zip file in current directory
    #    zipObj.extractall()
    
  