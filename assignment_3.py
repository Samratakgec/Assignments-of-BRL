import math
class Polygon :
    
    def area (self,a=None,b=None,c=None) :
        
        if a!= None and b==None and c==None :
            
            print("Command accepted to find the parameters for Circle") 
            ar = 3.14*a*a
            print("Area of circle is ",ar) 
            cr = 2*3.14*a
            print("Circumference of circle is ",cr) 
            
            
        if a!=None and b!=None and c==None :
            
            if a == b :
                
                
                print("Command accepted to find the parameters for Square") 
                ar = a*b 
                print("Area of square is ",ar)
                cr = 4*a
                print("Perimeter of square is ",cr) 
                
            else :
                
                print("Command accepted to find the parameters for Rectangle")  
                ar = a*b
                print("Area of rectangle is ",ar) 
                cr = 2*(a+b) 
                print("Perimeter of rectangle is ",cr) 
                
        elif a!= None and b!= None and c!= None :
            
            print("Command accepted to find the parameters for Triangle") 
            s = (a+b+c)/2
            ar = math.sqrt((s)*(s-a)*(s-b)*(s-c))
            print("Area of triangle is ",ar) 
            cr = a+b+c 
            print("Perimeter of triangle is ",cr) 
                
                
n = 1 
while n :
    
    x = int(input("Press 1 for circle, 2 for square, 3 for rectangle and 4 for triangle. ")) 
    print(" ")
    obj = Polygon()

    if x == 1 :
            
        a = int(input("Enter the radius of Circle "))
        obj.area(a)

    elif x == 2 :
            
        a = int(input("Enter one side length of Square "))
        obj.area(a,a) 
    
    elif x == 3 :
            
        a = int(input("Enter the length of Rectangle "))
        b = int(input("Enter the breadth of Rectangle "))
        obj.area(a,b)
            
    elif x == 4 :
            
        a = int(input("Enter the first side lenth of Triangle "))
        b = int(input("Enter the second side lenth of Triangle "))
        c = int(input("Enter the third side lenth of Triangle "))
        obj.area(a,b,c) 
    print(" ") 
        
    n= int(input("Enter 1 to continue and 0 to stop "))
        

 

                
                