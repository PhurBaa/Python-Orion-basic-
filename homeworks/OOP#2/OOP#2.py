"""
1. Make the class with composition.
"""

class Laptop:
    def __init__(self):
        battery1 = Battery('A11-065')
        battery2 = Battery('ADLX65C')
        self.batterys = [battery1,battery2]



class Battery:
    def __init__(self):
        def __init__(self,model):
            self.model = model


"""
2. Make the class with aggregation.
"""

class Guitar:
    def __init__(self,guitar_string):
        self.guitar_string = guitar_string
        string1 = GuitarString ('This is first guitar string')
        string2 = GuitarString('This is second guitar string')


class  GuitarString:
    pass

"""
3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should be static
"""

class Summary:
