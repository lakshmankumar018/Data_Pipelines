from util import get_conection

def build_insert_querey(table_name,column_names):
    column_values = tuple(map(lambda c: c.replace(c,"%s"),column_names))
    query = "insert into {} values {} ".format(table_name,column_values)
    return query

def load_table(database_details,data,column_names,table_name):
    target_database_details = database_details['target_database']
    conneection = get_conection(
        target_database_details['DB_TYPE'],
        target_database_details['DB_HOST'],
        target_database_details['DB_NAME'],
        target_database_details['DB_USER'],
        target_database_details['DB_PASS'],
        target_database_details['DB_PORT'],

    )
    cur = conneection.cursor()
    query = build_insert_querey(table_name,column_names)
    write_table_into_targetdb(conneection,cur,query,data)
    conneection.close()


def write_table_into_targetdb(connection,cursr,querey,data,batch_size = 100):
    #records =[]
    #count = 1

    #print(querey,"===========++++++++++++++")

    for rec in data:
        #records.append(rec)
        cursr.execute(querey,rec,multi=True)
        #print(rec,"+++++++++++++++++",type(rec))
        #if count % batch_size == 0:
    #cursr.executemany(querey,a for a in )
    connection.commit()

            #records = []

        #count = count +1
    #cursr.executemany(querey, records)
    #connection.commit()


