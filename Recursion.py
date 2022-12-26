#write a programme of
"""
def firstMethod():
    secondMethod()
    print("I am the first Method____1")

def secondMethod():
    thirdMethod()
    print("I am the second Method____2")

def thirdMethod():
    fourthMethod()
    print("I am the third Method____3")

def fourthMethod():
    print("I am the fourth Method____4")
firstMethod()
secondMethod()
thirdMethod()
fourthMethod()
 """
""" 
#Print number using Recursion
def recursiveMethod(n):
 if n<1:
     print("n is less than 1")
 else:
     recursiveMethod(n-1)
     print(n)
recursiveMethod(3)
"""
""" 
#write a program Power of two using Recursion

def PowerOfTwo(n):
    if n==0:
        return 1
    else :
        power=PowerOfTwo(n-1)
        return power*2

x=PowerOfTwo(7)
print(x)
"""
""" 
#Write a programe of Factorial of Number using  recursion

def Factorial(n):
    assert n>=0 and int(n)==n,'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else :
        return n*Factorial(n-1)

print(Factorial(4))
"""

""" 
#Factorila of number using  for loop
def Factorial(n):
    fact=1
    if n==1:
        return 1
    elif n<=0:
        return 1
    else :
        for i in range(1,n+1):
            fact=fact*i
        return fact
print(Factorial(8))

"""
#Factorila of number using  for loop
""" 
def Factorial(n):
   num=1
   while n>=1:
       num=num*n
       n=n-1
   return num
p=Factorial(5)
print(p)
"""
#create a program of Fibonacci using recursion
""" 
def Fibonacci(n):
    assert n>=0 and int(n)==n,'The number must be positive integer only!'
    if n in [0,1]:
        return n
    else :
        return Fibonacci(n-1)+ Fibonacci(n-2)
x=Fibonacci(7)
print(x)

"""
# HHow to find the sum of digits of a positive integer number using recursion ?

def SumOfTwoDigit(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n==0:
        return 0
    else :
        return int(n%10)+SumOfTwoDigit(int(n//10))
print(SumOfTwoDigit(121))

# How to find the sum of digits of a positive integer number without using recursion ?
def SumOfTwoDigit(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n==0:
        return 0
    else :
     su=int(n%10)
    um=SumOfTwoDigit(int(n//10))
    suum=su+um
print(SumOfTwoDigit(121))






