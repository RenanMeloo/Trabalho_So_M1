from multiprocessing import Process, Pipe
from Servidor import servidor
from Cliente1 import cliente1
from Cliente2 import cliente2

if __name__ == "__main__":
    conn1_servidor, conn1_cliente = Pipe()
    conn2_servidor, conn2_cliente = Pipe()

    p_servidor = Process(target=servidor, args=([conn1_servidor, conn2_servidor],))
    p_servidor.start()

    p_cliente1 = Process(target=cliente1, args=(conn1_cliente,))
    p_cliente2 = Process(target=cliente2, args=(conn2_cliente,))

    p_cliente1.start()
    p_cliente2.start()

    p_cliente1.join()
    p_cliente2.join()

    p_servidor.terminate()
    p_servidor.join()
