import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [nome, setNome] = useState('');
  const [resultado, setResultado] = useState(null);
  const [mes, setMes] = useState('');
  const [ano, setAno] = useState('');
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState(null);

  const consultar = async () => {
    setLoading(true);
    setErro(null);
    setResultado(null);

    try {
      const params = {
        nome,
        ...(mes && { mes }),
        ...(ano && { ano }),
      };

      const response = await axios.get('http://127.0.0.1:8000/descricao', { params });
      setResultado(response.data);
    } catch (error) {
      setErro('Erro ao consultar os dados. Verifique sua conexão ou tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Water Consumption Bot</h1>
        <p>Digite o nome de uma pessoa para verificar o consumo de água:</p>

        <div className="form">
          <input
            type="text"
            placeholder="Nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
          />
          <select value={mes} onChange={(e) => setMes(e.target.value)}>
            <option value="">Escolha o mês</option>
            <option value="janeiro">Janeiro</option>
            <option value="fevereiro">Fevereiro</option>
            <option value="março">Março</option>
            <option value="abril">Abril</option>
            <option value="maio">Maio</option>
            <option value="junho">Junho</option>
            <option value="julho">Julho</option>
            <option value="agosto">Agosto</option>
            <option value="setembro">Setembro</option>
            <option value="outubro">Outubro</option>
            <option value="novembro">Novembro</option>
            <option value="dezembro">Dezembro</option>
          </select>
          <input
            type="number"
            placeholder="Ano"
            value={ano}
            onChange={(e) => setAno(e.target.value)}
          />
          <button onClick={consultar} disabled={loading || !nome}>
            Consultar
          </button>
        </div>

        {loading && <p>Consultando...</p>}
        {erro && <p className="error">{erro}</p>}

        {resultado && (
          <div className="resultado">
            <h2>Resultado:</h2>
            <ul>
              {Array.isArray(resultado) ? (
                resultado.map((res, index) => <li key={index}>{res}</li>)
              ) : (
                <li>{resultado.mensagem}</li>
              )}
            </ul>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
