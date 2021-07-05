"""
1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
"""
int_a = 55
print (id(int_a))

str_b = 'cursor'
print(id(str_b))

set_c = {1, 2, 3}
print(id(set_c))

lst_d = [1, 2, 3]
print(id(lst_d))

dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))

"""
2. Append 4 and 5 to the lst_d and define the id one more time.
"""

lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

"""
3. Define the type of each object from step 1.
"""
print(type(int_a), type(str_b),type(set_c), type(lst_d), type(dict_e))

"""
4*. Check the type of the objects by using isinstance.
"""
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

