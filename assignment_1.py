class A :
    
    def __init__(self) :
        print("Welcome to class A")  
    
    def sum(self,a,b) :
       # print(a+b)
        print("This is sum function in class A",a+b)
        
    
class B(A) :
    
    def __init__(self) :
        print("Welcome to class B")
    def ssq(self,a,b) :
        self.a = a*a
        self.b = b*b 
        print("This is sum of sqrs function in class B", self.a + self.b)



class C(B) :
    
    def __init__(self) :
        print("Welcome in class C")    
    
    
    def div(self,a,b) :
        a = float(a)
        b = float(b)
        print("This is div function in class C", a/b) 


class D(B) :
    
    def __init__(self) :
        print("Welcome in class D")
    
    
    
    def modulo (self,a,b) :
       
        print("This is modulo function in classs D", a%b) 
        


class E(C,D) :
    def __init__ (self) :
        print("Welcome to class E")
    
    def sub (self,a,b) :
       print("This is substraction function in class E", a-b) 
       
       
print("Enter two numbers")       
x =  int(input())
y =  int (input())

print(" ")
print(" ")
objA = A()
objA.sum(x,y)
print("End of class A") 
print(" ")
print(" ")

objB= B()
objB.ssq(x,y) 
objB.sum(x,y) 
print("Class A is called as it is inherited in B") 
print("End of class B") 
print(" ")
print(" ")

objC = C()
objC.div(x,y)
objC.ssq(x,y)
objC.sum(x,y)
print("Class B is called as they were inherited in C")
print("End of class C")
print(" ")
print(" ")
    
objD = D()
objD.modulo(x,y)
objD.ssq(x,y)
objD.sum(x,y) 
print("Class  B is called as they were inherited in D")
print("End of class D") 
print(" ")
print(" ")

objE = E()
objE.sub (x,y)
objE.modulo(x,y)
objE.ssq(x,y)
objE.sum(x,y) 
print("Classes C and D are called as they were inherited in E") 
print("End of class E") 
print(" ")
print(" ")


    
    
    
    

