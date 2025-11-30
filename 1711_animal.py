# Создайте абстрактный класс `Animal` с абстрактным методом
# `make_sound()`. Реализуйте классы `Dog` и `Cat`, 
# унаследованные от `Animal`, и реализуйте в них метод `make_sound()`
# так, чтобы он возвращал строку `"Гав"` и `"Мяу"` соответственно.
# Напишите функцию `let_animal_speak(animal: Animal)`, которая 
# принимает объект типа `Animal` и выводит результат его метода 
# `make_sound()`. Протестируйте её на экземплярах `Dog` и `Cat`.

from abc import ABC, abstractmethod

class Animal(ABC):              # класс животное
    @abstractmethod
    def make_sound(self):        # издавать звук
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав"
    
class Cat(Animal):
    def make_sound(self):
        return "Мяу"

def let_animal_speak(animal: Animal):  # пусть животное говорит
    print(animal.make_sound())

dog = Dog() 
cat = Cat()

let_animal_speak(dog)
let_animal_speak(cat)

