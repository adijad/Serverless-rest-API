import json
from app.db_utils import get_db_connection
from app.db_utils import (
    get_all_categories_from_db,
    get_category_name_from_db,
    get_category_id_from_db,
    add_category_to_db,
    get_all_books_from_db,
    get_book_by_id_from_db,
    get_books_by_category_id_from_db,
    get_books_by_category_name_from_db,
    get_random_books_from_db,
    add_book_to_db,
)


# def get_all_categories(event, context):
#     """Fetch all categories from the database."""
#     connection = get_db_connection()
#     if not connection:
#         return {
#             "statusCode": 500,
#             "body": json.dumps({"error": "Database connection failed"})
#         }

#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM category;")
#         categories = cursor.fetchall()
#         return {
#             "statusCode": 200,
#             "body": json.dumps({"category": categories})
#         }
#     except Exception as e:
#         return {
#             "statusCode": 500,
#             "body": json.dumps({"error": str(e)})
#         }
#     finally:
#         connection.close()

#  Main entry point for the Lambda function.
def lambda_handler(event, context):
    try:
        # Log the entire event for debugging
        print("Received event:", json.dumps(event))

        path = event.get("path")
        http_method = event.get("httpMethod")

        print(f"Path: {path}, HTTP Method: {http_method}")  # Debugging the path and method

        if path == "/getAllCategory" and http_method == "GET":
            return get_all_categories()
        elif path.startswith("/getCategoryName") and http_method == "GET":
            # category_id = event.get("queryStringParameters", {}).get("category_id")
            category_id = event.get("pathParameters", {}).get("category_id")
            return get_category_name(category_id)
        elif path == "/getCategoryId" and http_method == "GET":
            name = event.get("queryStringParameters", {}).get("name")
            return get_category_id(name)
        elif path == "/addCategory" and http_method == "POST":
            body = json.loads(event.get("body", "{}"))
            return add_category(body)
        elif path == "/getAllBook" and http_method == "GET":
            return get_all_books()
        elif path == "/getBookById" and http_method == "GET":
            book_id = event.get("queryStringParameters", {}).get("book_id")
            return get_book_by_id(book_id)
        elif path == "/getBookByCategoryId" and http_method == "GET":
            category_id = event.get("queryStringParameters", {}).get("category_id")
            return get_books_by_category_id(category_id)
        elif path == "/getBookByCategoryName" and http_method == "GET":
            name = event.get("queryStringParameters", {}).get("name")
            return get_books_by_category_name(name)
        elif path == "/getRandomBook" and http_method == "GET":
            return get_random_books()
        elif path == "/addBook" and http_method == "POST":
            body = json.loads(event.get("body", "{}"))
            return add_book(body)
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Endpoint not found"})
            }
    except Exception as e:
        # Log the error for debugging
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "An error occurred", "details": str(e)})
        }


def get_all_categories():
    """Fetch all categories from the database."""
    try:
        categories = get_all_categories_from_db()
        if categories is None:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Failed to fetch categories"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"category": categories})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_category_name(category_id):
    # category_id = event.get("pathParameters", {}).get("category_id")
    """Fetch the name of a category by ID."""
    if not category_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing category_id"})
        }

    try:
        category = get_category_name_from_db(category_id)
        if category is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Category not found"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"name": category[0]})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_category_id(name):
    if not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing category_name"})
        }
    try:
        category = get_category_id_from_db(name)
        if category is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Category ID not found"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps({"category_id": category[0]})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def add_category(body):
    """Add a new category to the database."""
    category_id = body.get("category_id")
    name = body.get("name")

    if not category_id or not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing category_id or category_name"})
        }

    try:
        success = add_category_to_db(category_id, name)
        if not success:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Failed to add category"})
            }

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Category added successfully"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_all_books():
    try:
        books = get_all_books_from_db()
        if books is None:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Failed to fetch books"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps({"book": books})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_book_by_id(book_id):
    if not book_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing book_id"})
        }
    try:
        book = get_book_by_id_from_db(book_id)
        if book is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Book not found"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps({"book": book})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_books_by_category_id(category_id):
    if not category_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing category_id"})
        }
    try:
        books = get_books_by_category_id_from_db(category_id)
        if books is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "No books found for this category"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps({"books": books})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_books_by_category_name(name):
    if not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing category_name"})
        }
    try:
        books = get_books_by_category_name_from_db(name)
        if books is None:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "No books found for this category"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps({"book": books})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def get_random_books():
    try:
        books = get_random_books_from_db()
        if books is None:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Failed to fetch random books"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps({"book": books})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def add_book(body):
    """Handler for adding a new book."""
    book_id = body.get("book_id")
    title = body.get("title")
    author = body.get("author")
    description = body.get("description", "")
    price = body.get("price")
    rating = body.get("rating")
    is_public = body.get("is_public")
    is_featured = body.get("is_featured")
    category_id = body.get("category_id")

    # Validate input fields
    if book_id is None or title is None or author is None or price is None or rating is None or is_public is None or is_featured is None or category_id is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing required fields"})
        }

    try:
        success = add_book_to_db(book_id, title, author, description, price, rating, is_public, is_featured,
                                 category_id)
        if not success:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Failed to add book"})
            }

        return {
            "statusCode": 201,
            "body": json.dumps({"message": "Book added successfully"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
