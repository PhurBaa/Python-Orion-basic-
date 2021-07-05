"""
1. Create a Vehicle class with max_speed and mileage instance attributes
"""


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


"""
2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
"""


class Bus(Vehicle):
    def __init__(self, seating_capacity, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


"""
3. Determine which class a given Bus object belongs to (Check type of an object)
"""
print("Object type Buss:", type(Bus))
print(isinstance(Bus, type))

"""
4. Determine if School_bus is also an instance of the Vehicle class
"""
School_bus = Bus(20, 90, 1200)
print(isinstance(School_bus, Vehicle))

"""
5. Create a new class School with get_school_id and number_of_students instance attributes
"""


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


"""
6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
"""


class SchoolBus(School, Bus):
    def __init__(self, bus_school_color):
        self.bus_shool_color = bus_school_color

        School.__init__(self=School, get_school_id=142, number_of_students=10000)
        Bus.__init__(self=Bus, seating_capacity=50, max_speed=90, mileage=12000)

        def bus_school_color():
            bus_school_color = "Red"
            return bus_school_color


"""
7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
make a tuple of it and by using for call their action using the same method.
"""


class Bear:
    def make_sound(self):
        print("Hello, I'm angry bear")


class Wolf:
    def make_sound(self):
        print("Hello, I'm angry wolf")


bear = Bear()
wolf = Wolf()

for animals in (bear, wolf):
    animals.make_sound()
