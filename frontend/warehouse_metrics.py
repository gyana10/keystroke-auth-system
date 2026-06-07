import psycopg2
import pandas as pd

def get_metrics():

    conn = psycopg2.connect(
        host="localhost",
        database="keystroke_warehouse",
        user="postgres",
        password="root"
    )

    query = """
    SELECT *
    FROM analytics.user_typing_metrics
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df