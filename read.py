from util import get_conection

def read_table(database_details,table_name,limit =0):
    source_database_details =  database_details['source_database']
    connection = get_conection(
         source_database_details['DB_TYPE'],
        source_database_details['DB_HOST'],
         source_database_details['DB_NAME'],
         source_database_details['DB_USER'],
         source_database_details['DB_PASS'],
        source_database_details['DB_PORT']
    )
    cur = connection.cursor()
    print("=====in reading cursor")
    if limit ==0:
        query = 'select * from {table_name}'
    else:
        query = 'select * from {table_name} LIMIT {limit}'

    query = 'select * from {}'.format(table_name)
    print(query,"=======================")
    cur.execute(query)
    data = cur.fetchall()
    column_names = cur.column_names

    connection.close()
    return data,column_names
