import socket
import threading

# Função para manipular as conexões dos clientes
def handle_client(client_socket):
    request = client_socket.recv(1024)  # Recebe dados do cliente
    print(f"Recebido: {request.decode('utf-8')}")  # Exibe a mensagem recebida
    # Aqui você pode adicionar lógica para processar a mensagem conforme necessário
    # Por exemplo, roteamento para diferentes serviços com base na mensagem recebida.
    client_socket.close()  # Fecha a conexão com o cliente após processamento

def main():
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 9999  # Porta a ser usada pelo servidor

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket
    server.bind((host, port))  # Associa o servidor ao endereço e porta especificados
    server.listen(5)  # Começa a escutar por conexões, com no máximo 5 clientes em espera

    print(f"[*] Servidor escutando em {host}:{port}")

    while True:
        client, addr = server.accept()  # Aceita a conexão do cliente
        print(f"[*] Conexão aceita de {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))  # Cria uma nova thread para lidar com o cliente
        client_handler.start()  # Inicia a thread

if __name__ == "__main__":
    main()
