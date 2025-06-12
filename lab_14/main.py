import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
""")

cursor.executescript("""
CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Biography TEXT
);

CREATE TABLE Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT,
    Price REAL,
    AuthorID INTEGER,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT,
    Status TEXT
);

CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    BookID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);
""")

cursor.executescript("""
INSERT INTO Authors VALUES
(1, 'Джордж', 'Оруэлл', 'Английский писатель и журналист, автор "1984"'),
(2, 'Рэй', 'Брэдбери', 'Американский писатель-фантаст'),
(3, 'Айзек', 'Азимов', 'Американский писатель научной фантастики'),
(4, 'Агата', 'Кристи', 'Королева детектива');

INSERT INTO Books VALUES
(1, '1984', 450.00, 1),
(2, 'Фаренгейт 451', 420.00, 2),
(3, 'Я, Робот', 550.00, 3),
(4, 'Убийство в Восточном экспрессе', 600.00, 4),
(5, 'Вино из одуванчиков', 380.00, 2),
(6, 'Основание', 700.00, 3),
(7, 'Смерть на Ниле', 650.00, 4);

INSERT INTO Orders VALUES
(1, '2025-06-10', 'Доставлен'),
(2, '2025-06-12', 'В обработке'),
(3, '2025-06-13', 'Отменён');

INSERT INTO OrderItems VALUES
(1, 1, 1, 1),
(2, 1, 3, 2),
(3, 2, 2, 1),
(4, 2, 5, 1),
(5, 3, 7, 1);
""")

conn.commit()
cursor.close()
conn.close()
