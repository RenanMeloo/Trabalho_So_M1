from multiprocessing import Pipe, Process
from multiprocessing.connection import wait
import threading
import time
from Banco import BancoDeDados

def tratar_requisicao(conn, banco):
    while True:
        comando = conn.recv()
        if comando == "FIM":
            break
        print(f"[SERVIDOR] Recebido: {comando}")
        partes = comando.strip().split()
        if partes[0] == "INSERT":
            banco.inserir(int(partes[1]), partes[2])
        elif partes[0] == "DELETE":
            banco.delete(int(partes[1]))
        elif partes[0] == "SELECT":
            banco.select(int(partes[1]))
        elif partes[0] == "EDIT":
            banco.edit(int(partes[1]), partes[2])
        else:
            print("[SERVIDOR] Comando inválido")

def servidor(conns):
    banco = BancoDeDados()
    while True:
        prontos = wait(conns)
        for conn in prontos:
            threading.Thread(target=tratar_requisicao, args=(conn, banco)).start()
