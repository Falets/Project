import Product
from Receipt import Receipt
from Workshop import Workshop
import src
import datetime
import random

def FIO():
    name = input(src.name)
    lastname = input(src.lastname)
    surname = input(src.surname)
    return name, lastname, surname

def create_tv(mark, description):
    inches = input(src.user_inches)
    tv = TV(mark, description, inches)
    return tv

def create_mobile(mark, description):
    system = input(src.user_system)
    mobile = Mobile(mark, description, system)
    return mobile

def create_computer(mark, description):
    system = input(src.user_system)
    date = input(src.user_date)
    computer = Computer(mark, description, system, date)
    return computer

def create_receipt(workshop, name, lastname, surname):
    while True:
        type = input(src.user_type)
        if type == "1":
            mark = input(src.user_mark)
            brdescript = input(src.user_breakdescription)
            receipt = Receipt(create_tv(mark, brdescript), name, lastname, surname)
            workshop.add_receipt(receipt)
            print(receipt)
            break
        elif type == "2":
            mark = input(src.user_mark)
            brdescript = input(src.user_breakdescription)
            receipt = Receipt(create_computer(mark, brdescript), name, lastname, surname)
            workshop.add_receipt(receipt)
            print(receipt)
            break
        elif type == "3":
            mark = input(src.user_mark)
            brdescript = input(src.user_breakdescription)
            receipt = Receipt(create_mobile(mark, brdescript), name, lastname, surname)
            workshop.add_receipt(receipt)
            print(receipt)
            break
        else:
            print(src.user_wrong)

def user(workshop):
    try:
        name, lastname, surname = FIO()
        while True:
            choice = input(src.user_path)
            if choice == "1":
                create_receipt(workshop, name, lastname, surname)
                break
            else:
                break
    except Exception as e:
        print(e)

def main():
    workshop = Workshop([], src.password)
    while True:
        choice = input(src.main_path)
        if choice == "1":
            user(workshop)
        else:
            break

if __name__ == '__main__':
    main()