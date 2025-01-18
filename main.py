import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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
        required_columns = ['Nome', 'Medição Dezembro 2023 ()', 'Valor Dezembro 2023 (R$)']
        missing_columns = [col for col in required_columns if col not in dados.columns]

        if missing_columns:
            raise KeyError(f"As colunas obrigatórias estão ausentes: {missing_columns}")

        # Criar uma nova coluna com descrições formatadas
        dados['descricao'] = dados.apply(
            lambda row: f"{row['Nome']} teve consumo de {row['Medição Dezembro 2023 ()']}m³ em dezembro, pagando R${row['Valor Dezembro 2023 (R$)']}",
            axis=1
        )
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
def get_descricao(nome: str):
    if dados is None:
        raise HTTPException(status_code=500, detail="Os dados não foram carregados corretamente.")

    resultado = dados[dados['Nome'].str.contains(nome, case=False, na=False)]

    if resultado.empty:
        return {"mensagem": f"Nenhum consumo encontrado para o nome: {nome}"}

    return resultado['descricao'].tolist()

@app.get("/debug")
def debug():
    try:
        if dados is None:
            raise HTTPException(status_code=500, detail="Os dados não foram carregados corretamente.")
        return {"colunas": dados.columns.tolist()}
    except Exception as e:
        return {"erro": str(e)}
