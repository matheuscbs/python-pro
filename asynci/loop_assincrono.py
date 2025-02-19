from time import sleep, strftime

from asynci.loop import (ESPERANDO, executar_aleatoriamente, executar_depois,
                         iniciar_loop_de_eventos_assincrono)

fmt = '%H:%m:%S'
inicio = strftime(fmt)


def executar_em_intervalo():
    agora = strftime(fmt)
    print('Criada em %s executada em %s' % (inicio, agora))


tarefas = []
tarefas.append(executar_depois(executar_em_intervalo, 5))
tarefas.append(executar_depois(executar_em_intervalo, 2))
tarefas.append(executar_aleatoriamente(executar_em_intervalo))

iniciar_loop_de_eventos_assincrono()


while any((t.status == ESPERANDO for t in tarefas)):
    print('Mandando Bala na CPU')
    print('Tarefas: %s' % tarefas)

    sleep(1)
