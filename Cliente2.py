from multiprocessing import Pipe
import time

def cliente2(conn):
    comandos = [
        'INSERT 1 Joao',
        "SELECT 1"
    ]

    for cmd in comandos:
        print(f"[CLIENTE2] Enviando: {cmd}")
        conn.send(cmd)
        time.sleep(1)

    conn.send("FIM")  
