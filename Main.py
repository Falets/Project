from Product import (TV, Mobile, Computer)
from Receipt import Receipt
from Workshop import Workshop
import src

def return_menu():
    while True:
        choice = input(src.Variant+src.Leave_Path)
        if choice == "1":
            check = 1
            break
        elif choice == "2":
            check = 0
            break
        else:
            print(src.User_Wrong)
    return check


def fio_input():
    name = input(src.Name)
    lastname = input(src.Lastname)
    surname = input(src.Surname)
    return name, lastname, surname

def create_tv(mark, description):
    inches = input(src.User_Inches)
    tv = TV(mark, description, inches)
    return tv

def create_mobile(mark, description):
    system = input(src.User_System)
    mobile = Mobile(mark, description, system)
    return mobile

def create_computer(mark, description):
    system = input(src.User_System)
    date = input(src.User_Date)
    computer = Computer(mark, description, system, date)
    return computer

def create_receipt(workshop, name, lastname, surname):
    while True:
        type = input(src.Variant+src.User_Type)
        mark = input(src.User_Mark)
        brdescript = input(src.User_Breakdescription)
        if type == "1":
            receipt = Receipt(create_tv(mark, brdescript), name, lastname, surname)
        elif type == "2":
            receipt = Receipt(create_computer(mark, brdescript), name, lastname, surname)
        elif type == "3":
            receipt = Receipt(create_mobile(mark, brdescript), name, lastname, surname)
        else:
            print(src.User_Wrong)
        workshop.add_receipt(receipt)
        print(receipt)
        break

def user(workshop):
    try:
        name, lastname, surname = fio_input()
        while True:
            choice = input(src.Variant+src.User_Path)
            if choice == "1":
                create_receipt(workshop, name, lastname, surname)
                if return_menu():
                    break
                else:
                    continue
            else:
                break
    except Exception as e:
        print(e)

def main():
    workshop = Workshop([], src.Password)
    while True:
        choice = input(src.Variant+src.Main_Path)
        if choice == "1":
            user(workshop)
        else:
            break

if __name__ == '__main__':
    main()