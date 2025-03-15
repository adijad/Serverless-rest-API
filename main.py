from app.db_utils import get_db_connection
from app.handlers import get_all_categories

# Check database connection
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        print("Connection successful!")
        connection.close()
    else:
        print("Connection failed.")

# Get categories from the database
if __name__ == "__main__":
    # Simulate an AWS Lambda event
    fake_event = {}
    fake_context = {}
    response = get_all_categories(fake_event, fake_context)
    print(response)
