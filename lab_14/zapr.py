import sqlite3
print("запрос 1-------------\n")
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()
query = """
SELECT Books.Title, Books.Price, Authors.FirstName, Authors.LastName
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

print("запрос 2-------------\n")
query = """
SELECT Orders.OrderID, Orders.OrderDate, Books.Title, OrderItems.Quantity
FROM Orders
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Books ON OrderItems.BookID = Books.BookID
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

print("запрос 3-------------\n")
query = """
SELECT Orders.OrderID, SUM(Books.Price * OrderItems.Quantity) AS Total
FROM Orders
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Books ON OrderItems.BookID = Books.BookID
GROUP BY Orders.OrderID
"""
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()