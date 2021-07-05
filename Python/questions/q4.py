# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def is_vowel(a):

    if(a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u'):
        return True
    
    else:
        return False

a = input("Enter a single character: ")

print(is_vowel(a[0]))