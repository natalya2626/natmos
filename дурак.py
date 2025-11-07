class Card:                     # создается  класс  с именем карта 
    CLUBS = "Clubs"                  # трефы  клубы        #  константы  мастей
    DIAMONDS = "Diamonds"            # буби  алмазы
    HEARTS = "Hearts"                # черви  сердца
    SPADES = "Spades"                # пики  пики

    def __init__(self, suit, rank: int):  #  конструктор init. Это метод, который вызывается 
        #  при создании нового объекта класса Card.
        self._suit = suit   #  он принимает масть
        self._rank = rank   #  достоинство карты (целоe число например 10)

    @property         #  свойства
    def suit(self):   # Создаётся свойство только для чтения масти
        return self._suit

    @property
    def rank(self):             # создается свойство только для чтения достоинства карты
        return self._rank

    def is_superior(self, other: 'Card'):  #  метод сравнения по старшинству
        return (                          # Метод проверяет, старше ли текущая карта (self) другой карты (other)

            self.suit == other.suit and
            self.rank > other.rank
        )

    def __eq__(self, other: 'Card'):  #  метод сравнения на равенство
        return (
            self.suit == other.suit and
            self.rank == other.rank
        )

    def __str__(self):             # Определяет, что будет выведено, если вывести карту через print() 
                                   # или преобразовать её в строку
        return f"{self.rank} of {self.suit}"


card1 = Card(Card.CLUBS, 10)  # создание объекта 
# Создаётся экземпляр класса Card:

# масть — Card.CLUBS → "Clubs"  трефы
# достоинство — 10
# Объект card1 теперь хранит эти данные
print(card1.suit)