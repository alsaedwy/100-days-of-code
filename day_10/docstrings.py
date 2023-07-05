test_string = """
Hello
World!
"""
print(test_string)

def doc_func():
    # Does magical things
    return False

print(doc_func(.__doc__))