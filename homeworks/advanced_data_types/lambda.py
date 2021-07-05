from functools import reduce
"""
18.Convert (7) to lambda function
(7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y

"""
foo = lambda x, y: x if x < y else y
print(foo(x=3, y=5))

"""
19*. Convert (8) to regular function
(8)
foo = lambda x, y, z: z if y < x and x > z else y

"""
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

print(foo(x=3, y=4, z=5))

"""
20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
"""
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print (sorted(lst_to_sort))

"""
21. Sort lst_to_sort from max to min
"""
print(sorted(lst_to_sort,reverse=True))

"""
22. Use map and lambda to update the lst_to_sort by multiply each element by 2
"""
new_lst_to_sort = list(map(lambda i: i * 2, lst_to_sort))
print(new_lst_to_sort)

"""
23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
"""

list_A = [2, 3, 4]
list_B = [5, 6, 7]

new_list = list(map(lambda x,y: x + y, list_A, list_B))
print(new_list)

"""
24. Use reduce and lambda to compute the numbers of a lst_to_sort.
"""

sum_lst = reduce(lambda x,y : x + y, lst_to_sort)
print(sum_lst)

"""
25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
"""
fil_lamb = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(fil_lamb)

"""
26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
"""
b = range(-10,10)

new_filter = list(filter(lambda x : x < 0, b))
print(new_filter)

"""
27*. Using the filter function, find the values that are common to the two lists:
"""
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

new_filter_list = list(filter(lambda x: list_2.count(x) > 0, list_1))
print(new_filter_list)