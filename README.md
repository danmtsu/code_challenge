# code_challenge


# Projeto: Code Challenger

## Descrição
Este projeto é uma aplicação web interativa desenvolvida com Flask e Flask-SocketIO, que oferece funções matemáticas como cálculo de números de Fibonacci e números primos, utilizando abordagens lineares e recursivas. A aplicação inclui uma interface gráfica simples em HTML e JavaScript, permitindo a interação do usuário através de um chat.

## Funcionalidades
- **Cálculo de Fibonacci (Linear e Recursivo):**
  - Fibonacci linear usa um loop iterativo.
  - Fibonacci recursivo usa chamadas recursivas.
- **Cálculo de Números Primos (Linear e Recursivo):**
  - Números primos lineares calculam todos os primos até um número fornecido usando loops.
  - Números primos recursivos calculam primos até um número fornecido usando recursão.
- Interface web com suporte a mensagens para enviar comandos e visualizar os resultados.

## Tecnologias Utilizadas
- **Backend:** Flask, Flask-SocketIO
- **Frontend:** HTML, CSS, JavaScript, Socket.IO

## Configuração e Execução

### Pré-requisitos
- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://seu-repositorio-aqui.git
   cd seu-repositorio
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando o Projeto
1. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
2. Acesse a aplicação em seu navegador no endereço:
   ```
   http://localhost:5000
   ```

## Como Usar
1. Abra a página principal.
2. Selecione uma função no menu suspenso (exemplo: Fibonacci Linear, Números Primos Recursivo).
3. Insira um número no campo de entrada.
4. Clique no botão "Enviar" para ver os resultados no chat.


## Observações
- Certifique-se de que o Flask e o SocketIO estão instalados corretamente.
- A aplicação está configurada para rodar em ambiente local. Para disponibilizar em produção, utilize um servidor web adequado (como Gunicorn ou uWSGI) e um proxy reverso.

---

Sinta-se à vontade para relatar problemas!

