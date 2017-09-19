#Uvoz potrebnih klasa i biblioteka
import pik_tragac

#TESTIRANJE KLASE
test_niz=[0.05, 0.08, 0.08, 0.08, 0.1, 0.1, 0.08, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.21, 0.18, 0.18, 0.12, 0.1, 0.18, 0.15, 0.18, 0.12, 0.15, 0.18, 0.28, 0.42, 0.52, 0.6, 0.83, 0.94, 1.15, 1.3, 1.47, 1.66, 1.81, 1.91, 2.07, 2.15, 2.36, 2.6, 2.88, 3.03, 3.34, 3.53, 3.82, 4.03, 4.37, 4.58, 4.99, 5.19, 5.52, 5.82, 6.18, 6.38, 6.75, 6.93, 7.25, 7.4, 7.59, 7.74, 7.8, 7.8, 7.92, 8.02, 8.16, 8.29, 8.29, 8.39, 8.47, 8.44, 8.54, 8.53, 8.5, 8.36, 8.53, 8.63, 8.72, 8.77, 8.83, 8.88, 8.93, 8.93, 8.9, 8.88, 8.95, 8.88, 9.01, 9.06, 9.11, 9.19, 9.26, 9.35, 9.37, 9.35, 9.35, 9.35, 9.11, 9.26, 9.43, 9.5, 9.63, 9.66, 9.71, 9.74, 9.68, 9.74, 9.66, 9.61, 9.61, 9.74, 9.87, 10.05, 10.08, 10.13, 10.15, 10.08, 10.08, 10.02, 9.95, 9.99, 10.13, 10.29, 10.36, 10.39, 10.44, 10.5, 10.51, 10.39, 10.31, 10.23, 10.39, 10.5, 10.62, 10.7, 10.83, 10.88, 10.88, 10.88, 10.83, 10.81, 10.62, 10.6, 10.81, 10.91, 10.88, 10.41, 9.4, 8.26, 7.14, 6.23, 5.82, 4.96, 4.23, 3.95, 3.24, 2.3, 1.55, 0.88, 0.54, 0.33, 0.31, 0.21, 0.1, 0.02, 0.02, 0.02, 0.0, 0.05, 0.05]

#Pokretanje
objekat = pik_tragac.Citanje_lokala()

objekat.pokretanje(test_niz, 0.02) 

import csv_tragac
folder="C:\\Users\\TOA2BG\Documents\\Phyton\\Peak_finder\\P_07"

tragac=csv_tragac.Csv_tragac()
lista1=tragac.setParametri(folder)
lista=tragac.file_list
tragac.square(5)


#PREBACENO IZ PEAK FINEDER       
        
import os
folder="C:\\Users\\TOA2BG\Documents\\Phyton\\Peak_finder\\P_07"
file_list=os.listdir(folder)

str1="C:\\Users\\TOA2BG\Documents\\Phyton\\Peak_finder\\P_07\\"
str2=str(file_list[0])
str3=str1+str2


import csv
series=[]
ceo_niz=[]


for k in range(len(file_list)):
    path=str1+str(file_list[k])
    with open(path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        try:
            for row in spamreader:
                #print(row[1]!=None)
                if row[1]!=None:                
                    series.append(float(row[1].replace(",", ".")))               
                #print(row[1])
        except IndexError:
            gotdata = 'null'
    #print(series[5])       
    ceo_niz.append(series)                   
    series=[]


retightening_MAX=[]   
#Kreiranje objekta za peak
from matplotlib.pyplot import plot, scatter, show
kor_faktor=0 #Korektivni faktor za smanjenje vrednosti retightening.
for brojac in range(len(ceo_niz)+1) :  #default  range(len(ceo_niz)+1)
    print(brojac) 
    aleksa=ceo_niz[:][brojac-1]
    pikovanje.pokretanje(aleksa)
    for brojac_max in range(len(pikovanje.niz_max)):
        print("u petlji")
        if pikovanje.niz_max[brojac_max][1]>5:
            retightening_MAX.append(pikovanje.niz_max[brojac_max]-kor_faktor)            
            #plot(self.series)
            scatter(array(retightening_MAX)[:,0], array(retightening_MAX)[:,1], color='blue')
            print("break")
            break
        
for stampa in range(len(retightening_MAX)):
    deo1=str(file_list[stampa])
    deo2=str(retightening_MAX[stampa][1])
    print(deo1+"   "+deo2)