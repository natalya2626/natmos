# Task 2
from datetime import datetime


class Passport:                                      # класс  паспорт 
    def __init__(
        self, number, name, surname, date_of_birth,   #   date_of_birth- дата  рождения
        place_of_birth, gender                        #  place_of_birth - место рождения
    ):
        self.number = number
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.gender = gender

    def is_valid_age(self):                                 # действителен возраст
        now = datetime.now()                                # сейчас = дата и время.сейчас()   получаем текущую дату
        year_diff = now.year - self.date_of_birth.year  # разница в годах = сейчас.год-self.дата рождения.год
        month_diff = now.month - self.date_of_birth.month  #разница за мес = сейчас.мес-self.д р.месяц
        day_diff = now.day - self.date_of_birth.day        # разница в днях = сейчас.день-self.д.р.день  ( вычисляем разницу между текущей датой и датой рождения по годам, месяцам и дням. 
        if year_diff < 18:                                  # если разница в годах < 18:  (Если прошло меньше 18 полных лет — возраст недействителен. 
            return False                                    # 
        if year_diff == 18 and month_diff < 0:              # если разница в годах== 18 и разница за мес<0:    (Если ровно 18 лет, но текущий месяц ещё раньше месяца рождения — ещё не исполнилось 18. 
            return False
        if year_diff == 18 and month_diff == 0 and day_diff < 0:  # если 18 лет, тот же месяц, но день ещё не наступил — тоже не 18. 
            return False
        return True                                         #  если все проверки пройдены — возраст 18+. 


class Visa:                                         # класс виза 
    def __init__(self, number, date_of_issue,       # date_of_issue- дата выдачи  (дейте виши)
                 date_of_expiration, country):      # date_of_expiration- дата_истечения_срока действия (дейте эксперейшен)
        self.number = number
        self.date_of_issue = date_of_issue
        self.date_of_expiration = date_of_expiration
        self.country = country


class ForeignPassport(Passport):                   # Зарубежный паспорт (форээн пАспорт)  Наследуется от Passport → содержит все поля паспорта + дополнения. 
    def __init__(
        self, number, name, surname, date_of_birth,   # конструктор принимает те же данные, что и Passport, плюс список виз
        place_of_birth, gender,
        visas: list[Visa] = []                        # список виз
    ):
        super().__init__(        # вызывает конструктор родительского класса (Passport), чтобы инициализировать общие поля. 
            number, name, surname, date_of_birth,
            place_of_birth, gender
        )
        self.visas = visas          # Сохраняет список виз. 

    def add_visa(self, date_of_issue,                   # def добавить новую визу(self, дата выдачи, дата истечения срока, страна)
                 date_of_expiration, country):
        self.visas.append(Visa(
            number=len(self.visas) + 1,
            date_of_issue=date_of_issue,
            date_of_expiration=date_of_expiration,
            country=country
        ))   # Добавляет новую визу в список. Номер визы — просто длина списка + 1. 

    def has_access(self, country):      # has_access- имеет доступ  (хаз аксэс)
        for visa in self.visas:         #  для визы в списке виз:   ? 
            if visa.country == country:    # if виза.страна == страна:
                return True
        return False
# Проверяет, есть ли у владельца виза в указанную страну. 

def can_buy_alcohol(passport):          # можно купить алкоголь (кан  бай  алкогол)
    return passport.is_valid_age()
# простая функция, которая вызывает метод is_valid_age() у объекта паспорта. 

a = Passport(                           # Создаётся объект Passport.
    123456,
    "John", "Doe",
    date_of_birth="1990-01-01",    # ❗ date_of_birth — строка "1990-01-01", а не объект datetime. 
    place_of_birth="New York",
    gender="male"                   # мужской  (мэйл)
)

foreign_passport = ForeignPassport(   # Создаётся загранпаспорт.
    number=456789,
    visas=[
        Visa(
            number=1,
            date_of_issue="2022-01-01",
            date_of_expiration="2023-01-01",
            country="USA"
        )
    ]
)

passports = [
    a,
    foreign_passport.passport
]

for passport in passports:
    print(can_buy_alcohol(passport))