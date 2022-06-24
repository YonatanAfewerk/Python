# import database 
import sqlite3
from tabulate import tabulate

# choice = int(input("Enter Your choice Read Db(1) Insert To Db(2): "))


# if 1 == choice:
#     print(database.show_all_products())
# elif 2 == choice:
#     product_list = [
#          (11,'EXTRA chewing gum','EXTRA','chewing gum 35 stick','Available',499.9),]

#     print(database.add_to_product(product_list))



conn = sqlite3.connect("Register.db")
c = conn.cursor()


c.execute('''
    SELECT * 
    FROM registered
''')

table = c.fetchall()

print(tabulate(table,tablefmt='grid'))

