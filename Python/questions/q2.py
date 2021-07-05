# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a,b,c):
    if(a == b):

        if(a > c):
            return a
        else:
            return c

    
    elif(b==c):

        if(a>b):
            return a
        else:
            return b

    elif(a == c):

        if(a>b):
            return a
        else:
            return b

    elif(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


a = input("Enter input a: ")
b = input("Enter input b: ")
c = input("Enter input c: ")

print(max_of_three(a, b, c))