import sqlite3
import os
import pathlib
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():

    current_dir = pathlib.Path(__file__).parent.resolve()
    db_file_name = "database.sqlite3"
    db_path = os.path.join(current_dir, db_file_name)

    sql_create_categories_table = """ CREATE TABLE IF NOT EXISTS categories (
                                        category_name text PRIMARY KEY,
                                        category_description text NOT NULL
                                    ); """

    sql_create_units_table = """CREATE TABLE IF NOT EXISTS units (
                                    units text PRIMARY KEY
                                );"""

    sql_create_positions_table = """CREATE TABLE IF NOT EXISTS positions (
                                    position text PRIMARY KEY
                                );"""

    sql_create_goods_table = """ CREATE TABLE IF NOT EXISTS goods (
                                        good_id integer PRIMARY KEY,
                                        good_name text,
                                        good_unit text,
                                        good_cat text,
                                        FOREIGN KEY (good_unit) REFERENCES units (units),
                                        FOREIGN KEY (good_cat) REFERENCES categories (category_name)
                                    ); """

    sql_create_employees_table = """ CREATE TABLE IF NOT EXISTS employees (
                                        employee_id integer PRIMARY KEY,
                                        employee_fio text,
                                        employee_position text,
                                        FOREIGN KEY (employee_position) REFERENCES positions (position)
                                    ); """

    sql_create_vendors_table = """ CREATE TABLE IF NOT EXISTS vendors (
                                        vendor_id integer PRIMARY KEY,
                                        vendor_name text,
                                        vendor_ownershipform text,
                                        vendor_address text,
                                        vendor_phone text,
                                        vendor_email text
                                    ); """

    conn = create_connection(db_path)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_units_table)
        create_table(conn, sql_create_positions_table)
        create_table(conn, sql_create_goods_table)
        create_table(conn, sql_create_employees_table)
        create_table(conn, sql_create_vendors_table)
        # conn.commit()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
