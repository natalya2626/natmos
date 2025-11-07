# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой)
#  для работы с деньгами. В классе должны быть предусмотрены поле для 
# хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки  и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.

class Money:
    def __init__(self, whole, cents, currency):                 # конструктор init. Это метод, 
                                                                # который вызывается 
                                                                # при создании нового объекта класса Money.
        self._whole = whole                               # он принимает целую часть доллара
        self._cents = cents                               # поле для хранения центов
        self._currency = currency                         # (где currency — строка: "USD", "EUR", "UAH").

    @property                                   # свойства
    def whole(self):                            # Создаётся свойство только для чтения целой части валюты
        return self._whole         
    
    @property                                   # свойства
    def cents(self):                            # Создаётся свойство только для чтения центов копеек
        return self._cents         
    
    @property                                   # свойства
    def currency(self):                         # Создаётся свойство только для чтения типа валюты
        return self._currency   

    def __str__(self):
        return f"{self._whole}.{self._cents:02d} {self._currency}"

    def set_whole(self, value):
        if value < 0:
            raise ValueError("Whole part cannot be negative")
        self._whole = value

    def set_cents(self, value):
        if not (0 <= value < 100):
            raise ValueError("Cents must be between 0 and 99")
        self._cents = value

if __name__ == "__main__":
    money1 = Money(50, 75, "USD")
    print(money1)  # → 50.75 USD

    money1.set_cents(30)
    print(money1)  # → 50.30 USD

    money1.set_whole(100)
    print(money1)  # → 100.30 USDss