import sqlite3
import pandas as pd

# Caminho do arquivo Excel
file_path = "consumo-agua-2024.xlsx"  # Substitua pelo caminho correto no seu projeto

# Nome do arquivo do banco de dados SQLite
db_path = "consumo_agua.db"

try:
    # Ler a planilha Excel
    data = pd.read_excel(file_path)

    # Conectar ao SQLite
    conn = sqlite3.connect(db_path)

    # Exportar a planilha para uma tabela no banco de dados
    table_name = "consumo_agua"
    data.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"Banco de dados criado com sucesso: {db_path}")
    conn.close()
except Exception as e:
    print(f"Erro ao criar o banco de dados: {e}")
