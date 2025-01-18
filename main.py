import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configurar o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir o endereço do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho para o arquivo Excel
file_path = "consumo-agua-2024.xlsx"

def carregar_dados():
    try:
        # Carregar os dados do Excel
        dados = pd.read_excel(file_path)

        # Imprimir os nomes das colunas para depuração
        print("Colunas disponíveis no arquivo:", dados.columns.tolist())

        # Verificar se as colunas obrigatórias estão presentes
        if 'Nome' not in dados.columns:
            raise KeyError("A coluna 'Nome' é obrigatória e não foi encontrada no arquivo.")

        return dados

    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return None
    except KeyError as e:
        print(f"Erro nas colunas do arquivo: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return None

# Carregar os dados ao iniciar
dados = carregar_dados()

@app.get("/")
def read_root():
    if dados is None:
        raise HTTPException(status_code=500, detail="Os dados não foram carregados corretamente.")
    return {"message": "API funcionando corretamente!"}

@app.get("/descricao")
def get_descricao(
    nome: str,
    mes: str = Query(default=None, regex=r"^(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)$", description="Mês do consumo"),
    ano: int = Query(default=None, description="Ano do consumo")
):
    if dados is None:
        raise HTTPException(status_code=500, detail="Os dados não foram carregados corretamente.")

    # Normalizar o nome para busca
    resultado = dados[dados['Nome'].str.contains(nome, case=False, na=False)]

    if resultado.empty:
        return {"mensagem": f"Nenhum consumo encontrado para o nome: {nome}"}

    # Determinar o mês e ano atuais se não forem fornecidos
    agora = datetime.now()
    mes_atual = agora.strftime("%B").lower()  # Nome do mês atual em minúsculas
    ano_atual = agora.year

    # Ajustar para o mês anterior se o mês atual for janeiro
    if mes is None and ano is None:
        if mes_atual == "january":
            mes = "dezembro"
            ano = ano_atual - 1
        else:
            mes = mes_atual
            ano = ano_atual

    # Caso o mês seja fornecido, mas o ano não
    if ano is None:
        ano = ano_atual

    # Construir os nomes das colunas dinamicamente
    if f"Consumo {mes.capitalize()}" in dados.columns and f"Valor {mes.capitalize()}" in dados.columns:
        # Se a coluna não tem ano, usar o ano atual como referência
        coluna_consumo = f"Consumo {mes.capitalize()}"
        coluna_valor = f"Valor {mes.capitalize()}"
    else:
        # Caso contrário, procurar colunas com o ano explícito
        coluna_consumo = f"Consumo {mes.capitalize()} ({ano})"
        coluna_valor = f"Valor {mes.capitalize()} ({ano})"

    if coluna_consumo not in dados.columns or coluna_valor not in dados.columns:
        return {"mensagem": f"Os dados para {mes.capitalize()} de {ano} não estão disponíveis."}

    # Adicionar as descrições baseadas nos dados filtrados
    resultado['descricao'] = resultado.apply(
        lambda row: f"{row['Nome']} teve consumo de {row[coluna_consumo]}m³ em {mes.capitalize()}, pagando R${row[coluna_valor]}",
        axis=1
    )

    return resultado['descricao'].tolist()

@app.get("/debug")
def debug():
    try:
        if dados is None:
            raise HTTPException(status_code=500, detail="Os dados não foram carregados corretamente.")
        return {"colunas": dados.columns.tolist()}
    except Exception as e:
        return {"erro": str(e)}
