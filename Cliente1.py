from multiprocessing import Pipe
import time

def cliente1(conn):
    comandos = [
        "INSERT 2 ana",
        "EDIT 1 pedro"
    ]

    for cmd in comandos:
        print(f"[CLIENTE1] Enviando: {cmd}")
        conn.send(cmd)
        time.sleep(1)

    conn.send("FIM")  
