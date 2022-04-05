from Product import Product
from Mobile import Mobile
from TV import TV
from Computer import Computer
from Receipt import Receipt
import datetime
import random


class Workshop:
    def __init__(self, receipt_names: list, password):
        self.__receipt = {receipt.id: receipt for receipt in receipt_names}
        self.__password = password

    def add_receipt(self, new_receipt):
        self.__receipt.update({new_receipt.id: new_receipt})

    def remove_receipt(self, receipt_id):
        self.__receipt.pop(receipt_id)

    def get_receipt(self, receipt_id):
        return self.__receipt[receipt_id]

    def get_receipt_fio(self, name, lastname, surname):
        receipt_names_fio = []
        for receipt in self.__receipt.values():
            if receipt.name == name and receipt.lastname == lastname and receipt.surname == surname:
                receipt_names_fio.append(receipt)
        return receipt_names_fio

    def check_password(self, password):
        if password == self.__password:
            return True
        return False