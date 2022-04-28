class Admin:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    def __str__(self):
        return f"Login: {self.login}. Password: {self.password}"

    def change_status(self, workshop, number_receipt, number_status):
        receipt = workshop.get_receipt(number_receipt)
        receipt._status = number_status

    def change_date(self, workshop, number_receipt, new_date):
        receipt = workshop.get_receipt(number_receipt)
        receipt._dateofissue = new_date