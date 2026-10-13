# 🌐 Painel de Monitoramento Simples em Python

Um painel de monitoramento de servidores e APIs web leve, construído inteiramente com a **biblioteca padrão do Python** (sem dependências externas). Ele inicia um servidor HTTP local e exibe uma interface web responsiva e elegante que é atualizada automaticamente.

---

## ✨ Características

* **Zero Dependências Externas:** Utiliza apenas módulos nativos do Python (`urllib`, `http.server`, `socket`, `time`, etc.).
* **Atualização Automática:** A página web possui um mecanismo de *refresh* configurável para checar o status dos serviços periodicamente.
* **Interface Visual Intuitiva:** Exibe cards dinâmicos com códigos de cores (`Verde` para **Online** e `Vermelho` para **Offline**).
* **Tratamento Robusto de Erros:** Identifica e reporta falhas como erros HTTP, timeouts, falhas de DNS ou conexões recusadas.
* **Logs Limpos:** O console do terminal permanece limpo, suprimindo requisições HTTP secundárias para facilitar a visualização.

---

## 🚀 Como Executar

### Pré-requisitos
* Ter o **Python 3.x** instalado no seu computador.

### Passo a Passo

1. Baixe ou clone este repositório contendo o arquivo `Monitor.py`.
2. Abra o terminal (Prompt de Comando, PowerShell ou Terminal do Linux/macOS) na pasta onde o arquivo está salvo.
3. Execute o script com o comando:

```bash
python Monitor.py
```

4. Abra o seu navegador web favorito e acesse o endereço:
   👉 **[http://localhost:8501](http://localhost:8501)**

5. Para encerrar o monitoramento, retorne ao terminal e pressione **`Ctrl + C`**.

---

## ⚙️ Configuração Personalizada

Você pode abrir o arquivo `Monitor.py` em qualquer editor de código e ajustar as variáveis de configuração no topo do arquivo:

```python
# Lista de endpoints que você deseja monitorar
ENDPOINTS = [
    {"id": 1, "name": "Meu Servidor Local", "url": "https://www.google.com.br"},
    {"id": 2, "name": "API Externa", "url": "https://httpbin.org/status/200"},
]

TEMPO_ATUALIZACAO = 10  # Tempo (em segundos) para atualizar a página web
TEMPO_MAXIMO = 5        # Tempo limite (timeout em segundos) para a resposta da requisição
PORTA_SERVIDOR = 8501   # Porta local onde o painel será hospedado
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem principal.
* **`http.server`:** Para subir o servidor web nativo.
* **`urllib.request`:** Para disparar as requisições HTTP de teste.
* **HTML5 & CSS3:** Para a estilização moderna e limpa do painel de controle.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE). Sinta-se à vontade para usá-lo, modificá-lo e melhorá-lo!
