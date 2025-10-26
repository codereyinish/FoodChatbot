import mysql.connector

global cnx
from dotenv import load_dotenv
import os

load_dotenv()

# Create the connection
cnx = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("db_password"),
    database=os.getenv("database")
)


def safe_query(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # the function will gets invocated and will start  running from  cursor = cnx.cursor() as usual
        except mysql.connector.Error as err:  # for mysql related error like table no exist, connection lost
            print(f"MySQL ❌: {err}")
            cnx.rollback()
            return -1
        except Exception as e:  # General non-MYSQL related errors, python 🐞
            print(f"🐞 Unexpected error: {e}")
            cnx.rollback()
            return -1
    return wrapper


@safe_query
def insert_order_item(next_order_id: int, food_item: int, quantity: int):
    cursor = cnx.cursor()

    # Calling the stored procedure
    cursor.callproc('insert_order_item', (next_order_id, food_item, quantity))

    # Commiting the change
    cnx.commit()

    # Closing the cursor
    cursor.close()

    print("Order item inserted successfully")
    return 1


@safe_query
def get_next_order_id():
    cursor = cnx.cursor()

    query = "Select max(order_id) from orders"
    cursor.execute(query)

    result = cursor.fetchone()[0]

    cursor.close()

    # Returning the next available order_Id
    if result is None:
        return 1
    else:
        return result + 1


@safe_query
def get_total_order_price(order_id):
    cursor = cnx.cursor()

    query = "Select Sum(total_price) from orders where order_id =%s"
    cursor.execute(query, (order_id,))

    # fetch the result, (65.00,0) --> tuple so get [0]
    total = cursor.fetchone()[0]

    cursor.close()

    return total


@safe_query
def validateTrackID(track_id):
    cursor = cnx.cursor()
    query = "Select * from order_tracking where order_id=%s"
    cursor.execute(query, (track_id,))
    row = cursor.fetchone()
    cursor.close()
    if not row:
        return -1
    else:
        status = row[1]
        return status


@safe_query
def extract_saved_order_from_db(track_id):
    cursor = cnx.cursor()
    query = """
        select m.name, o.quantity
        from orders as o
        join menu_items as m
            on o.item_id = m.item_id
        where o.order_id = %s         
        """
    cursor.execute(query, (track_id,))
    rows = cursor.fetchall()
    cursor.close()
    return rows
