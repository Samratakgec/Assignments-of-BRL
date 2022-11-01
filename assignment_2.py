# sum   diff    multiplication  both_mag    slope_of_line_formed    anglediff

import math
from abc import ABC, abstractmethod

class A(ABC) :
    
    @abstractmethod
    def cal (self,a,b,c,d) :
        pass
    
class sum (A) :
    
    def __init__(self) :
        print("The Sum is ")
        
    def cal (self,a,b,c,d) :
        print(a+c)
        print(b+d)
    
    
class diff (A) :
    
    def __init__(self) :
        print("The Difference is ")
        
    def cal (self,a,b,c,d) :
        print(a-c)
        print(b-d) 
        
        
class mul (A) :
    
    def __init__(self) :
        print("Their product is")
        
    def cal (self,a,b,c,d) :
        print((a*c)-(b*d)) 
        print((a*d)+(b*c)) 
        
        
class mag(A) :
    
    def __init__(self) :
        print("Their magnitudes are") 
        
    def cal (self,a,b,c,d) :
        print(math.sqrt((a*a)+(b*b))) 
        print(math.sqrt((c*c)+(d*d))) 
        
class eq (A)  :
    
    def __init__(self) :
        print("The equation of line formed") 
        
    def cal (self,a,b,c,d) :
        m = (d-b)/(c-a) 
        print("Y - ",b,"=",m,"(X -",a,") of slope ",m)    
    
        
class anglediff (A) :
    
    def __init__(self) :
        print("The difference of their angles made with origin")
        
    def cal (self,a,b,c,d) :
        m1 = b/a
        m2 = c/d 
        m3 = m1-m2
        tantheta = (abs(m3))/(1+(m1*m2))
        angle = math.atan(tantheta) 
        
        angle = math.degrees(angle) 
        print(angle) 
        
n = 1

while n :
    print("Enter two complex numbers")
    print(" ")
    print("Enter real part of first complex number")
    a=int(input())
    print("Enter imaginary part of first complex number")
    b=int(input())
    print("Enter real part of second complex number")
    c=int(input())
    print("Enter imaginary part of second complex number")
    d =int(input())

    print(" ")
    print("Enter 1 to add")
    print("Enter 2 to substract")
    print("Enter 3 to find their product")
    print("Enter 4 to find their magnitudes")
    print("Enter 5 to find the equation of line formed") 
    print("Enter 6 to find The difference of their angles made with origin") 


    n =int(input())

    if n==1 :
       obj = sum()
       obj.cal(a,b,c,d) 
   

    if n==2 :
        obj = diff()
        obj.cal(a,b,c,d) 
    
    if n==3 : 
        obj = mul()
        obj.cal(a,b,c,d) 
        
    if n==4 : 
        obj = mag()
        obj.cal(a,b,c,d) 
        
    if n==5 : 
        obj = eq() 
        obj.cal(a,b,c,d) 
    
    if n==6 : 
        obj = anglediff()  
        obj.cal(a,b,c,d) 
        
    print(" ")
   
    n = int(input("Enter 1 to continue or 0 to stop "))
    
print("End of Program")
    
    
    
    
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    



