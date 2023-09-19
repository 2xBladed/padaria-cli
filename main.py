#import sqlite3
from db_utils import *
from cli_utils import *

def main() -> None:

    #database = 'database.db'

    criar_database(database)
    pragma_config(database)
    criar_tabelas(database)

    main_loop()

if  __name__ == '__main__':
    main()