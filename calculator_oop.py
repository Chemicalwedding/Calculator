import math

class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b
       
    def tangent(self, a, b):
    	  return math.atan2(a, b) 
    	
    def root(self, a):
    	  return math.sqrt(a) 

#create a calculator object
my_cl = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Tangent")
    print("6: Root")
    print("7: Exit")
    
    ch = int(input("Select operation: "))
    
    #Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 5, 6, 7):
        
        #first check whether user want to exit
        if(ch == 7):
            break
        
        #second if only root than only one input is required
        if(ch ==6):
        	a = float(input("Enter number: "))
        
        #If not then ask fo the input and call appropiate methods                
        elif(ch <=5):
        	a = float(input("Enter first number: "))
        	b = float(input("Enter second number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cl.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cl.multiply(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", my_cl.divide(a, b))
        elif(ch == 5):
            print(a, "tangent", b, "=", my_cl.tangent(a, b))
        elif(ch == 6):
            print("root of", a, "=", my_cl.root(a))
        
    else:
        print("Invalid Input")