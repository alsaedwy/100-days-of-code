# Python uses Mersenne Twister; a psudonrandom number generator.

# Do not name Python script as the imported module; it'll create a circular dependancy. (except it is an actual module you've created)

import random

# pi_module.py has the value of pi in a variable.
import pi_module

random_int = random.randint(1, 10)

print(random_int)

print(pi_module.pi)

# random() creates a float while randin() creates an integer

random_float = random.random() * 5
print(random_float)