import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Connected to the database!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_all(query, params=None):
    connection = get_db_connection()
    if not connection:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None
    finally:
        cursor.close()
        connection.close()

# Execute a SELECT query and fetch a single result.

def fetch_one(query, params=None):
    connection = get_db_connection()
    if not connection:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None
    finally:
        cursor.close()
        connection.close()

def execute_query(query, params=None):
    connection = get_db_connection()
    if not connection:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(query, params or ())
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return False
    finally:
        cursor.close()
        connection.close()

# Category Functions

def get_all_categories_from_db():
    query = "SELECT * FROM category;"
    return fetch_all(query)

def get_category_name_from_db(category_id):
    query = "SELECT name FROM category WHERE category_id = %s;"
    return fetch_one(query, (category_id,))

def get_category_id_from_db(name):
    query = "SELECT category_id FROM category WHERE name = %s;"
    return fetch_one(query, (name,))

def add_category_to_db(category_id, name):
    query = "INSERT INTO category (category_id, name) VALUES (%s, %s);"
    return execute_query(query, (category_id, name))


# Book Functions

def get_all_books_from_db():
    query = "SELECT * FROM book;"
    return fetch_all(query)


def get_book_by_id_from_db(book_id):
    query = "SELECT * FROM book WHERE book_id = %s;"
    return fetch_one(query, (book_id,))


def get_books_by_category_id_from_db(category_id):
    query = "SELECT * FROM book WHERE category_id = %s;"
    return fetch_all(query, (category_id,))


def get_books_by_category_name_from_db(name):
    query = """
    SELECT b.* 
    FROM book b
    INNER JOIN category c ON b.category_id = c.category_id
    WHERE c.name = %s;
    """
    return fetch_all(query, (name,))


def get_random_books_from_db():
    query = "SELECT * FROM book ORDER BY RAND() LIMIT 5;"
    return fetch_all(query)

def add_book_to_db(book_id, title, author, description, price, rating, is_public, is_featured, category_id):
    query = """
    INSERT INTO book (book_id, title, author, description, price, rating, is_public, is_featured, category_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    return execute_query(query, (book_id, title, author, description, price, rating, is_public, is_featured, category_id))