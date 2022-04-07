import Product
import datetime
import random

class Receipt:
    __status = {1: "Ремонтируется", 2: "Готово", 3: "Выдано клиенту"}

    def __init__(self, product, name, lastname, surname):
        self._id = product.id
        self._product = product
        self._acceptdate = datetime.date.today()
        self._name = name
        self._lastname = lastname
        self._surname = surname
        self._status = 1
        self._dateofissue = datetime.date.today() + datetime.timedelta(days=random.randint(1, 6))

    def __str__(self):
        return f"Номер квитанции: {self._id}. Тип техники: {self._product.__class__.__name__}. " \
               f"{self._product.__str__()}\n" \
               f"Дата сдачи: {self._acceptdate}. Дата выдачи: {self._dateofissue}. " \
               f"ФИО: {self._name} {self._lastname} {self._surname}. Статус: {Receipt.__status[self._status]}"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def lastname(self):
        return self._lastname

    @property
    def surname(self):
        return self._surname