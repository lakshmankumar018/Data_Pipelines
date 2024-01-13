"""
This file contains connections from source database to destination database
"""

import pandas as pd
from config import database_details
from mysql import connector as mc
from mysql.connector import Error as ec

def load_database_details(env):
    return database_details[env]


def get_mysql_connection(DB_HOST,DB_NAME,DB_USER,DB_PASS,DB_PORT):
    try:
        connection = mc.connect(
            user = DB_USER,
            password = DB_PASS,
            host=DB_HOST,
            port =DB_PORT,
            database = DB_NAME
        )
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("invalid credentials")
        else:
            print(error)
    return connection

def get_conection(db_type,db_host,db_name,db_user,db_pass,db_port):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host,db_name,db_user,db_pass,db_port)

    return connection

def get_tables(path):
    tables = pd.read_csv(path,sep=':')
    return tables.query('to_be_loaded == "yes"')

