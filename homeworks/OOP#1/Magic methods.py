"""
8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
otherwise return message: "Your city is too small".
"""


class City:
    def __init__(self,name,population):
        self.name = name
        self.population = population


    def __new__(cls, name,population):
        if population > 1500:
            new_instace = super(City,cls).__new__(cls)
            return new_instace
        else:
            return print("Your city is too small")


"""
9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
"""

class City:
    def __init__(self,name,population):
        self.name = name
        self.population = population


    def __new__(cls, name,population):
        if population > 1500:
            new_instace = super(City,cls).__new__(cls)
            print(f'The population of the city {name} is {population}')
            return new_instace
        else:
            return print("Your city is too small")

"""
10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.
"""

class AddMethod:
    def __init__(self,x):
        self.x = x

    def __abs__(self,y):
        if y.x >10 or self.x > 10:
            return self.x * y.x
        else:
            self.x + y.x

"""
11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
Create a new class with __call__ method and define this call to return sum.
"""

class Calleble:

    def __call__(self,number1,number2):
        sum = number1 + number2
        return sum

"""
12*. Making Your Objects Truthy or Falsey Using __bool__().
Create class MyOrder with cart and customer instance attributes.
Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
e.g.:
order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
bool(order_1)
True
bool(order_2)
False
"""

class MyOrder:

    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        cart_len = len(self.cart)
        return cart_len > 0

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
