# Water Consumption Tracker

## Descrição (Português)
Este projeto é uma aplicação composta por um backend desenvolvido em **FastAPI** e um frontend em **React.js**. O objetivo é fornecer uma interface para consulta de dados de consumo de água de uma comunidade, permitindo que os usuários obtenham informações detalhadas sobre seus consumos mensais.

### Funcionalidades
- Consulta de consumo de água por nome.
- Backend utilizando FastAPI para gerenciar os dados.
- Frontend interativo desenvolvido em React.js.

### Requisitos do Sistema
#### Backend:
- Python 3.9 ou superior
- Pacotes: `fastapi`, `uvicorn`, `pandas`, `openpyxl`

#### Frontend:
- Node.js (v16 ou superior recomendado)
- Pacote `axios` instalado

### Como Configurar e Executar

#### Backend:
1. Instale os pacotes necessários:
   ```bash
   pip install fastapi uvicorn pandas openpyxl
   ```
2. Certifique-se de que o arquivo `consumo-agua-2024.xlsx` está presente no diretório do projeto.
3. Execute o servidor:
   ```bash
   python -m uvicorn main:app --reload
   ```
4. O servidor estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

#### Frontend:
1. Instale as dependências do projeto React:
   ```bash
   npm install
   ```
2. Inicie o servidor React:
   ```bash
   npm start
   ```
3. O frontend estará disponível em [http://localhost:3000](http://localhost:3000).

### Uso
1. Abra o frontend em seu navegador.
2. Digite o nome desejado no campo de entrada e clique em "Enviar".
3. A aplicação exibirá o consumo de água correspondente ao nome informado.

### Estrutura de Arquivos
```
/
├── main.py          # Backend FastAPI
├── consumo-agua-2024.xlsx  # Arquivo Excel com os dados
├── water-consumption-bot/  # Diretório do projeto React
│   ├── src/
│   │   ├── App.js   # Arquivo principal do React
│   │   └── ...
└── README.md        # Documentação
```

---

## Description (English)
This project is an application consisting of a **FastAPI** backend and a **React.js** frontend. The goal is to provide an interface for querying water consumption data of a community, allowing users to retrieve detailed information about their monthly consumption.

### Features
- Query water consumption by name.
- Backend using FastAPI to manage data.
- Interactive frontend built with React.js.

### System Requirements
#### Backend:
- Python 3.9 or higher
- Packages: `fastapi`, `uvicorn`, `pandas`, `openpyxl`

#### Frontend:
- Node.js (v16 or higher recommended)
- `axios` package installed

### How to Set Up and Run

#### Backend:
1. Install the required packages:
   ```bash
   pip install fastapi uvicorn pandas openpyxl
   ```
2. Ensure the file `consumo-agua-2024.xlsx` is present in the project directory.
3. Start the server:
   ```bash
   python -m uvicorn main:app --reload
   ```
4. The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

#### Frontend:
1. Install the React project dependencies:
   ```bash
   npm install
   ```
2. Start the React server:
   ```bash
   npm start
   ```
3. The frontend will be available at [http://localhost:3000](http://localhost:3000).

### Usage
1. Open the frontend in your browser.
2. Enter the desired name in the input field and click "Send".
3. The application will display the water consumption corresponding to the entered name.

### File Structure
```
/
├── main.py          # FastAPI backend
├── consumo-agua-2024.xlsx  # Excel file with data
├── water-consumption-bot/  # React project directory
│   ├── src/
│   │   ├── App.js   # Main React file
│   │   └── ...
└── README.md        # Documentation
```

