import time

import pyautogui


def nao_ficar_afk(intervalo=60):
    """
    Simula um pequeno movimento do mouse a cada 'intervalo' segundos para evitar que o sistema marque o usuário como inativo.
    """
    try:
        while True:
            # Salva a posição atual do mouse
            pos_x, pos_y = pyautogui.position()

            # Move o mouse para a direita e depois volta à posição original
            pyautogui.move(10, 0, duration=0.1)
            pyautogui.move(-10, 0, duration=0.1)

            # Retorna para a posição original (opcional, já que o movimento já foi revertido)
            pyautogui.moveTo(pos_x, pos_y, duration=0.1)

            # Espera pelo intervalo especificado
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")


if __name__ == "__main__":
    # Define o intervalo de 60 segundos (pode ser ajustado conforme necessário)
    nao_ficar_afk(60)
