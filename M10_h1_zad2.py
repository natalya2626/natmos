# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:

    def __init__(
        self, book_title, year_of_manufacture, publisher, 
        genre, author, price
    ):
        self.book_title = book_title                     # название книги 
        self.year_of_manufacture = year_of_manufacture   # год выпуска
        self.publisher = publisher                       # издатель
        self.genre = genre                               # жанр
        self.author = author                             # автор
        self.price = price                               # цена

    def input_data(self):
        self.book_title = input("наз ")
        self.year_of_manufacture = int(input("г "))
        self.publisher  = input("И ")
        self.genre = (input("Ж: "))
        self.author = input("А: ")
        self.price = float(input("Ц: "))    

    def display_info(self):
        print(f"Название книги: {self.book_title}")           # название книги
        print(f"Год выпуска: {self.year_of_manufacture}")     # еаr манифакче  год выпуска 
        print(f"Издатель: {self.publisher}")                  # издатель
        print(f"Жанр: {self.genre}")                          # жанр жанрэ
        print(f"Автор: {self.author}")                        # автор
        print(f"Цена: {self.price}")                          # цена

    def get_book(self):                         # определить получить книгу (сам себя):   
        return self.book_title                  # вернуть self. название книги
    
    def set_book(self, book):                   # определить установить книга(сам себя, книга):
        self.book_title = book_title            # self.название книги = название книги

    def get_year_of_manufacture(self):          # определить получить год выпуска(сам себя):   
        return self.year_of_manufacture         # вернуть self.год выпуска
    
    def set_year_of_manufacture(self, year_of_manufacture):# определить установить год выпуска(self, год вып):
        self.year_of_manufacture = year_of_manufacture     # self.год вып = год выпуска

    def get_publisher(self):                    # определить получить издатель(сам себя):   
        return self.publisher                   # вернуть self.издатель
    
    def set_publisher(self, publisher):         # определить установить издатель(self, издатель):
        self.publisher = publisher              # self.издатель = издатель    

    def get_genre(self):                    # определить получить жанр(сам себя):   
        return self.genre                   # вернуть self.жанр
    
    def set_genre(self, genre):             # определить установить жанр(self, жанр):
        self.genre = genre                  # self.жанр = жанр      

    def get_author(self):                    # определить получить автор(сам себя):   
        return self.author                   # вернуть self.автор
    
    def set_author(self, author):             # определить установить автор(self, автор):
        self.author = author                  # self.автор = автор          

    def get_price(self):                    # определить получить цену(сам себя):   
        return self.price                   # вернуть self.цена
    
    def set_price(self, price):             # определить установить цену(self, цена):
        self.price = price                  # self.цена = цена  

# После определения класса можно создать объект и протестировать его:    
book = Book("", 0, "", "", "", 0.0)     # заглушка
book.input_data()
book.display_info()    
