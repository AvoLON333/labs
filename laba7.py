class Employee:
    def __init__(self, name, empl_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.empl_id = empl_id

    def get_info(self):
        return f"Id: {self.empl_id}, Имя: {self.name}"

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department
        self.team = []

    def manage_project(self):
        return f"Менеджер: {self.name} управляет проектом в отделе {self.department}"

    def get_info(self):
        return f"{super().get_info()}, Статус: Менеджер, Отдел: {self.department}"

class Technician(Employee):
    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник: {self.name}, обслуживает по специальности {self.specialization}"

    def get_info(self):
        return f"{super().get_info()}, Статус: Техник, Специализация: {self.specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, empl_id, department, specialization):
        super().__init__(name=name, empl_id = empl_id, department=department, specialization=specialization)

    def perform_maintenance(self):
        return f"Технический сотрудник {self.name}, обслуживает в специализации {self.specialization}"

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.department}"

    def add_employee(self, employee):
        if employee not in self.team:
            self.team.append(employee)
            return f"Сотрудник {employee.name} присоединяется к {self.name}"
        else:
            return f"Сотрудник {employee.name} уже присоединился к {self.name}"

    def get_team_info(self):
        if not self.team:
            return f"У технического менеджера {self.name} отсутствуют подчинённые"
        team_info = [f"Команда {self.name}",
                     f"Кол-во сотрудников: {len(self.team)}"]
        for i, team in enumerate(self.team, 1):
            team_info.append(f" {i}. {team.get_info()}")
        return team_info

print("__Class Employee__")

empl1 = Employee("Александр Демченко", "FF334")
print(f"Сотрудник: {empl1.get_info()}")

print("__Class Manager__")

mng1 = Manager (name ="Максим Скибин", empl_id = "OO223", department="Производственный отдел")
print(f"Менеджер: {mng1.get_info()}")
print(f"Обязанность: {mng1.manage_project()}")

#CLASS TECHNICIAN

print("__Class Technician__")
tch1 = Technician(name ="Виктор Орехов", empl_id ="QQ322", specialization="Связь")
print(f"Техник: {tch1.get_info()}")
print(f"Операция: {tch1.perform_maintenance()}")

#CLASS TechManager

print("__Class TechManager__")
tech_mgr1 = TechManager( name="Максим Кириллов", empl_id ="CH232", department="Технический отдел", specialization="Безопасность")
print(f"Технический менеджер: {tech_mgr1.get_info()}")
print(f"Операция 1: {tech_mgr1.manage_project()}")
print(f"Операция 2: {tech_mgr1.perform_maintenance()}")

tech_mgr1.add_employee(tch1)
tech_mgr1.add_employee(empl1)
print(tech_mgr1.get_team_info())

employees = [
    Employee(name="Сергей Нечаев", empl_id="TT881"),
    Manager(name ="Василий Шолохов", empl_id="AA213",department= "Разработка"),
    Technician(name="Илья Доманин",empl_id= "FFF123", specialization="Мониторинг"),
    tech_mgr1
]

print("Информация о сотрудниках")
for i, employee in enumerate(employees, 1):
    print(f"{i}. {employee.get_info()}")






