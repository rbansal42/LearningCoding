# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

def is_palindrome(str):

    j = len(str) - 1
    for i in range(len(str)):

        if(str[i] != str[j]):
            return False
        else:
            return True

        j -= 1


str = input("Input a String: ")

print(is_palindrome(str))
