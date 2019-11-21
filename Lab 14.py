# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

import pandas as pd
import sqlite3

class Well:
    def __init__(self, **kwargs):
        if 'startDate' in kwargs: self._startDate = kwargs['startDate']
        if 'rate' in kwargs: self._rate = kwargs['rate']
        if 'CumProd' in kwargs: self._CumProd = kwargs['CumProd']
        if 'q_i' in kwargs: self._q_i = kwargs['q_i']
        if 'D_i' in kwargs: self._D_i = kwargs['D_i']
        
    def computeRate(self):
        self._rate = 0
        return self._rate
    
    def computeCumProd(self):
        self._CumProd = 0
        return self._CumProd
    
    def getStartDate(self):
        pass
    
    def setStartDate(self,myStartDate):
        self._startDate = myStartDate
        
    def setInitRate(self,qi):
        self._q_i = qi
        
    def setRate(self,r):
        self._rate = r
    
    def setCumP(self,CP):
        self._CumProd = CP
        
    def setDailyRate(self,Di):
        self._D_i = Di
    
class ProductionWell(Well):
    sign = -1  # this is a class property
    def __init__(self, **kwargs):
        if 'startDate' in kwargs: self._startDate = kwargs['startDate']
        if 'rate' in kwargs: self._rate = kwargs['rate']
        if 'CumProd' in kwargs: self._CumProd = kwargs['CumProd']
        if 'q_i' in kwargs: self._q_i = kwargs['q_i']
        if 'D_i' in kwargs: self._D_i = kwargs['D_i']
        
    def computeRate(self, t):    #this method overrides the version in the "Well" super class 
        self._rate = self._q_i*np.exp(-(self._D_i)*t)
        return self._rate   
    
    def computeCumProd(self, *inputVars):  #t is redundant. Change to **kwargs
        t = inputVars[0]
        self._CumProd = (self._q_i - self._rate)/self._D_i
        return self._CumProd 
    
    def getStartDate(self):
        pass
    
    def setStartDate(self,myStartDate):
        self._startDate = myStartDate
        
    def setInitRate(self,qi):
        self._q_i = qi
        
    def setRate(self,r):
        self._rate = r
    
    def setCumP(self,CP):
        self._CumProd = CP
        
    def setDailyRate(self,Di):
        self._D_i = Di
    
class InjectionWell(Well):
    sign = 1
    def __init__(self, **kwargs):
        if 'startDate' in kwargs: self._startDate = kwargs['startDate']
        if 'rate' in kwargs: self._rate = kwargs['rate']
        if 'CumProd' in kwargs: self._CumProd = kwargs['CumProd']
        if 'q_i' in kwargs: self._q_i = kwargs['q_i']
        if 'D_i' in kwargs: self._D_i = kwargs['D_i']
        
    def computeRate(self, q_i):
        self._rate = q_i
        return self._rate   
    
    #Cum Prod is computed based on constant rate of water injection
    def computeCumProd(self, t):
        self._CumProd = self._q_i * t
        return self._CumProd
    
    def setStartDate(self,myStartDate):
        self._startDate = myStartDate
        
    def setInitRate(self,qi):
        self._q_i = qi
        
    def setRate(self,r):
        self._rate = r
    
    def setCumP(self,CP):
        self._CumProd = CP
        
    def setDailyRate(self,Di):
        self._D_i = Di
    
class AppraisalWell(Well):
    sign = 0
    
well_1 = Well()
well_1.computeCumProd()
well_2 = Well()
well_2.computeCumProd()

producer_A = ProductionWell(startDate = 2001, rate = 5000, q_i = 6000)

producer_C = ProductionWell()
producer_C.setStartDate(2020)
producer_C.setInitRate(5000)

producer_B = ProductionWell(startDate = 2001, rate = 4000, D_i = 0.02)

injector_A = InjectionWell(startDate = 2005, rate = 2500)
injector_B = InjectionWell(startDate = 2005, rate = 2500)

producer_A.computeRate(10)
producer_A.computeCumProd(10)  #this computes CumProd, and is also an accessor or getter for the CumProd attribute

producer_B.computeRate(11)
producer_B.computeCumProd(11)

injector_B.computeRate(1000)
injector_B.computeCumProd(11)  

injector_A.computeRate(1000)
injector_A.computeCumProd(11) 

#It will be a bad idea to accesss and modify the CumProd attribute of a producer directly from other codes.
#An accessor or getter needs to be used, in keeping with the tenets of OOP. Specifically, data encapsulation.
producer_A._CumProd
producer_A._CumProd = 30000  #Other programs can prevent this by using private variables.  DON'T DO THIS!!
producer_A._CumProd

for well in [producer_A, producer_B, injector_A, injector_B, well_1]:
    print(well._CumProd)  #This is polymorphism. The well object could be a ProductionWell, an InjectionWell, etc.

#well_1 = producer_A

#well_1._q_i
#well_1.computeRate(3)
#well_1._rate
#well_1.sign
#type(well_1)
#def main():
    #well_1 = Well()