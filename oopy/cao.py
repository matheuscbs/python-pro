class Mamifero:
    """Vertebrados dotados de glândulas mamárias"""


class Cao(Mamifero):
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def latir(self, vezes=1):
        # Quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print(self.nome + ':' + ' Au!' * vezes)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao(%r)' % self.nome

    def __eq__(self, outro):
        return (isinstance(outro, Cao) and
                self.__dict__ == outro.__dict__)


class Pequines(Cao):
    """ O pequinês está normalmente nervoso:

         >>> fido = Pequines('Fido')
         >>> fido.latir()
         Fido: Au! Au!
    """
    nervoso = True


class GrandeMixin(object):
    """ Mixin: muda o latido"""
    def latir(self, vezes=1):
        # faz de conta que cães grandes não mudam
        # seu latido quando nervosos
        print(self.nome + ':' + ' Wuff!' * vezes)


class Mastiff(GrandeMixin, Cao):
    """ O mastiff late diferente:

         >>> atos = Mastiff('Atos')
         >>> atos.latir()
         Atos: Wuff!
    """


class SaoBernardo(GrandeMixin, Cao):
    """O São Bernardo serve conhaque:

        >>> sansao = SaoBernardo('Sansao')
        >>> sansao.latir()
        Sansao: Wuff!
        >>> sansao.servir()
        Sansao serve o conhaque (restam 9 doses)
        >>> sansao.doses = 1
        >>> sansao.servir()
        Sansao serve o conhaque (restam 0 doses)
        >>> sansao.servir()
        Traceback (most recent call last):
          ...
        ValueError: Acabou o conhaque!
    """

    def __init__(self, nome):
        Cao.__init__(self, nome)
        self.doses = 10

    def servir(self):
        if self.doses == 0:
            raise ValueError('Acabou o conhaque!')
        self.doses -= 1
        msg = '{0} serve o conhaque (restam {1} doses)'
        print(msg.format(self.nome, self.doses))
