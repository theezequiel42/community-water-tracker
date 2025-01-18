# Water Consumption Bot

## Descrição
O **Water Consumption Bot** é um projeto que permite consultar o consumo de água de usuários de uma comunidade com base em dados de um banco SQLite criado a partir de uma planilha Excel. A aplicação conta com um backend em Python (FastAPI) e um frontend em React.js, proporcionando uma interface intuitiva para realizar consultas e obter informações detalhadas sobre o consumo.

---

## Funcionalidades
- Consulta de consumo de água por nome.
- Filtros por mês e ano.
- Carregamento dinâmico dos dados do banco SQLite.
- Interface responsiva para visualização dos resultados.

---

## Tecnologias Utilizadas

### Backend
- **Python**
  - FastAPI
  - SQLite
  - pandas
  - SQLAlchemy

### Frontend
- **React.js**
  - Axios
  - CSS para estilização básica

---

## Instalação e Configuração

### 1. Backend

1. Certifique-se de que o Python 3.10+ está instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install fastapi uvicorn pandas sqlalchemy sqlite3 openpyxl
   ```
3. Gere o banco de dados SQLite a partir da planilha Excel:
   - Coloque o arquivo `consumo-agua.xlsx` na pasta do projeto.
   - Certifique-se de que o script cria o banco corretamente no primeiro início.
4. Inicie o servidor backend:
   ```bash
   python -m uvicorn main:app --reload
   ```
5. O backend estará acessível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 2. Frontend

1. Navegue até a pasta do frontend:
   ```bash
   cd water-consumption-bot
   ```
2. Instale as dependências necessárias:
   ```bash
   npm install
   ```
3. Inicie o servidor do frontend:
   ```bash
   npm start
   ```
4. O frontend estará acessível em: [http://localhost:3000](http://localhost:3000)

---

## Uso

1. Abra o navegador e acesse o frontend.
2. Digite o nome de uma pessoa para consultar o consumo de água.
3. (Opcional) Selecione um mês e um ano específicos para filtrar os resultados.
4. Clique em **Consultar**.

---

## Endpoints do Backend

### 1. `/descricao`
**Método:** GET  
**Parâmetros:**
- `nome` (obrigatório): Nome da pessoa a ser consultada.
- `mes` (opcional): Mês do consumo.
- `ano` (opcional): Ano do consumo.

**Exemplo de uso:**
```bash
GET http://127.0.0.1:8000/descricao?nome=gilmar&mes=dezembro&ano=2024
```

### 2. `/debug`
**Método:** GET  
Exibe informações de debug sobre as colunas do banco de dados carregado.

**Exemplo de uso:**
```bash
GET http://127.0.0.1:8000/debug
```

---

## Estrutura do Projeto
```
.
├── main.py          # Backend FastAPI
├── database.db      # Banco de dados SQLite gerado
├── consumo-agua.xlsx # Planilha original para criar o banco
├── water-consumption-bot/ # Diretório do frontend
│   ├── src/
│   │   ├── App.js  # Componente principal do React
│   │   ├── App.css # Estilização
│   │   └── index.js
│   └── package.json # Configuração do frontend
└── README.md        # Este arquivo
```


## Contribuição
Sinta-se à vontade para abrir issues e enviar pull requests para melhorias neste projeto.

---

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

