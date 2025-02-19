from threading import Thread


def contar(nome, n):
    for i in range(n):
        print(nome, i)


def contar_depois(t1, t2):
    contar(2, 100)
    print('Aguardando t2')
    t2.join()
    print('Aguardando t1')
    t1.join()
    print('Depois do join')
    contar(2, 100)


threads = tuple(Thread(target=contar, args=(i, 100)) for i in range(1, 3))
depois_t = Thread(target=contar_depois, args=threads)

for t in threads:
    t.start()
depois_t.start()
