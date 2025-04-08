import threading
from threading import Semaphore
class BancoDeDados:
    def __init__(self):
        self.registros = []
        self.lock = threading.Lock()

    def inserir(self, id, nome):
        with self.lock:
            for registro in self.registros:
                if registro['id'] == id:
                    print(f"[ERRO] ID {id} já existe! Inserção ignorada.")
                    return
            novo_registro = {'id': id, 'nome': nome}
            self.registros.append(novo_registro)
            print(f"Registro inserido: {novo_registro}")

    def delete(self, id):
        with self.lock:
            for registro in self.registros:
                if registro['id'] == id:
                    self.registros.remove(registro)
                    print(f"Registro removido: {registro}")
                    return
            print(f"[ERRO] Registro com id={id} não encontrado.")

    def select(self, id):
        with self.lock:
            for registro in self.registros:
                if registro['id'] == id:
                    print(f"Registro encontrado: {registro['id']}, {registro['nome']}")
                    return registro
            print(f"[ERRO] Não foi possível encontrar o id={id}")
            return None

    def edit(self, id, novo_nome):
        with self.lock:
            for registro in self.registros:
                if registro['id'] == id:
                    registro['nome'] = novo_nome
                    print(f"Registro editado com sucesso: {registro['id']}, {registro['nome']}")
                    return
            print(f"[ERRO] Não encontramos ninguém com o ID {id}")
