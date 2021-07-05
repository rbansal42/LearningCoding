# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers
#       in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum1(elements):
    total = 0

    for i in range(len(elements)):
        total = total + elements[i]

    return total


def multiply1(elements):
    total = 1

    for i in range(len(elements)):
        total = total * elements[i]

    return total


s = [1, 2, 3, 4, 5]
print(sum1(s))
print(multiply1(s))
