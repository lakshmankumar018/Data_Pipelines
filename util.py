"""
This file contains connections from source database to destination database
"""

import pandas as pd


def get_tables(path):
    tables = pd.read_csv(path,sep=':')
    return tables.query('to_be_loaded == "yes"')

