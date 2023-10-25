# Задание на класс Point3D
'''
class Point3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")

    def distance(self, a ,b):
        return b - a

    def distance2(self):
        return f'Расстояние от x до y: {self.distance(self.x, self.y)}.\nРасстояние между y и z: {self.distance(self.y, self.z)}.\n'

first = Point3D(2, 5, 8)
second = Point3D(5, 8, 7)
third = Point3D(8,7,3)
first.info()

print(first.distance2())
print(second.distance2())
'''

# Задание на нахождение площади и периметра квадрата
'''
class Square:

    def __init__(self, a=0):
        self.a = a

    def calculate_quare(self):
        return f"Площадь квадрата: {self.a ** 2}"

    def calculate_perimeter(self):
        return f"Периметр квадрата: {self.a * 4}"

first = Square(2)

print(first.calculate_quare())
print(first.calculate_perimeter())
'''

# Задание на нахождение площади и периметра треугольника
'''
class Triangle:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = (self.a ** 2 + self.b ** 2) ** (0.5)

    def calculate_quare(self):
        sin = self.c / self.a

        return f"Площадь треугольника: {((self.a * self.b)/2)*sin}"

    def calculate_perimeter(self):
        return f"Периметр треугольника: {self.a + self.b + self.c}"

tri = Triangle(3,5)
print(tri.calculate_quare())
print(tri.calculate_perimeter())
'''

# Задание вычисление расстояния между точками

'''
class Function_distance:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def point_distance(self):
        line_x = self.x2 - self.x1
        line_y = self.y2 - self.y1

        return (line_x ** 2 + line_y ** 2) ** (0.5)


first_line = Function_distance(2,4,6,9)
second_line = Function_distance(6,9,6,0)
third_line = Function_distance(2,4,6,0)

per = first_line.point_distance() + second_line.point_distance() + third_line.point_distance()

print(f"Периметр треугольника: {per}")
'''

# Задание 4
'''
class CPerson:
    # Конструктор
    def __init__(self, first_name='', last_name='', surname='', date_day='', date_moth='', date_year='', pol=''):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.date_day = date_day
        self.date_moth = date_moth
        self.date_year = date_year
        self.pol = pol

    def edit_info(self, first_name='', last_name='', surname='', date_day='', date_moth='', date_year='', pol=''):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.date_day = date_day
        self.date_moth = date_moth
        self.date_year = date_year
        self.pol = pol
    def show_info(self):
        return f'{self.first_name} {self.last_name} {self.surname}. Date of Birth: {self.date_day}.{self.date_moth}.{self.date_year}, Пол: {self.pol}.'

    # Деструктор
    def __del__(self):
        print('Object destroy')

f_n = 'Andriyanov'
l_n = 'Kirill'
s_n = 'Evgenevich'

d_d = '17'
d_m = '02'
d_y = '2006'

p = 'Men'

function = CPerson()
function.edit_info(f_n,l_n,s_n, d_d,d_m,d_y, p)

print(function.show_info())

del function
'''

# Класс Phone
'''
class Phone:
    def __init__(self, number=0, model='', weight=0):
        self.number = number
        self.model = model
        self.weight = weight

    def show_info(self):
        return f"Number: {str(self.number)}, Model: {str(self.model)}, Weight: {str(self.weight)}"

    def receiveCall(self, name=''):
        self.name = name
        return f"Звонит {self.name}"

    def getNumber(self):
        return self.number

tel_1 = Phone('+79033861243', 'Sumsung', 5)
tel_2 = Phone('+78063462345', 'Asus', 4)
tel_3 = Phone('+79053962311', 'Honor', 6)

print('Phones:')
print(tel_1.show_info())
print(tel_2.show_info())
print(tel_3.show_info())
print()
print(tel_1.receiveCall('Кирилл'))
print(tel_2.receiveCall('Артём'))
print(tel_3.receiveCall('Андрей'))
print()
print(tel_1.getNumber())
print(tel_2.getNumber())
print(tel_3.getNumber())
'''

# Класс Reader
'''
class Reader:
    def __init__(self, full_name='', number_ticket='', group='', birthday='', phone=''):
        self.full_name = full_name
        self.number_ticket = number_ticket
        self.group = group
        self.birthday = birthday
        self.phone = phone

    def takeBook(self, take_books):
        return f"{self.full_name} взял {take_books} книги."

    def returnBook(self, take_books):
        return f"{self.full_name} вернул {take_books} книги."

function = Reader('Андриянов К. Е.', '369', '315-8', '17.02.2006', '+79053961044')

print(function.takeBook(3))
print(function.returnBook(3))
'''



