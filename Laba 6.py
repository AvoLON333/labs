"""class UserAccount():
    def __init__(self , username , email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password
        return "Пороль изменён"

    def check_password(self, password_to_check):
        if self.password == password_to_check:
            return True
        else:
            return False

user = UserAccount(username = "admin", email = "id@da231.com", password = "123")

#Начальный пароль
print(f"Проверка пароля: {user.check_password(str('123'))}")
print(f"Проверка пароля: {user.check_password(str('999'))}")


#Смена пороля

user.set_password("322")
print(f"Проверка старого пороля: {user.check_password(str('123'))}")
print(f"Проверка нового пороля: {user.check_password(str('322'))}")"""


class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"{self.make} {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f"{self.make} {self.model} {self.fuel_type}"

car1 = Car("McLaren", "F1", "Бензин")
print(car1.get_info())
car2 = Car("Tesla", "Modul S", "Электричество")
print(car2.get_info())











