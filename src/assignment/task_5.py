"""
Create a function called calculate_sum that accepts any number of numbers as arguments (using *args). The function should return the sum of all numbers passed in.

Call calculate_sum with varying numbers of arguments (e.g., calculate_sum(1, 2, 3) and calculate_sum(5, 10, 15, 20)).
"""


def my_sum(*args):
    return sum(args)

result1 = my_sum(2, 5, 6)
result2 = my_sum(4, 6, 7, 3)

print(result1)
print(result2)


