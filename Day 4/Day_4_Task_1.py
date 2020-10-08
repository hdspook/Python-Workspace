#Factorial Program using custom defined function

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


print("Enter a Number : ")

num = int(input())

print(f"The Factorial of {num} is : {factorial(num)}")


#Factorial using inbuilt fucntion

import math 

print(f"The Factorial of {num} using inbuilt fucntion is : {math.factorial(num)}")
