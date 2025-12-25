class Book():
    """Описание книги"""
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        """Возвращение информации о книге"""
        print("Книга под названием" + self.title  + "под авторством" + " " + self.author + " " + "написана в" + " " + str(self.year) + " " + "году")
Book1 = Book(" 'Преступление и наказание' ", "Ф.М.Достоевский", 1866)
Book2 = Book("Война и мир", "Л.Н.Толстой", 1867)

Book1.get_info()


class Circle():
    """Радиус"""
    def __init__(self, radius):
        self.radius = radius
    """Возвращение значения радиуса"""
    def get_radius(self):
        return self.radius
    """Изменение радиуса"""
    def set_radius(self,new_radius):
        self.radius = new_radius
"""Новое значение"""
class Circle1(Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius
Cr1 = Circle(10)
print(Cr1.get_radius())
Cr1.set_radius(40)
print(Cr1.get_radius())







