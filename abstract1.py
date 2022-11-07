from abc import ABC, abstractmethod
import math
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
class sub1(Myclass):
    def calculate(self,x):
         print('square value=', x*x)
class sub2(Myclass):
    def calculate(self,x):
         print('square root=', math.sqrt(x))
class sub3(Myclass):
    def calculate(self,x):
         print('cube=', x**3)
obj1=sub1()
obj1.calculate(16)
obj2=sub2()
obj2.calculate(16)
obj3=sub3()
obj3.calculate(16)

         
