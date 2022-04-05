from Product import Product

class Computer(Product):

    def __init__(self, mark, break_description, system, date):
        super().__init__(mark, break_description)
        self._system = system
        self._date = date



    def __str__(self):
        return f"{self._mark}. {self._system}. {self._breakd}"

