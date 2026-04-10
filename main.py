import psycopg2
import os
from dotenv import load_dotenv

# loading variables from the .env file
load_dotenv()

def find_most_profit_buyer():
    try:
        # connection to database
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv('DB_HOST'),
            port=os.getenv("DB_PORT")
        )

        # creating a cursor for database manipulation
        cursor = conn.cursor()

        # SQL-query to get buyer data
        query = """
            SELECT buyer, price, distance, tariff
            FROM buyers_data
        """
        # extracting values from the database
        cursor.execute(query)

        # initialization of variables
        best_price = 0 
        best_buyer = None

        # basic cycle of finding maximum profit
        for buyer, s, l, t in cursor.fetchall():
            current_profit = float(s) - (float(l) * float(t))

            # load the best price if the current price is greater than the previous one
            if current_profit > best_price:
                best_price = current_profit
                best_buyer = buyer

        cursor.close()
        conn.close()
        return f"Recommended buyer: {best_buyer} | Expected net profit: {current_profit:.2f}"
    
    except Exception as e:
        return f"Error: {e}"

# start
print(find_most_profit_buyer())