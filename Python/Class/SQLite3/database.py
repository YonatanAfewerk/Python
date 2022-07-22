import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("Daisy's thrift shop-Inventory-Management.db")
c = conn.cursor()

def show_all_products():
        # get data from the tables 
    c.execute(""" 
        SELECT *
        FROM product
    """)

    table = c.fetchall()

    print( tabulate(table,tablefmt='grid'))

    return tabulate(table,tablefmt='grid')



def add_to_product(product_list):
    c.executemany("""
            INSERT INTO product(pro_id,Pro_name,pro_brand,pro_type,status,pro_price) 
            VALUES (?,?,?,?,?,?)""",product_list)

    conn.commit()
    conn.close()

    return f'Added Data! {c.rowcount} rows affected'


show_all_products()