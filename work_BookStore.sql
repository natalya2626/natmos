sqlite3 BookStore.db
PRAGMA foreign_keys = ON;
CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL CHECK (FirstName != ''),
    LastName TEXT NOT NULL CHECK (LastName != ''));


CREATE TABLE Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL CHECK (Title != ''),
    AuthorID INTEGER NOT NULL, 
    Price REAL NOT NULL,
    FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID) 
);

INSERT INTO Authors (FirstName, LastName) VALUES ('Лев', 'Толстой');
INSERT INTO Books (Title, AuthorID, Price) VALUES ('Война и мир', 1, 599.99);

-- Экспорт ДО удаления
.mode csv
.headers on
.output authors_before.csv
SELECT * FROM Authors;
.output books_before.csv
SELECT * FROM Books;

-- Удаление данных
DELETE FROM Books;
DELETE FROM Authors;

-- Экспорт ПОСЛЕ удаления
.output authors_after.csv
SELECT * FROM Authors;
.output books_after.csv
SELECT * FROM Books;

-- (опционально) вернуть вывод в консоль
.output stdout