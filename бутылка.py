# Чпсть 1  импорт
from datetime import datetime, timedelta
# datetime — позволяет работать с датами и временем
# timedelta — показывает разницу между двумя датами (например, «3 дня»)
# random — генерирует случайные числа (используется для создания тестовых данных)
import random

#  Часть 2: Класс BottleProduct (базовый класс)
class BottleProduct:  # Объявляется класс BottleProduct («продукт в бутылке»).
    tax = 0.22        # переменная класса (налог 22% для всех товаров этого типа).
    def __init__(self, volume, price, brand, expiration_date: datetime):   # конструктор
        self.price = price                                      # базовая цена,
        self.volume = volume                                    # объём (в мл или л),
        self.brand = brand                                      # бренд
        self.expiration_date = expiration_date #дата окончания срока годности (обязательно укажите объект datetime). 

# Метод: сколько осталось до истечения срока    
    def time_until_expiration(self):   # Возвращает оставшееся время до истечения срока годности.
        if self.expiration_date <= datetime.now():
            return timedelta(0)     # Если срок уже истёк → возвращается timedelta(0) (нулевой интервал).
        return self.expiration_date - datetime.now() #  В противном случае — разницу между датой окончания 
                                                     #   и текущим моментом.

# Метод: итоговая цена с учётом налога   
    def get_final_price(self):
        return self.price * (1 + self.tax)   # Базовая цена увеличивается на 22 % (1 + 0.22 = 1.22).  

# Часть 3: Класс AlcoholProduct (наследник)          
class AlcoholProduct(BottleProduct):      # Наследует всё от BottleProduct, но добавляет специфику алкоголя.
    def __init__(self, volume, price, brand, expiration_date: datetime, alcohol_volume_percentage):# конструтор
        super().__init__(volume, price, brand, expiration_date) # Вызывает конструктор родительского класса
                                                                #(super().__init__) для установки общих полей.
        self.alcohol_volume_percentage = alcohol_volume_percentage                    
        # Добавляет новое поле: alcohol_volume_percentage — крепость (в процентах, например, 40%).

# Переопределённый метод цены:
    def get_final_price(self):
        return (
            super().get_final_price() +      #  Сначала берётся цена с налогом из родительского класса.
            self.alcohol_volume_percentage * # Затем добавляется надбавка:alcohol_volume_percentage * price
            self.price
        )
#  Важно: если alcohol_volume_percentage = 40, то надбавка = 40 × price — это очень много!
# Возможно, имелось в виду деление на 100 (например, 0.4 * price), но в коде указано именно так.
#  Это может быть намеренно упрощено для демонстрации наследования и переопределения методов.  

# Часть 4: Класс CashRegister (кассовый аппарат)
class CashRegister:                 # Создаётся касса.
    def __init__(self, products):   # Несмотря на параметр products, внутри всегда создаётся
                                    # пустой список _products.
                                    # (Параметр products не используется — возможно, 
                                    # это опечатка, но не критично.)
        self._products = []  

 #   Метод добавления товара:
    def add_product(self, product):
        self._products.append(product)  # Просто добавляет товар в список.

# Метод оплаты (checkout):    # чекаут
    def checkout(self):
        total = 0             # Инициализирует итоговую сумму.