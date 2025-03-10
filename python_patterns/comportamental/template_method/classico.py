from abc import ABC, abstractmethod


class AbstractSpam(ABC):
    def enviar_spam_para_todos_usuarios(self, msg):
        # Obter uma lista de contatos
        for nome, endereco in self.obter_contatos():
            # Para cada usuário, enviar uma msg pelo canal
            self.enviar_mensagem(nome, endereco, msg)

    @abstractmethod
    def obter_contatos(self):
        """
            Deve retornar uma lista onde cada elemento é uma tupla.
            O primeiro elemento da tupla é o nome do contato e o segundo o seu endereço no respectivo canal
            de envio de mensagem
        """
        pass

    @abstractmethod
    def enviar_mensagem(self, nome, endereco, msg):
        """Deve enviar mensagem para usuario
            :param nome: str com nome do usuário
            :param endereco: str com endereco do usuário no canal
            :param msg: str mensagem a ser enviada
            :return: booleano indicando se mensagem foi enviada ou não
        """
        pass


if __name__ == '__main__':
    class SpamParaConsole(AbstractSpam):
        def obter_contatos(self):
            # Retornando uma lista correta de tuplas (nome, endereço)
            return [('Matheus', 'matheus@email.com'), ('João', 'joao@email.com')]

        def enviar_mensagem(self, nome, endereco, msg):
            print(f'Msg para {nome} no endereço {endereco}: {msg}')

    spam_para_console = SpamParaConsole()
    spam_para_console.enviar_spam_para_todos_usuarios('Olá Template Method')
