# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:09:36 2017

@author: aleksat90
"""

import sys
from numpy import NaN, Inf, arange, isscalar, asarray, array

class Citanje_lokala():
    maxtab = []
    mintab = []
    
    def pokretanje(self,vrednosti,preciznost):        
        self.series=vrednosti
        self.razlika=preciznost
        
        self.peakdet()
        
        #niz_max=[] 
        #niz_min=[]
        #if __name__=="__main__":
        from matplotlib.pyplot import plot, scatter, show
        maxtab, mintab = self.peakdet()
        plot(self.series)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
        scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
        show()
    
    #v niz za koji se trazi peak
    #delta -> vrednosti 
    def peakdet(self,x = None): 
        v=self.series #dodeljivanje vrednosti niz ka vrednosti v koja ce se dalje koristiti
        delta=self.razlika #dodeljivanje vrednosti razlika kao delta u metodi
        
        maxtab = []
        mintab = [] 
           
        if x is None:
            x = arange(len(v))
        
        v = asarray(v)
        
        if len(v) != len(x):
            sys.exit('Input vectors v and x must have same length')
        
        if not isscalar(delta):
            sys.exit('Input argument delta must be a scalar')
        
        if delta <= 0:
            sys.exit('Input argument delta must be positive')
        
        mn, mx = Inf, -Inf
        mnpos, mxpos = NaN, NaN
        
        lookformax = True
        
        for i in arange(len(v)):
            this = v[i]
            if this > mx:
                mx = this
                mxpos = x[i]
            if this < mn:
                mn = this
                mnpos = x[i]
            
            if lookformax:
                if this < mx-delta:
                    maxtab.append((mxpos, mx))
                    mn = this
                    mnpos = x[i]
                    lookformax = False
            else:
                if this > mn+delta:
                    mintab.append((mnpos, mn))
                    mx = this
                    mxpos = x[i]
                    lookformax = True
        return array(maxtab), array(mintab)
    


    def getValues(self):
        niz_max=self.peakdet.maxtab
        return niz_max


#TESTIRANJE KLASE
test_niz=[0.05, 0.08, 0.08, 0.08, 0.1, 0.1, 0.08, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.21, 0.18, 0.18, 0.12, 0.1, 0.18, 0.15, 0.18, 0.12, 0.15, 0.18, 0.28, 0.42, 0.52, 0.6, 0.83, 0.94, 1.15, 1.3, 1.47, 1.66, 1.81, 1.91, 2.07, 2.15, 2.36, 2.6, 2.88, 3.03, 3.34, 3.53, 3.82, 4.03, 4.37, 4.58, 4.99, 5.19, 5.52, 5.82, 6.18, 6.38, 6.75, 6.93, 7.25, 7.4, 7.59, 7.74, 7.8, 7.8, 7.92, 8.02, 8.16, 8.29, 8.29, 8.39, 8.47, 8.44, 8.54, 8.53, 8.5, 8.36, 8.53, 8.63, 8.72, 8.77, 8.83, 8.88, 8.93, 8.93, 8.9, 8.88, 8.95, 8.88, 9.01, 9.06, 9.11, 9.19, 9.26, 9.35, 9.37, 9.35, 9.35, 9.35, 9.11, 9.26, 9.43, 9.5, 9.63, 9.66, 9.71, 9.74, 9.68, 9.74, 9.66, 9.61, 9.61, 9.74, 9.87, 10.05, 10.08, 10.13, 10.15, 10.08, 10.08, 10.02, 9.95, 9.99, 10.13, 10.29, 10.36, 10.39, 10.44, 10.5, 10.51, 10.39, 10.31, 10.23, 10.39, 10.5, 10.62, 10.7, 10.83, 10.88, 10.88, 10.88, 10.83, 10.81, 10.62, 10.6, 10.81, 10.91, 10.88, 10.41, 9.4, 8.26, 7.14, 6.23, 5.82, 4.96, 4.23, 3.95, 3.24, 2.3, 1.55, 0.88, 0.54, 0.33, 0.31, 0.21, 0.1, 0.02, 0.02, 0.02, 0.0, 0.05, 0.05]

#Pokretanje
objekat = Citanje_lokala()

objekat.pokretanje(test_niz,0.07)   
