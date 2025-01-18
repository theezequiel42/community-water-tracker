# Comandos para Gerenciar o Projeto

Este arquivo contém os comandos necessários para navegar nos diretórios do projeto e reiniciar o backend e o frontend.

---

## 1. Navegar até o Diretório do Backend
1. Abra o terminal ou PowerShell.
2. Execute o seguinte comando para entrar no diretório principal do projeto:
   ```bash
   cd C:\Users\ezequ\OneDrive\Documentos\GitHub\community-water-tracker
   ```
3. Para iniciar o backend, use:
   ```bash
   python -m uvicorn main:app --reload
   ```
   - O backend estará acessível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 2. Navegar até o Diretório do Frontend
1. No mesmo terminal ou em uma nova aba, execute:
   ```bash
   cd C:\Users\ezequ\OneDrive\Documentos\GitHub\community-water-tracker\water-consumption-bot
   ```
2. Para iniciar o frontend, use:
   ```bash
   npm start
   ```
   - O frontend estará acessível em [http://localhost:3000](http://localhost:3000).

---

## 3. Reiniciar Backend e Frontend
- Para reiniciar o **backend**, pressione `CTRL+C` no terminal onde ele está rodando e execute novamente:
  ```bash
  python -m uvicorn main:app --reload
  ```

- Para reiniciar o **frontend**, pressione `CTRL+C` no terminal do React e execute novamente:
  ```bash
  npm start
  ```

---

## 4. Resumo dos Endereços
- **Backend**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Frontend**: [http://localhost:3000](http://localhost:3000)

