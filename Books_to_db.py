import pyodbc
from Book.books_characterics import books_list

id = 1

for items in books_list:
    class Book:
        def __init__(self, book_dict):
            self.title = book_dict['Title']
            self.author = book_dict['Author']
            self.language = book_dict['Language']
            self.country = book_dict['Country']


    class SQLManager:
        def __init__(self):
            self.conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=(LocalDB)\\MSSQLLocalDB;"
                "Database=WebProject.sql;"
                "Trusted_Connection=Yes;"
            )

        def get_all(self) -> list:
            print(">>> Reading")

            cursor = self.conn.cursor()
            cursor.execute("select * from Book")

            list_products = []
            for i in range(len(cursor)):
                list_products.append(cursor[i])

            self.conn.close()
            return list(cursor)

        def create(self, book, id):
            print(f'>>> Creating Line For Book Named "{book.title}"')

            cursor = self.conn.cursor()
            cursor.execute(
                'insert into Book(id, Title, Author, Language, Country) values(?, ?, ?, ?, ?);',
                (id, book.title, book.author, book.language, book.country)
                # (id, 'dsc', 'rdgf', 'yujhgn', 'ythgf')
            )

            self.conn.commit()
            self.conn.close()

        def delete(self):
            print('>>> Deleting')

            cursor = self.conn.cursor()
            cursor.execute(
                'Delete From Book Where id=id'
            )

            self.conn.commit()
            self.conn.close()


    book = Book(items)

    a = SQLManager()
    # a.delete()
    a.create(book, id)
    id += 1
