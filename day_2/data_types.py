a_float = float(123)

print(type(a_float))

# You can add _ to be used as a "comma", while using a comma will be used to indicate two (or more) different values.
print(123,4)
print(123_4)
# round() function instead of int() in order to round the float instead of chopping it off. ex: round(2.6666666, 2)
print(round(2.666666,2))
print(round(2.666666))
# floor division -> a division operation that rounds the result down to the nearest whole number or integer, which is less than or equal to the normal division result.
print("Normal")
print (8 / 3)
print("With floor division")
print(8 // 3)

# Number manipulation
score = 0
score += 1
print (score)

# f-Strings allows to aggregate multiple types (int, boolean, str & float)

print(f"Your score is {score}")