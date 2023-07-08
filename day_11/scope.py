# Global scope variable (global variable)
var = 1 

def increase():
    # Local scope (variable)
    var = 2
    print(f"Inside {var}")

print(f"Outside {var}")
increase()


# local and global scopes apply to functions and variables 

def outer_func():
    # local scope
    def inner_func():
        print(1)
    inner_func()

# global scope (will give an error if called outside of outer_func())
# inner_func()
# error: 
#     inner_func()
#     ^^^^^^^^^^
# NameError: name 'inner_func' is not defined. Did you mean: 'outer_func'?


# block scopes are considered in the global scope/namespace
# scopes only apply to functions (probably something else as well), but not to blocks; like if, while and for loops.

"""
To modify a global variable inside a function, we can use the argument "global", example:
"""

global_var = 10

def increase_by_1():
    global global_var
    global_var += 1
    print(global_var)

increase_by_1()

# It is not a good practice to use "global" argument, since you can --read-- and --use-- it, but modifying it is not a good practice.

# You can use "return" to modify the global variable as a better practice.

# It is a good practice to captialize the global variables:
PI = 3.14159
URL = "HTTPS://alaa.sh"