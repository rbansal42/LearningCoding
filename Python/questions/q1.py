"""

Define a function max() that takes two numbers as arguments and returns the largest of them. 
Use the if-then-else construct available in Python. 
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

"""

a = input("Enter number a: ")
b = input("Enter number b: ")

print(max(a, b))

def max(a, b):

    if(a == b):
        print("Both Values are equal")
    
    elif(a > b):
        return a

    elif(a < b):
        return b

