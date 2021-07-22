"""
Magic methods:
8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
otherwise return message: "Your city is too small".
"""


class City(object):
    def __new__(cls, name, population):
        if population > 1500:
            return object
        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population


kyiv = City('kyiv', 2884000)
lviv = City('lviv', 721301)



class City():
    def __new__(cls, name, population):

        if population > 1500:
            return super().__new__(cls)
        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population


kyiv = City('Kyiv', 2884000)
lviv = City('lviv', 721301)



"""
9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
"""


class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'The population ot the city {self.name} is {self.population}'


kyiv = City('Kyiv', 2884000)
lviv = City('Lviv', 721301)



"""
10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.
"""

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)

        else:
            print('Your city is too small')

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'The population at the city {self.name} is {self.population}'

    def __add__(self, other):
        if self.population > 10 or other.population > 10:
            return self.population * other.population
        else:
            return self.population + other.population


kyiv = City('Kyiv', 2884000)
lviv = City('Lviv', 721301)


"""
11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
Create a new class with __call__ method and define this call to return sum.
"""

class Salary:
    total_hour_of_work = 0
    total_salary = 0

    def __init__(self, price_per_hour):
        self.price_per_hour = price_per_hour

    def __call__(self, time_of_work):
        self.total_hour_of_work += time_of_work
        self.total_salary += time_of_work * self.price_per_hour
        return time_of_work * self.price_per_hour


manager = Salary(10)
print('month1', manager(5))
print('month2', manager(6))
print('month3', manager(7))


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
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 1:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')

print(bool(order_1))
print(bool(order_2))