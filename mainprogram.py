import sys

from util import get_tables,load_database_details
from read import read_table
from write import load_table,build_insert_querey
def main():
    print("hello world")
    """ this program takes one argument as env variable but in practical you need to write another 
      function regarding the usage"""
    env = sys.argv[1] # check env variables under run option
    db_details = load_database_details(env)
    print(db_details)
    tables = get_tables('table_list')
    for table_name in tables['table_name']:
        print("reading data from source db")
        data,column_names = read_table(db_details,table_name)
        """ the above code is for reading the data now after reading it I will write in mysql """
        print("writing data from source db")
        #qx = build_insert_querey(table_name,column_names)
        #print("in qxxxxxxxxxxxxxxxxxx====",qx)
        load_table(db_details,data,column_names,table_name)



    #for record in data:
    #print(record)
        


if __name__=='__main__':
    main()
