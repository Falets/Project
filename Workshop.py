from Admin import Admin

class Workshop:
    def __init__(self, receipt_names: list, admin_list: list):
        self.__receipt = {receipt.id: receipt for receipt in receipt_names}
        self.__admin_list = admin_list

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

    def all_admins(self):
        for admin in self.__admin_list:
            print(admin)

    def add_admin(self, login, password):
        for admin in self.__admin_list:
            if admin.login == login:
                print("login занят")
                break
        else:
            self.__admin_list.append(Admin(login, password))

    def delete_admin(self, login):
        for admin in self.__admin_list:
            if admin.login == login:
                self.__admin_list.remove(admin)

    def get_admin(self, login):
        for admin in self.__admin_list:
            if admin.login == login:
                return admin

    @property
    def admin_list(self):
        return self.__admin_list