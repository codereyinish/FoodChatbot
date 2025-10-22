import mysql.connector
global cnx
from dotenv import load_dotenv
import os
load_dotenv()


#Create the connection
cnx = mysql.connector.connect(
    host = os.getenv("host"),
    user = os.getenv("user"),
    password = os.getenv("db_password"),
    database = os.getenv("database")
)



def insert_order_item(next_order_id:int, food_item:int, quantity:int):
    try:
        cursor = cnx.cursor()

        #Calling the stored procedure
        cursor.callproc('insert_order_item', (next_order_id, food_item, quantity))

        #Commiting the change
        cnx.commit()

        #Closing the cursor
        cursor.close()

        print("Order item inserted successfully")
        return 1

    except mysql.connector.Error as err: #for mysql related error like table no exist, connection lost
        print(f"Error inserting the item: {err}"  )

        #Rollback changes if necessary
        cnx.rollback()
        return -1

    except Exception as e: #General non-MYSQL related errors, python 🐞
        print(f" An error occured {e}")

        cnx.rollback()
        return -1



        #Execute the procedure
        #we dont want do insert into values() multiple times





def get_next_order_id():
    try:
        cursor = cnx.cursor()

        query = "Select max(order_id) from orders"
        cursor.execute(query)

        result = cursor.fetchone()[0]

        cursor.close()

        #Returning the next available order_Id
        if result is None:
            return 1
        else:
            return result+1


    except mysql.connector.Error as err:
        print(f"Error inserting the item: {err}")

        # Rollback changes if necessary
        cnx.rollback()
        return -1


def get_total_order_price(order_id):
    try:
        cursor = cnx.cursor()

        query = "Select Sum(total_price) from orders where order_id =%s"
        cursor.execute(query, (order_id, ))

        #fetch the result, (65.00,0) --> tuple so get [0]
        total = cursor.fetchone()[0]

        cursor.close()

        return total

    except mysql.connector.Error as err:
        print(f"Error calculating the total_price: {err}")
        return -1

    except Exception as e:
        print(f"🐞 Unexpected error: {e}")
        return -1


def validateTrackID(track_id):
    try:
        cursor = cnx.cursor()
        query = "Select * from order_tracking where order_id=%s"
        cursor.execute(query,(track_id, ))
        row = cursor.fetchone()
        cursor.close()
        if not row:
            return -1
        else:
            status = row[1]
            return status

    except mysql.connector.Error as err:
        print(f"Error tracking the order: {err}")
        return -1

    except Exception as e:
        print(f"🐞 Unexpected error: {e}")
        return -1


9






