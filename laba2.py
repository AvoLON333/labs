#1
def greet(name):
    print(f"Привет, {name}")
greet("Сергей")

def square(number):
    return number * number
print(f"Квадрат числа 7: {square(7)}")

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
print(f"{max_of_two(3, 2)}")


#2
def describe_person(name, age=30):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
describe_person("Сергей")


a = int(input("Enter a number: "))
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True
print(is_prime(a))






