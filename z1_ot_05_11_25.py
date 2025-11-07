# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте класс  CoffeeMachine
# (содержит информацию о кофемашине), класс Blender  (содержит информацию
#  о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

class Device:                                      #  класс изобретение
    def __init__(self, operating_manual, passport, has_grinding_function):  #  конструктор init. Это метод, который вызывается 
                                                    #  при создании нового объекта класса Devise.
        self._operating_manual = operating_manual   # он принимает руководство по эксплуатации
        self._passport = passport                   # паспорт
        self._has_grinding_function = has_grinding_function    # размолоть 

    @property                                      #  свойства
    def operating_manual(self):                    # Создаётся свойство только для чтения руководства по эксплуатации
        return self._operating_manual    

    @property
    def passport(self):                                     # создается свойство только для чтения паспорта
        return self._passport
    
    def __str__(self):
        return f"Device: {self._operating_manual}, {self._passport}"    

class CoffeeMachine(Device):                                    # класс  кофемашина
    def __init__(self, operating_manual, passport, has_grinding_function, brew_type):
        super().__init__(operating_manual, passport, has_grinding_function)
        self._brew_type = brew_type

    def brew_coffee(self):                                   # метод заварить кофе
        print(f"Завариваю кофе типа '{self._brew_type}'...")  
     
class Blender(Device):                                           # класс блендер
    def __init__(self, operating_manual, passport, has_grinding_function, volume):
        super().__init__(operating_manual, passport, has_grinding_function)
        self._volume = volume                 
 
    def blend(self):                                      # метод   смесь
        print(f"Взбиваю смесь в чаше объёмом {self._volume} л...")    

class MeatGrinder(Device):                                       # класс мясорубка
    def __init__(self, operating_manual, passport, has_grinding_function, power):
        super().__init__(operating_manual, passport, has_grinding_function)
        self._power = power                                       # мощность

    def make_minced_meat(self):
        print(f"Делаю фарш... Мощность: {self._power} Вт")

if __name__ == "__main__":
    coffee_machine = CoffeeMachine("Инструкция CM-100", "Паспорт CM-100", True, "Эспрессо")
    blender = Blender("Инструкция BL-200", "Паспорт BL-200", False, 2.0)
    meat_grinder = MeatGrinder("Инструкция MG-300", "Паспорт MG-300", True, 800)

    print(coffee_machine)
    coffee_machine.brew_coffee()

    print(blender)
    blender.blend()

    print(meat_grinder)
    meat_grinder.make_minced_meat()
