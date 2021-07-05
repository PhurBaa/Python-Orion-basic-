"""
(1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

12. Convert (1) to list comprehension
"""

list_comp= [num **2 if num % 2 ==1 else num ** 4 for num in range(10)]
print(list_comp)

"""
3. Convert (2) to regular for with if-else
(2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
"""

list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)

print(list_comprehension)

"""
14. Convert (3) to dict comprehension.

(3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

"""

d = {num: num ** 2 for num in range (1,11) if num % 2 == 1}
print(d)

"""
15*. Convert (4) to dict comprehension.
(4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
"""

d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)

"""
16. Convert (5) to regular for with if.

(5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
"""
dict_comprehension = {}
for x in range(10):
    if x**3 % 4 ==0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)

"""
17*. Convert (6) to regular for with if-else.
(6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
"""
dict_comprehension2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension2[x] = x ** 3
    else:
        dict_comprehension2[x] = x
print(dict_comprehension2)