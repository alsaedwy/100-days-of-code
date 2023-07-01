import inspect
import random
source_file = inspect.getsource(random.randrange)
print(source_file)