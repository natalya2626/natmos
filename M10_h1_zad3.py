# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:                                           # класс Стадион  
                           
    def __init__(
        self, name_stadium, opening_date, country, 
        city, capacity
    ):
        self.name_stadium = name_stadium                 # название стадиона 
        self.opening_date = opening_date                 # дата открытия
        self.country = country                           # страна
        self.city = city                                 # город
        self.capacity = capacity                         # вместимость  капАсати
     
    def input_data(self):
        self.name_stadium = input("Н: ")                 # название стадиона 
        self.opening_date = input("Д о: ")               # дата открытия
        self.country = input("С: ")                      # страна
        self.city = input("Г: ")                         # город
        self.capacity = int(input("В: "))                # вместимость 

    def display_info(self):    
        print(f"Название стадиона: {self.name_stadium}")  
        print(f"Дата открытия: {self.opening_date}")  
        print(f"Страна: {self.country}")  
        print(f"Город: {self.city}")  
        print(f"Вместимость: {self.capacity}")  

    def get_stadium(self):                            # определить получить стадион (сам себя):   
        return self.name_stadium                      # вернуть self.название стадиона
    
    def set_stadium(self, stadium):                   # определить установить стадион(сам себя, стадион):
        self.name_stadium = stadium              # self.название стадиона = название стадиона   

    def get_opening_date(self):                       # определить получить дата открытия (сам себя):   
        return self.opening_date                      # вернуть self.дата открытия
    
    def set_opening_date(self, opening_date):   # определить установить дата открытия(сам себя, д открытия):
        self.opening_date = opening_date        # self.дата открытия = дата открытия
    
    def get_country(self):                       # определить получить страна(сам себя):   
        return self.country                      # вернуть self.страна
    
    def set_country(self, country):           # определить установить страна(сам себя, страна):
        self.country = country                # self.страна = страна

    def get_city(self):                      # определить получить город (сам себя):   
        return self.city                     # вернуть self.город
    
    def set_city(self, city):         # определить установить город(сам себя, город):
        self.city = city              # self.город = город
    
    def get_capacity(self):                      # определить получить вместимость (сам себя):   
        return self.capacity                     # вернуть self.вместимость
    
    def set_capacity(self, capacity):         # определить установить вместимость(сам себя, вместимость):
        self.capacity = capacity              # self.вместимость = вместимость

    
# После определения класса можно создать объект и протестировать его:           
stadium=Stadium("", "", "", "", "")          # заглушка
stadium.input_data()  
stadium.display_info()     
