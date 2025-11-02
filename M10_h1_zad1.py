# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска,производителя, объем двигателя, 
# цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса. 
 
class Car:
    
    def __init__(
            self, model_name,year_manufacture, 
            manufacturer, engine_displacement,
            car_color, price
    ):
        self.model_name = model_name                     # название модели 
        self.year_manufacture = year_manufacture         # год выпуска
        self.manufacturer = manufacturer                 # производитель
        self.engine_displacement = engine_displacement   # объем двигателя
        self.car_color = car_color                       # цвет машины
        self.price = price                               # цена

    def input_data(self):
        self.model_name = input("Введите модель: ")
        self.year_manufacture = int(input("Введите год выпуска: "))
        self.manufacturer  = input("Производитель: ")
        self.engine_displacement = float(input("Объем двигателя: "))
        self.car_color = input("Цвет машины: ")
        self.price = float(input("Цена: "))

    def display_info(self):
        print(f"Модель: {self.model_name}")
        print(f"Год выпуска: {self.year_manufacture}")        # еаr манифакче
        print(f"Производитель: {self.manufacturer}")          # манифакчуре
        print(f"Объем двигателя: {self.engine_displacement}") # энжен дисплейсмэнт
        print(f"Цвет машины: {self.car_color}")
        print(f"Цена: {self.price}")

    def get_model(self):              # определить получить  модель(сам себя)
        return self.model_name        # возвращает self.имя модели

    def set_model(self, model):       # определить установление модели (сам себя , модель)
        self.model_name = model

    def get_year_manufacture(self):        # определить получить год выпуска (сам себя)
        return self.year_manufacture       # возвращает self.год выпуска

    def set_year_manufacture(self, year_manufacture): # определить установление год выпуска (сам себя , год выпуска)
        self.year_manufacture = year_manufacture 

    def get_manufacturer(self):         # определить получить производителя(сам себя)
        return self.manufacturer        # возвращает self.производитель

    def set_manufacturer(self, manufacturer): # определить установление производителя (сам себя , )
        self.manufacturer = manufacturer

    def get_engine_displacement(self):        # определить получить объем двигателя(сам себя)
        return self.engine_displacement       # возвращает self.объем двигателя

    def set_engine_displacement(self, engine_displacement): # определить установление объема двигателя (сам себя , объем двигателя)
        self.engine_displacement =  engine_displacement  

    def get_car_color(self):              # определить получить цвет машины(сам себя)
        return self.car_color             # возвращает self.цвет машины

    def set_car_color(self, car_color):   # определить установление цвета машины (сам себя , цвет машины)
        self.car_color = car_color

    def get_price(self):              # определить получить цена (сам себя)
        return self.price             # возвращает self. цена

    def set_price(self, price):       # определить установление цена (сам себя , цена)
        self.price = price

# После определения класса можно создать объект и протестировать его:    
car = Car("", 0, "", 0.0, "", 0.0)     # заглушка
car.input_data()
car.display_info()    