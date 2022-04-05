from Product import Product

class TV(Product):

    def __init__(self, mark, break_description, inches):
        super().__init__(mark, break_description)
        self._inches = inches



    def __str__(self):
        return f"{self._mark}. {self._system}. {self._breakd}"