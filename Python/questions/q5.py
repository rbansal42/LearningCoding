# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). 
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def rob(s):
    s = s
    robbed = ''
    index = 0
    for i in s:
        if s[index] == 'a' or s[index] == 'e' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
            robbed = robbed + s[index]
            index += 1
        else:
            robbed = robbed + s[index] + 'o' + s[index]
            index += 1

    return robbed


string = input("Input the string to be robbed: ")

print(rob(string))
