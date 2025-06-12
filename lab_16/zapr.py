import sqlite3
from pypika import Query, Table, functions as fn

print("\nзапрос 1 ----------------\n")
conn = sqlite3.connect('books.db')
cur = conn.cursor()

books = Table('books')
ratings = Table('ratings')

q = Query.from_(books).join(ratings).on(books.id == ratings.book_id).select(books.title, books.price, ratings.rating)
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)

print("\nзапрос 2 ----------------\n")

q = Query.from_(books).join(ratings).on(books.id == ratings.book_id).select(books.title, ratings.rating).where(ratings.rating == 5)
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)

print("\nзапрос 3 ----------------\n")

q = Query.from_(books).select(fn.Avg(books.price).as_("avg_price"))
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)
print("\nзапрос 4 ----------------\n")

q = Query.from_(ratings).select(ratings.rating, fn.Count(ratings.id).as_("count")).groupby(ratings.rating)
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)


print("\nзапрос 5 ----------------\n")

q = Query.from_(books).join(ratings).on(books.id == ratings.book_id).select(fn.Max(books.price).as_("max_price")).where(ratings.rating >= 3)
sql = q.get_sql()
cur.execute(sql)
rows = cur.fetchall()

for i in rows:
    print(i)

conn.close()