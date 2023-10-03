import socket

import requests

server = socket.socket()
server.bind((socket.gethostbyname(socket.gethostname()), 5000))
server.listen(5)

while True:
    conn, adr = server.accept()
    gt = conn.recv(1024)
    url = ""
    method = ""
    try:
        url = gt.decode().splitlines()[1].split("Host: ")[1]
        method = gt.decode().split(" ")[0]
    except Exception:
        pass

    if not url.startswith("https://") or not url.startswith("http://"):
        url = "https://" + url

    print(url, method)

    if method == "GET":
        print(1)
        result = requests.get(url)
        print(result.content.decode())
        conn.send(result.content)

    elif method == "POST":
        result = requests.post(url)
        conn.send(result.text.encode())

    elif method == "PUT":
        result = requests.put(url)
        conn.send(result.text.encode())

    elif method == "DELETE":
        result = requests.delete(url)
        conn.send(result.text.encode())


        
