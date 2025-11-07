# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.

class Ship:                                         # класс корабль
    def __init__(self, displacement, load_capacity, speed, strength, controllability):  #  конструктор init. Это метод, который вызывается 
                                                    #  при создании нового объекта класса Ship.
        self._displacement = displacement           # он принимает водоизмещение
        self._load_capacity = load_capacity         # грузоподъёмность
        self._speed = speed                         # скорость
        self._strength = strength                   # прочность
        self._controllability = controllability     # управляемость

    @property                                       # свойства
    def displacement(self):                         # Создаётся свойство только для чтения водоизмещения
        return self._displacement 

    @property                                       #  свойства
    def load_capacity(self):                        # Создаётся свойство только для чтения грузоподъемности
        return self._load_capacity 

    @property                                       #  свойства
    def speed(self):                                # Создаётся свойство только для чтения скорости
        return self._speed       

    @property                                       #  свойства
    def strength(self):                                # Создаётся свойство только для чтения прочности
        return self._strength          
    
    @property                                       #  свойства
    def controllability(self):                      # Создаётся свойство только для чтения управляемости
        return self._controllability          
    
    def __str__(self):
        return f"Ship: {self._displacement}, {self._load_capacity},{self._speed}, {self._strength}, {self._controllability}"    
    
class Frigate(Ship):
    def __init__(self, displacement, load_capacity, speed, strength, controllability, escort_other_vessels):
        super().__init__(displacement, load_capacity, speed, strength, controllability)
        self._escort_other_vessels = escort_other_vessels    # эскорт других судов

    def protection_of_sea_communications(self):          # охрана морских коммуникаций
        print(f"Охраняю морские коммуникации: '{self._escort_other_vessels}'...")  

class Destroyer(Ship):                                  # класс эсминец  дистроя
    def __init__(self, displacement, load_capacity, speed, strength, controllability, anti_submarine_capability):
        super().__init__(displacement, load_capacity, speed, strength, controllability)
        self._anti_submarine_capability = anti_submarine_capability  #   противолодочная  способность      
    
    def anti_submarine_warfare(self):                   # борьба с подводными лодками  
        print(f"Веду борьбу c подводными лодками. Способность: {self._anti_submarine_capability}")

    

class Cruiser(Ship): 
    def __init__(self, displacement, load_capacity, speed, strength, controllability, defense_formations_warships_convoys_ships):
        super().__init__(displacement, load_capacity, speed, strength, controllability) 
        self._defense_formations_warships_convoys_ships = defense_formations_warships_convoys_ships
        # оборона соединений боевых кораблей и конвоев судов

    def fight_against_the_enemy_fleet(self):      # борьба с флотом противника   
       print(f"Атакую вражеский флот для защиты наших соединений: '{self._defense_formations_warships_convoys_ships}'...")  


if __name__ == "__main__":
    frigate = Frigate(3000, 500, 30, 80, 90, "конвой A1")
    frigate.protection_of_sea_communications()
    print(frigate)

    destroyer = Destroyer(7000, 800, 35, 90, 85, "Высокая")
    destroyer.anti_submarine_warfare()
    print(destroyer)

    cruiser = Cruiser(12000, 2000, 32, 95, 80, "Флотская группа Альфа")
    cruiser.fight_against_the_enemy_fleet()
    print(cruiser) 