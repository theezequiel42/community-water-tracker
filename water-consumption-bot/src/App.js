import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const API_URL = "http://127.0.0.1:8000"; // Certifique-se de que este é o endereço correto do backend

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.get(`${API_URL}/descricao`, {
        params: { nome: input },
      });
      if (Array.isArray(res.data)) {
        setResponse(res.data.join("\n"));
      } else {
        setResponse(res.data.mensagem || "Nenhuma resposta encontrada.");
      }
    } catch (error) {
      console.error("Erro ao conectar com o servidor:", error);
      if (error.response && error.response.data) {
        setResponse(error.response.data.detail || "Erro de conexão com o servidor.");
      } else {
        setResponse("Erro de conexão com o servidor.");
      }
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Water Consumption Bot</h1>
      <p>Digite o nome de uma pessoa para verificar o consumo:</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite o nome"
          style={{ padding: "10px", width: "300px", marginRight: "10px" }}
        />
        <button type="submit" style={{ padding: "10px 20px" }}>
          Enviar
        </button>
      </form>
      <div style={{ marginTop: "20px", whiteSpace: "pre-line" }}>
        <h3>Resposta:</h3>
        <p>{response}</p>
      </div>
    </div>
  );
};

export default App;
