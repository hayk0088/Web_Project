import pyodbc
from Author.About_Authors import authors_list

id = 1

for items in authors_list:
    class Author:
        def __init__(self, authors_list):
            self.name = authors_list['Name']
            self.born = authors_list['Born']

        def __repr__(self):
            print(self.name, self.born)


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
            cursor.execute("select * from Author")

            list_products = []
            for i in range(len(cursor)):
                list_products.append(cursor[i])

            self.conn.close()
            return list(cursor)

        def create(self, book, id):
            print(f'>>> Creating Line For Author Named "{author.name}"')

            cursor = self.conn.cursor()
            cursor.execute(
                'insert into Author(id, Name, Born) values(?, ?, ?);',
                (id, author.name, author.born)
            )

            self.conn.commit()
            self.conn.close()

        def delete(self):
            print('>>> Deleting')

            cursor = self.conn.cursor()
            cursor.execute(
                'Delete From Author Where id=id'
            )

            self.conn.commit()
            self.conn.close()


    author = Author(items)

    a = SQLManager()

    # a.delete()
    a.create(author, id)
    id += 1
