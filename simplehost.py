import socket

host = "127.0.0.2"
port=1234
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port));
        s.listen();
        print("[%]Started Server On: Host[{}], PORT[{}]".format(host, port))
        conn, addr = s.accept()
        print("[%]Accepted Connection From: {}".format(addr))
        data = conn.recv(1024)
        print(data)