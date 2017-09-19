
import os
import csv

class Csv_tragac:
    def setParametri(self,folder):
        self.folder=folder
        self.file_list=os.listdir(folder)        
        return "Ok"
    
    def square(self.n):
        return self.n * self.n
    
#    def ucitavanje(self):
#        series=[]
#        for k in range(len(self.file_list)):
#            path=str1+str(self.file_list[k])
#            with open(path, 'r') as csvfile:
#                spamreader = csv.reader(csvfile, delimiter=';')
#                try:
#                    for row in spamreader:
#                        #print(row[1]!=None)
#                        if row[1]!=None:                
#                            series.append(float(row[1].replace(",", ".")))               
#                        #print(row[1])
#                except IndexError:
#                    gotdata = 'null'
#            #print(series[5])       
#            ceo_niz.append(series)                   
#            series=[]