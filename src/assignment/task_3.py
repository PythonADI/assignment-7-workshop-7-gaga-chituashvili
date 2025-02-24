"""
Define a variable name = "Alice" at the global level. Create a function change_name that has a local variable also called name with the value "Bob". Print name both inside and outside the function after calling change_name.

- Observe how Python handles variables with the same name in different scopes.
- Try adding global name inside change_name and see what happens to the global name.
"""


NAME = "Alice"


def change_name():
    NAME = "Bob"
    print(NAME)

change_name()
print(NAME)


def global_name():
    global NAME
    NAME = "NICK"
    print(NAME)

global_name()

print(NAME)