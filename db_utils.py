import sqlite3
import time

def data_hora() -> str:
    '''
    Retorna a data e a hora no formato YYYY-MM-DD HH:MM:SS
    '''
    data = list(time.localtime())
    data = [str(x) for x in data]
    return '-'.join([data[0],data[1],data[2]]) + ' ' + ':'.join([data[3],data[4],data[5]])

def criar_database(database) -> None:
    '''
    Cria se não existir, a database.
    '''
    conn = sqlite3.connect(database)
    conn.commit()
    conn.close()
    return

def pragma_config(database) -> None:
    '''
    Modifica as configurações PRAGMA da database.
    '''
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    conn.close()
    return

# TODO: editar as tabelas e adicionar preço e valor de caixa (receita)
def criar_tabelas(database) -> None:
    '''
    Cria se não existir as tabelas necessárias na database.
    '''
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Produto (
                    barCode INTEGER PRIMARY KEY,
                    name TEXT UNIQUE
                )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Estoque (
                    barCode_produto INTEGER PRIMARY KEY,
                    quantity INTEGER,
                    FOREIGN KEY (barCode_produto) REFERENCES Produto(barcode)
                )''')    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Log (
                    operation TEXT PRIMARY KEY,
                    barCode_produto INTEGER,
                    quantity INTEGER,
                    dateTime TEXT,
                    FOREIGN KEY (barCode_produto) REFERENCES Produto(barcode)
                )''')

    conn.commit()
    conn.close()
    return

# TODO
def criar_index() -> None:
    pass

# TODO: fazer testes para verificar os tipos dos argumentos, 
# ex.: verificar se barcode é int.
def insert_produto(barcode: int, name: str, quantity=None) -> None:
    '''
    Insere um produto na database.
    '''
    sql1 = '''  INSERT INTO Produto(barCode, name)
                VALUES(?,?)'''
    sql2 = '''  INSERT INTO Estoque(barCode_produto, quantity)
                VALUES(?,?)'''
    sql3 = '''  INSERT INTO Log(operation, barCode_produto, quantity, dateTime)
                VALUES(?,?,?,?)'''
    operation = 'created & in' if quantity != None else 'created'
    date_time = data_hora()

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(sql1, (barcode, name))

    if quantity != None:
        cursor.execute(sql2, (barcode, quantity))
    
    cursor.execute(sql3, (operation, barcode, quantity, date_time))

    conn.commit()
    conn.close()
    return

# TODO
def delete_produto():
    pass

# TODO
def vender_produto():
    pass