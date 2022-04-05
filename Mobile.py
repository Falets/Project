from Product import Product

class Mobile(Product):

    def __init__(self, mark, break_description, system):
        super().__init__(mark, break_description)
        self._system = system



    def __str__(self):
        return f"{self._mark}. {self._system}. {self._breakd}"

