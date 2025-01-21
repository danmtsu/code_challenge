from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"
app.config["DEBUG"] = True
socketio = SocketIO(app, cors_allowed_origins="*")

def fibonacci_linear(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibanacci_recursive(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    if n <= 1:
        return n
    return fibanacci_recursive(n - 1) + fibanacci_recursive(n - 2)

def number_primos_linear(n):
    if n <= 1:
        raise ValueError("n must be greater than 1")
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def primes_recursive(n, current=None):
    if current is None:
        current = n
    if n < 2:
        raise ValueError("n must be greater than 1")
    if current < 2:
        return []

    def is_prime(num, divisor=None):
        if divisor is None:
            divisor = int(num ** 0.5)
        if divisor < 2:
            return True
        if num % divisor == 0:
            return False
        return is_prime(num, divisor - 1)

    primes = primes_recursive(n, current - 1)
    if is_prime(current):
        primes.append(current)

    return primes

@socketio.on("message")
def call_functions(mensagem):
    try:
        if mensagem.startswith("fibonacci linear"):
            n = int(mensagem.split()[-1])
            resultado = fibonacci_linear(n)
            send(f"Fibonacci Linear de {n}: {resultado}")
        elif mensagem.startswith("fibonacci recursivo"):
            n = int(mensagem.split()[-1])
            resultado = fibanacci_recursive(n)
            send(f"Fibonacci Recursivo de {n}: {resultado}")
        elif mensagem.startswith("primos linear"):
            n = int(mensagem.split()[-1])
            resultado = number_primos_linear(n)
            send(f"Números primos até {n} (Linear): {resultado}")
        elif mensagem.startswith("primos recursivo"):
            n = int(mensagem.split()[-1])
            resultado = primes_recursive(n)
            send(f"Números primos até {n} (Recursivo): {resultado}")
        else:
            send("Comando não reconhecido. Use: 'fibonacci linear', 'fibonacci recursivo', 'primos linear' ou 'primos recursivo'.")
    except ValueError as e:
        send(f"Erro: {str(e)}")
    except Exception as e:
        send(f"Ocorreu um erro: {str(e)}")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host='localhost')
