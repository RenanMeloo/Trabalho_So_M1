from multiprocessing import Pipe
import time

def cliente2(conn):
    comandos = [
        "INSERT 1 João",
        "INSERT 2 Maria",
        "DELETE 1",
        "SELECT 2",
        "INSERT 1 João",
        "INSERT 2 Maria",
        "DELETE 1",
        "SELECT 2",
        "INSERT 1 João",
        "INSERT 2 Maria",
        "DELETE 1",
        "SELECT 2"
    ]

    for cmd in comandos:
        print(f"[CLIENTE2] Enviando: {cmd}")
        conn.send(cmd)
        time.sleep(1)

    conn.send("FIM")  
