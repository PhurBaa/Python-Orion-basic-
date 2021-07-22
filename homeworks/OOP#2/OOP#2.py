"""
1. Make the class with composition.
"""


class Laptop:
    def __init__(self):
        battery1 = Battery('A11-065')
        battery2 = Battery('ADLX65C')
        self.batterys = [battery1, battery2]


class Battery:
    def __init__(self):
        def __init__(self, model):
            self.model = model


"""
2. Make the class with aggregation.
"""


class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar = Guitar()

"""
3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should be static
"""


class Summary:
    @staticmethod
    def add_nums(a, b, c):
        sum = a + b + c
        return sum


"""
4.    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
 It should have 2 methods:
 carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
 which should create Pasta instances with predefined list of ingredients.
 Example:
     pasta_1 = Pasta(["tomato", "cucumber"])
     pasta_1.ingredients will equal to ["tomato", "cucumber"]
     pasta_2 = Pasta.bolognaise()
     pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
 """


class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


"""
5.    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """


class Concert:
    max_visitor_num = 0

    def __init__(self, visitors_count):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return f"Max visitors number: {self._visitors_count}"

    @visitors_count.setter
    def visitors_count(self, v_count):
        if v_count > self.max_visitor_num:
            self._visitors_count = self.max_visitor_num
        else:
            self._visitors_count = v_count


Concert.max_visitor_num = 5000
concert = Concert()
concert.visitors_count = 3567
print(concert.visitors_count)

"""
6.    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
7.    Create the same class (6) but using NamedTuple
"""
import dataclasses
from collections import namedtuple


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


AddressBookDataClass = namedtuple('AdressBookDataClass',
                                  ['key', 'name', 'phone_number', 'adress', 'email', 'birthday', 'age'])
my_adress = AddressBookDataClass(142, 'Vitalii', '+380633709346', 'Bereznyakivska street', 'phurba@icloud.com',
                                 '13.09.89', 31)

"""
8.    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
Make its str() representation the same as for AddressBookDataClass defined above.
"""


class AdressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
            return f'Info about us {self.key} {self.name} {self.phone_number} {self.adress} {self.email} {self.birthday} {self.age}'


my_adress = AddressBookDataClass(142, 'Vitalii', '+380633709346', 'Bereznyakivska street', 'phurba@icloud.com',
                                 '13.09.89', 31)

"""
9.    Change the value of the age property of the person object
"""


class Person:
    def __init__(self, name, age, conuntry):
        self.name = name
        self.age = age
        self.conuntry = conuntry


person = Person('John', '36', 'USA')
setattr(person, 'age', '31')


@property
def person_info(self):
    return print(f'Name : {self.name}, Age: {self.age}, Country: {self.country}')


print('Hello, my name is:', getattr(person, 'age'))

"""
10.   Add an 'email' attribute of the object student and set its value
   Assign the new attribute to 'student_email' variable and print it by using getattr
"""


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


id = 0
name = ' '

student = Student('0', 'Vitalii')
setattr(student, 'email', 'none')
student_email = student.email
setattr(student, 'student_email', 'iphurba@iloud.com')

print('Hello, my name is:', getattr(student, 'name'), 'my email is:', getattr(student, 'student_email'))

"""
12.    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
"""


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def convert(self):
        celsius_to_fahrenheit = (self._temperature * 1.8) + 32
        temp = f'Temperature is {celsius_to_fahrenheit} on fahrenheit'
        return temp


print(Celsius(5).convert)
