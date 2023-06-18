print("If in succession")
# both if statements will be executed
if True:
    print("True")
if True:
    print("True")
else:
    print("False")

print("Using elif")
# only the first "if" or "elif" that is True will be executed
if True:
    print("True")
elif True:
    print("True")
else:
    print("True")

# lecture 34, day 3

# If the "if" statement is nested -> it is not mandatory to add else.

# If a condition with "elif" is matched, everything else is ignored.