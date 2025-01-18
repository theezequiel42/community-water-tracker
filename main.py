import sqlite3
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

app = FastAPI()

# Configurar o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir o endereço do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho absoluto para o banco de dados SQLite
db_path = os.path.abspath("consumo_agua.db")

@app.get("/")
def read_root():
    return {"message": "API funcionando corretamente!"}

@app.get("/descricao")
def get_descricao(
    nome: str,
    mes: str = Query(default=None, regex=r"^(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)$", description="Mês do consumo"),
    ano: int = Query(default=None, description="Ano do consumo")
):
    try:
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Determinar o mês e ano atuais se não forem fornecidos
        agora = datetime.now()
        mes_atual = agora.strftime("%B").lower()  # Nome do mês atual em minúsculas
        ano_atual = agora.year

        if mes is None and ano is None:
            if mes_atual == "january":
                mes = "dezembro"
                ano = ano_atual - 1
            else:
                mes = mes_atual
                ano = ano_atual

        if ano is None:
            ano = ano_atual

        # Construir os nomes das colunas dinamicamente
        coluna_consumo = f"Consumo {mes.capitalize()} {ano} (m³)"
        coluna_valor = f"Valor {mes.capitalize()} {ano} (R$)"

        # Verificar se as colunas existem na tabela
        cursor.execute("PRAGMA table_info(consumo_agua)")
        colunas = [info[1] for info in cursor.fetchall()]

        if coluna_consumo not in colunas or coluna_valor not in colunas:
            return {"mensagem": f"Os dados para {mes.capitalize()} de {ano} não estão disponíveis."}

        # Consultar os dados para o nome especificado
        query = f"SELECT Nome, `{coluna_consumo}`, `{coluna_valor}` FROM consumo_agua WHERE Nome LIKE ?"
        cursor.execute(query, (f"%{nome}%",))
        resultados = cursor.fetchall()

        if not resultados:
            return {"mensagem": f"Nenhum consumo encontrado para o nome: {nome}"}

        # Montar a resposta
        descricao = [
            f"{row[0]} teve consumo de {row[1]}m³ em {mes.capitalize()}, pagando R${row[2]}"
            for row in resultados
        ]

        return descricao

    except Exception as e:
        return {"erro": str(e)}

    finally:
        conn.close()

@app.get("/debug")
def debug():
    try:
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Obter informações sobre as colunas da tabela
        cursor.execute("PRAGMA table_info(consumo_agua)")
        colunas = [info[1] for info in cursor.fetchall()]

        return {"colunas": colunas}

    except Exception as e:
        return {"erro": str(e)}

    finally:
        conn.close()

@app.get("/nomes")
def get_nomes(query: str = ""):
    """
    Retorna uma lista de nomes que correspondem ao parâmetro de consulta.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Consulta para buscar nomes que começam com o termo digitado
        cursor.execute("SELECT DISTINCT Nome FROM consumo_agua WHERE Nome LIKE ?", (f"{query}%",))
        resultados = cursor.fetchall()

        nomes = [row[0] for row in resultados]
        return {"nomes": nomes}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        conn.close()
