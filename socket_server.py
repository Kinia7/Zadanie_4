import socket
import json
import os

def udp_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP server is listening on {host}:{port}")

        while True:
            data, address = server_socket.recvfrom(1024)
            print(f"Received data from {address}: {data.decode()}")

            # Przetwarzanie danych do słownika
            try:
                data_dict = json.loads(data.decode())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue

            # Zapisywanie danych do pliku JSON
            save_to_json(data_dict)

def save_to_json(data_dict):
    storage_folder = "storage"
    if not os.path.exists(storage_folder):
        os.makedirs(storage_folder)

    file_path = os.path.join(storage_folder, "data.json")
    with open(file_path, "w") as file:
        json.dump(data_dict, file)
        print(f"Data saved to {file_path}")

HOST = '127.0.0.1'
PORT = 5000

udp_server(HOST, PORT)
