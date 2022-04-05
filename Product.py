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
