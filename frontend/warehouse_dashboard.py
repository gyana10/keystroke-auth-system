import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="keystroke_warehouse",
    user="postgres",
    password="root"
)

def get_user_statistics():

    query = """
    SELECT *
    FROM analytics.user_statistics
    """

    return pd.read_sql(query, conn)


def get_typing_metrics():

    query = """
    SELECT *
    FROM analytics.user_typing_metrics
    """

    return pd.read_sql(query, conn)