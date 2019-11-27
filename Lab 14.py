import numpy as np
import matplotlib.pyplot as plt
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
    
    def computeCumProd(self, **kwargs):  #t is redundant. Change to **kwargs
        self._CumProd = (self._q_i - self._rate)/self._D_i
        return self._CumProd 
    
class InjectionWell(Well):
    sign = 1
    def __init__(self, **kwargs):
        if 'startDate' in kwargs: self._startDate = kwargs['startDate']
        if 'rate' in kwargs: self._rate = kwargs['rate']
        if 'CumProd' in kwargs: self._CumProd = kwargs['CumProd']
        if 'q_i' in kwargs: self._q_i = kwargs['q_i']
        
    def computeRate(self, **kwargs):
        if 'q_i' in kwargs: self._q_i = kwargs['q_i']
        return self._rate   
    
    def computeCumProd(self, t):
        self._CumProd = self._q_i * t
        return self._CumProd
    
class AppraisalWell(Well):
    sign = 0
    
well_1 = Well()
well_1.computeCumProd()
well_2 = Well()
well_2.computeCumProd()

producer_A = ProductionWell(startDate = 2001, rate = 5000, q_i = 6000, D_i = 0.03)

#producer_C = ProductionWell()
#producer_C.setStartDate(2020)
#producer_C.setInitRate(5000)

producer_B = ProductionWell(startDate = 2001, rate = 4000,q_i = 7000, D_i = 0.02)

injector_A = InjectionWell(startDate = 2005, rate = 2500, q_i = 9500)
injector_B = InjectionWell(startDate = 2005, rate = 2500, q_i = 10000)

producer_A.computeRate(10)
producer_A.computeCumProd()  #this computes CumProd, and is also an accessor or getter for the CumProd attribute



producer_B.computeRate(5)
producer_B.computeCumProd()

injector_B.computeRate()
injector_B.computeCumProd(t = 20)  

injector_A.computeRate()
injector_A.computeCumProd(t = 50) 

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
    
#EXTRA CREDIT
class Shape:
    def __init__ (self,**kwargs):
        if 'length' in kwargs: self._length = kwargs['length']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'area' in kwargs: self._area = kwargs['area']
        if 'volume' in kwargs: self._volume = kwargs['volume']
    
    def computeArea(self, **kwargs):
        self._area = 0
        return self._area   
    
    def computePerimeter(self,**kwargs):
        self._perimeter = 0
        return self._perimeter
    
    def computeSurfacearea(self,**kwargs):
        self._surfacearea = 0
        return self._surfacearea
    
    def computeVolume(self, **kwargs):
        self._volume = 0
        return self._volume
    
class TwoDshape(Shape):
    sign = -1
    def __init__ (self,**kwargs):
        if 'length' in kwargs: self._length = kwargs['length']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'area' in kwargs: self._area = kwargs['area']
        if 'perimeter' in kwargs: self._perimeter = kwargs['perimeter']
        
    def computeArea(self, **kwargs):
        self._area = 0
        return self._area 
    
    def computePerimeter(self,**kwargs):
        self._perimeter = 0
        return self._perimeter
        
class ThreeDshape(Shape):
    sign = 1
    def __init__ (self,**kwargs):
        if 'length' in kwargs: self._length = kwargs['length']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'volume' in kwargs: self._volume = kwargs['volume']
        if 'surfacearea' in kwargs: self._surfacearea = kwargs['surfacearea']
    
    def computeSurfacearea(self,**kwargs):
        self._surfacearea = 0
        return self._surfacearea
    
    def computeVolume(self, **kwargs):
        self._volume = 0
        return self._volume 
    
class rectangle (TwoDshape):
    sign = -2
    def __init__ (self,**kwargs):
        if 'length' in kwargs: self._length = kwargs['length']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'area' in kwargs: self._area = kwargs['area']
        if 'perimeter' in kwargs: self._perimeter = kwargs['perimeter']
    
    def computeArea(self, **kwargs):
        self._area = self._length*self._width
        return self._area 
    
    def computePerimeter(self,**kwargs):
        self._perimeter = (2*self._length)+(2*self._width)
        return self._perimeter
    
class triangle(TwoDshape):
    sign = -3
    def __init__ (self,**kwargs):
        if 'length1' in kwargs: self._length1 = kwargs['length1'] #length 1,2,3 refers to the different sides of a triangle
        if 'length2' in kwargs: self._length2 = kwargs['length2']
        if 'length3' in kwargs: self._length3 = kwargs['length3']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'area' in kwargs: self._area = kwargs['area']
        if 'perimeter' in kwargs: self._perimeter = kwargs['perimeter']
        
    def computeArea(self, **kwargs):
        self._area = self._height*self._width*0.5
        return self._area    
    
    def computePerimeter(self,**kwargs):
        self._perimeter = self._length1 + self._length2 + self._length3
        return self._perimeter
        
class  cuboid(ThreeDshape):
    sign = 2
    def __init__ (self,**kwargs):
        if 'length' in kwargs: self._length = kwargs['length']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'volume' in kwargs: self._volume = kwargs['volume']
        if 'surfacearea' in kwargs: self._surfacearea = kwargs['surfacearea']
        
    def computeSurfacearea(self,**kwargs):
        self._surfacearea = (self._length*self._height*4) + (self._width*self._height*2)
        return self._surfacearea
        
    def computeVolume(self, **kwargs):
        self._volume = self._length*self._width*self._height
        return self._volume    
        
class cube(ThreeDshape):
    sign = 3
    def __init__ (self,**kwargs):
        if 'length' in kwargs: self._length = kwargs['length']
        if 'width' in kwargs: self._width = kwargs['width']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'volume' in kwargs: self._volume = kwargs['volume']
        if 'surfacearea' in kwargs: self._surfacearea = kwargs['surfacearea']
    
    def computeSurfacearea(self,**kwargs):
        self._surfacearea = (self._length*self._width)*6
        return self._surfacearea

    def computeVolume(self, **kwargs):
        self._volume = self._length*self._width*self._height
        return self._volume 

box = cube(length = 3, width = 3, height = 3)
box.computeSurfacearea()
box.computeVolume()

pie = triangle(width = 10, height = 20, length1 = 10, length2 = 25, length3 = 22)
pie.computeArea()
pie.computePerimeter()

package = cuboid(length = 30, height = 24, width = 90)
package.computeSurfacearea()
package.computeVolume()

paper = rectangle(width = 8.5, length = 11)
paper.computeArea()
paper.computePerimeter()

for shape in [paper,pie]:
    print(shape._area,shape._perimeter)
    
for shape in [box,package]:
    print(shape._surfacearea, shape._volume)
    
for shape in [box,package,paper,pie]:
    print(shape._width)
    
#DISCUSSION    
    
#Data Encapsulation
#Dimensions MUST be entered when defining our objects. After defining dimensions, the object is able to access the necessary methods within the subclasses in order to compute either the perimeter, area, surface area, or volume. These values can then be printed.     
    
#Inheritance
#We start with the parent class, Shape. Within the shape class, we define 4 functions for computing volume, area, surface area, and permieter.
#Within the parent class, we define two subclasses, TwoDshape and ThreeDshape. Within those subclasses, we define that area and perimeter apply to 2-D shapes & surface area and volume apply to 3-D shapes.
#Within the 2-d shape subclass, we define more subclasses for when we have either a rectangle or triangle. Each new subclass has a method for computing its distinct area and perimeter.
#Within the 3-d shape subclass, we define more subclasses for when we have either a cube or cuboid. Each new subclass has a different method for computing its volume and surface area.
    
#Polymorphism was used in the last three loops of code. 
#For loop 1, I had the loop print the area and perimeter of our 2-D shapes. 
#For loop 2, I had the loop print the surface area and volume of our 3-D shapes.
#For loop 3, I had the loop print out a common attribute to all of our objects; the width of the shape.