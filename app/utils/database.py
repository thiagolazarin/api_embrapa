import sqlite3

DB_NAME = "data.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def save_dataframe_to_db(df, table_name):
    """
    Salva um DataFrame no banco de dados SQLite.
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        table_name (str): Nome da tabela no banco de dados.
    """
    conn = get_connection()
    
    # Salvar no banco, sobrescrevendo a tabela, se existir
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()
