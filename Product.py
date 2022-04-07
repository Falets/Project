class Product:
    __counter = 1

    def __init__(self, mark, break_description):
        self._mark = mark
        self._breakd = break_description
        self._id = Product.__counter
        Product.__counter += 1

    def __str__(self):
        return f"{self._mark}. {self._breakd}"

    @property
    def id(self):
        return self._id

class Computer(Product):

    def __init__(self, mark, break_description, system, date):
        super().__init__(mark, break_description)
        self._system = system
        self._date = date



    def __str__(self):
        return f"{self._mark}. {self._system}. {self._breakd}"

class Mobile(Product):

    def __init__(self, mark, break_description, system):
        super().__init__(mark, break_description)
        self._system = system



    def __str__(self):
        return f"{self._mark}. {self._system}. {self._breakd}"

class TV(Product):

    def __init__(self, mark, break_description, inches):
        super().__init__(mark, break_description)
        self._inches = inches



    def __str__(self):
        return f"{self._mark}. {self._system}. {self._breakd}"