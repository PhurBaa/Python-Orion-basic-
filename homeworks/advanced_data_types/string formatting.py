"""
Replace the placeholders with a value:
"Anna has ___ apples and ___ peaches."

5. With .format and curly braces {}
"""
print(('Anna has {} apples and {} peaches'.format(1, 2)))

"""
6. By passing index numbers into the curly braces.
"""
print('Anna has {0} apples and {1} peaches'.format(2, 6))

"""
7. By using keyword arguments into the curly braces.
"""
print('Anna has {apples} apples and {peaches} peaches'.format(apples=4, peaches=3))

"""
8*. With indicators of field size (5 chars for the first and 3 for the second)
"""
print('Anna has {0:5} apples and {1:3} peaches'.format(5,7))

"""
9. With f-strings and variables
"""
apples = 8
peaches = 10
print(f'Anna has {apples} apples and {peaches} peaches')

"""
10. With % operator
"""
apples = 11
peaches = 15
print('Anna has %d apples and %d peaches' % (apples, peaches))

"""
11*. With variable substitutions by name (hint: by using dict)
"""
a = {'apples': 12, 'peaches': 16}
print('Anna has {apples} apples and {peaches} peaches'.format(**a))

