import math

def add(a,b):
    return(a+b)

def sub(c,d):
    return(c-d)

def mult(a,b):
    return(a*b)

def div(c,d):
    return(c/d)
    
    
if __name__=='__main__':
    
    k1=int(input("Enter 1st Number:"))
    k2=int(input("Enter 2nd Number:"))
    print("ADD: " +str(add(k1,k2)))
    print("SUB: " +str(sub(k1,k2)))
    print("MULT: " +str(mult(k1,k2)))
    print("DIV: " +str(div(k1,k2)))
    