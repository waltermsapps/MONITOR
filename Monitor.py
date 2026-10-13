import urllib.request
import urllib.error
import socket
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
ENDPOINTS = [
    {"id": 1, "name": "Meu Servidor Local", "url": "https://www.google.com.br"},
    {"id": 2, "name": "API Externa (Simula OK)", "url": "https://httpbin.org/status/200"},
    {"id": 3, "name": "API Externa (Simula OK2)", "url": "https://httpbin.org/status/200"},
    {"id": 4, "name": "API Externa (Simula Erro)", "url": "https://www.google.com"}
]

TEMPO_ATUALIZACAO = 10  # Tempo entre as checagens em segundos
TEMPO_MAXIMO = 5        # Timeout de 5 segundos
PORTA_SERVIDOR = 8501   # Porta para acessar no navegador

def checar_endpoint(endpoint):
    """Faz a requisição HTTP e retorna o status (Mantido do original)"""
    url_base = endpoint["url"]
    timestamp = int(time.time())
    url_check = f"{url_base}&_t={timestamp}" if "?" in url_base else f"{url_base}?_t={timestamp}"
    
    req = urllib.request.Request(url_check, headers={
        'User-Agent': 'Sysadmin-Monitor/1.0',
        'Cache-Control': 'no-cache'
    })
    
    try:
        resposta = urllib.request.urlopen(req, timeout=TEMPO_MAXIMO)
        return True, f"HTTP {resposta.getcode()}"
    except urllib.error.HTTPError as erro:
        return False, f"HTTP {erro.code}"
    except urllib.error.URLError as erro:
        if isinstance(erro.reason, socket.timeout):
            return False, "Timeout (Sem resposta em 5s)"
        else:
            return False, "Conexão Recusada ou Falha de DNS"
    except Exception as erro:
        return False, f"Erro: {str(erro)}"
class MonitorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Responde que a requisição foi um sucesso
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Início do HTML com CSS básico para deixar bonito
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Painel de Monitoramento</title>
            <!-- A tag abaixo faz a página dar refresh automático -->
            <meta http-equiv="refresh" content="{TEMPO_ATUALIZACAO}">
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; }}
                .container {{ max-width: 800px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
                h1 {{ text-align: center; color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
                .card {{ border: 1px solid #e1e1e1; border-radius: 6px; padding: 15px; margin-bottom: 15px; display: flex; align-items: center; }}
                .card.online {{ border-left: 5px solid #2ecc71; }}
                .card.offline {{ border-left: 5px solid #e74c3c; background-color: #fdf2f2; }}
                .badge {{ padding: 6px 12px; color: #fff; font-weight: bold; border-radius: 4px; margin-right: 20px; min-width: 80px; text-align: center; }}
                .badge.online {{ background-color: #2ecc71; }}
                .badge.offline {{ background-color: #e74c3c; }}
                .details {{ flex-grow: 1; }}
                .details strong {{ font-size: 1.1em; display: block; margin-bottom: 5px; }}
                .details span {{ font-size: 0.9em; color: #555; display: block; }}
                .footer {{ text-align: center; margin-top: 20px; font-size: 0.85em; color: #7f8c8d; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌐 Painel de Monitoramento</h1>
        """

        # Checa cada endpoint e cria um "card" na interface
        for item in ENDPOINTS:
            sucesso, mensagem = checar_endpoint(item)
            
            status_class = "online" if sucesso else "offline"
            status_text = "ONLINE" if sucesso else "OFFLINE"

            html_content += f"""
                <div class="card {status_class}">
                    <div class="badge {status_class}">{status_text}</div>
                    <div class="details">
                        <strong>{item['name']}</strong>
                        <span><b>URL:</b> {item['url']}</span>
                        <span><b>Status:</b> {mensagem}</span>
                    </div>
                </div>
            """

        # Rodapé com a hora
        hora_atual = datetime.now().strftime('%H:%M:%S')
        html_content += f"""
                <div class="footer">
                    Última atualização: {hora_atual} <br>
                    Próxima checagem automática em {TEMPO_ATUALIZACAO} segundos.
                </div>
            </div>
        </body>
        </html>
        """

        # Envia o HTML para o navegador
        self.wfile.write(html_content.encode('utf-8'))

    # Oculta os logs do servidor HTTP no terminal para não poluir
    def log_message(self, format, *args):
        pass

def iniciar_servidor():
    """Inicia o servidor web local"""
    server_address = ('', PORTA_SERVIDOR)
    httpd = HTTPServer(server_address, MonitorHandler)
    print(f"=== Servidor Iniciado ===")
    print(f"Abra o seu navegador e acesse: http://localhost:{PORTA_SERVIDOR}")
    print("Pressione Ctrl+C no terminal para parar o monitoramento.")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado com sucesso.")
        httpd.server_close()

if __name__ == "__main__":
    socket.setdefaulttimeout(TEMPO_MAXIMO)
    iniciar_servidor()