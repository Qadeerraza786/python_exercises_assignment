"""
7. Stripping Names
Task:
● Use a variable to represent a person’s name, and include some whitespace characters
at the beginning and end of the name.
● Make sure you use each character combination, \t and \n, at least once.
● Print the name once, so the whitespace around the name is displayed.
● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
strip().
"""
name: str ="\tQadeer raza\n"
print(name)
print(name.lstrip())
print(name.strip())
print(name.rstrip())
