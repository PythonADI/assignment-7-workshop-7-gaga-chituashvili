"""
Write a function called describe_person that takes any number of keyword arguments using **kwargs and prints each key-value pair in the format "key: value".

Test describe_person with different sets of keyword arguments (e.g., name="Alice", age=30, city="New York").
"""


def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, city="New York")