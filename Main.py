from Product import (TV, Mobile, Computer)
from Receipt import Receipt
from Workshop import Workshop
from Admin import Admin
import src

def return_menu():
    while True:
        choice = input(src.VARIANT+src.LEAVE_PATH)
        if choice == "1":
            check = 1
            break
        elif choice == "2":
            check = 0
            break
        else:
            print(src.USER_WRONG)
    return check


def fio_input():
    name = input(src.NAME)
    lastname = input(src.LASTNAME)
    surname = input(src.SURNAME)
    return name, lastname, surname

def create_tv(mark, description):
    inches = input(src.USER_INCHES)
    tv = TV(mark, description, inches)
    return tv

def create_mobile(mark, description):
    system = input(src.USER_SYSTEM)
    mobile = Mobile(mark, description, system)
    return mobile

def create_computer(mark, description):
    system = input(src.USER_SYSTEM)
    date = input(src.USER_DATE)
    computer = Computer(mark, description, system, date)
    return computer

def create_receipt(workshop, name, lastname, surname):
    while True:
        type = input(src.VARIANT+src.USER_TYPE)
        mark = input(src.USER_MARK)
        brdescript = input(src.USER_BREAKDESCRIPTION)
        if type == "1":
            receipt = Receipt(create_tv(mark, brdescript), name, lastname, surname)
        elif type == "2":
            receipt = Receipt(create_computer(mark, brdescript), name, lastname, surname)
        elif type == "3":
            receipt = Receipt(create_mobile(mark, brdescript), name, lastname, surname)
        else:
            print(src.USER_WRONG)
        workshop.add_receipt(receipt)
        print(receipt)
        break

def show_info(workshop, name, lastname, surname):
    while True:
        path_info = input(src.VARIANT+src.ID_FIO_INFO)
        if path_info == "1":
            info_1 = int(input(src.ID_INFO))
            receipt = workshop.get_receipt(info_1)
            if receipt.name == name and receipt.lastname == lastname and receipt.surname == surname:
                print(receipt)
            else:
                print(src.CANNOT_SHOW)
        elif path_info == "2":
            for receipts in workshop.get_receipt_fio(name, lastname, surname):
                print(receipts)
        else:
            print(src.USER_WRONG)
        break

def user(workshop):
    try:
        name, lastname, surname = fio_input()
        while True:
            choice = input(src.VARIANT+src.USER_PATH)
            if choice == "1":
                create_receipt(workshop, name, lastname, surname)
                if return_menu():
                    break
                else:
                    continue
            elif choice == "2":
                show_info(workshop, name, lastname, surname)
                if return_menu():
                    break
                else:
                    continue
            else:
                break
    except Exception as e:
        print(e)

def check_info(workshop, login, password):
    for admin in workshop.admin_list:
        if admin.login == login and admin.password == password:
            return True
    else:
        return False

def operations_with_admins(workshop):
    while True:
        path_info = input(src.VARIANT+src.ADMIN_ADMINS)
        if path_info == "1":
            workshop.all_admins()
        elif path_info == "2":
            login1 = input(src.ADMIN_LOGIN)
            workshop.delete_admin(login1)
        elif path_info == "3":
            login1 = input(src.ADMIN_LOGIN)
            password = input(src.ADMIN_PASSWORD)
            workshop.add_admin(login1, password)
        else:
            print(src.USER_WRONG)
        break

def operations_with_receipts(workshop, login):
    while True:
        path_info = input(src.VARIANT+src.ADMIN_RECEIPT)
        if path_info == "1":
            admin = workshop.get_admin(login)
            number_receipt = int(input(src.ADMIN_RECEIPT_NUMBER))
            status = int(input(src.ADMIN_RECEIPT_STATUS))
            admin.change_status(workshop, number_receipt, status)
        elif path_info == "2":
            admin = workshop.get_admin(login)
            number_receipt = int(input(src.ADMIN_RECEIPT_NUMBER))
            dateofissue = input(src.ADMIN_RECEIPT_NEW_DATE)
            admin.change_date(workshop, number_receipt, dateofissue)
        elif path_info == "3":
            number_receipt = int(input(src.ADMIN_RECEIPT_NUMBER))
            print(workshop.get_receipt(number_receipt))
        else:
            print(src.USER_WRONG)
        break

def admin(workshop):
    try:
        login = input(src.ADMIN_LOGIN)
        password = input(src.ADMIN_PASSWORD)
        if check_info(workshop, login, password):
            while True:
                choice = input(src.VARIANT + src.ADMIN_PATH)
                if choice == "1":
                    operations_with_admins(workshop)
                    if return_menu():
                        break
                    else:
                        continue
                elif choice == "2":
                    operations_with_receipts(workshop, login)
                    if return_menu():
                        break
                    else:
                        continue
        else:
            print("Неправильный login или пароль")
    except Exception as e:
        print(e)

def main():
    workshop = Workshop([], [Admin("admin", "123")])
    while True:
        choice = input(src.VARIANT+src.MAIN_PATH)
        if choice == "1":
            user(workshop)
        elif choice == "2":
            admin(workshop)
        else:
            break

if __name__ == '__main__':
    main()