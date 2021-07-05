# Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

def len_of_string(a):

    len = 0

    for i in a:
        len += 1
    return len


s = input("Input String: ")

print(len_of_string(s))