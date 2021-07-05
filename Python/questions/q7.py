# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(str):

    str_reverse = ''
    j = len(str) - 1
    for i in range(len(str)):
        str_reverse += str[j]
        j -= 1
    return str_reverse

str = input("Input a String: ")

print(reverse(str))