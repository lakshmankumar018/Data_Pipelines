import sys
from config import database_details

def main():
    print("hello world")
    """ this program takes one argument as env variable but in practical you need to write another 
      function regarding the usage"""
    env = sys.argv[1] # check env variables under run option
    db_details = database_details[env]
   # print(db_details)



if __name__=='__main__':
    main()
