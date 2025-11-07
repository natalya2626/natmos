# Часть 1  импорт
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
        if self.expiration_date <= datetime.now():  # дата оконч срока <= дата и время сейчас
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
        self._products.append(product)        # Просто добавляет товар в список.

# Метод оплаты (checkout):                    # чекаут  проверить
    def checkout(self):
        total = 0                             # Инициализирует итоговую сумму покупки
        products_to_sell = (                  # продукты продать
            item for item in self._products                   # элемент для элемент в сам себя._продукты
            if item.time_until_expiration() > timedelta(0)    # если элемент.время до истечения срока()> delta времени(0)
        )
   #   Создаёт генератор только тех товаров, у которых не истёк срок годности
   #(time_until_expiration() > 0 → значит, ещё можно продать).
     
        for product in products_to_sell:            #  для продукт в  продукты продать:
            print('Продаваемый товар: ', product.brand)
            final_price = product.get_final_price()
            print('Цена: ', final_price)
            total += final_price
 # Для каждого годного товара:
    # Печатает бренд,
    # Вычисляет итоговую цену (с налогом и, возможно, надбавкой)
    # Добавляет к общей сумме.

        self._products.clear()           # Очищает список товаров после продажи.  
        return total                     # Возвращает итоговую сумму.
    
# Создание тестовых данных    
register = CashRegister([])              # Создаётся пустая касса
for _ in range(5):
    # Цикл выполнится 5 раз → будет добавлено 10 товаров: 5 обычных + 5 алкогольных.

# Добавление обычного товара:   
    register.add_product(                               # регистр.добавить_продукты
        BottleProduct(                                  # бутилированный продукт 
            volume=random.randint(1, 100),              # Объём: случайное число от 1 до 100.
            price=random.randint(1, 100),               # Цена: от 1 до 100.
            brand=f"Brand {random.randint(1, 100)}",    # Бренд: "Brand X", где X — случайное число
            expiration_date=(                           # дата окончания срока
                datetime.now() +                        # дата и время сейчас
                timedelta(days=random.randint(-3, 30))  # показывает разницу между двумя датами
            ),
        )
    )
# Срок годности: от 3 дней назад до 30 дней вперёд → срок годности некоторых товаров истек.

# Добавление алкогольного товара:
    register.add_product(
        AlcoholProduct(
            volume=random.randint(1, 100),
            price=random.randint(1, 100),
            brand=f"Alco Brand {random.randint(1, 100)}",
            expiration_date=(
                datetime.now() +
                timedelta( 
                    days=random.randint(-3, 30),
                )
            ),

            alcohol_volume_percentage=random.randint(1, 100),
        )
    )
# Аналогично, но с крепостью от 1 % до 100 %.

# Окончательный расчёт
total_price = register.checkout()                       # весь прайс = регистр.проверить()
# Вызывается способ оплаты:
# Товары с истекшим сроком годности игнорируются.
# Для остальных печатается информация и суммируется стоимость.
print(f'Итоговая сумма: {total_price:.2f} руб.')

