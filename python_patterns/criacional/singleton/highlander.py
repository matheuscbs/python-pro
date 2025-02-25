from threading import RLock


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        with RLock():
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def apaga(self):
        return 'Apagando dados do BD de prod'


class SubSingleton(Singleton):
    def apaga(self):
        return 'Não apagando nada'


if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = SubSingleton()
    print(id(obj1))
    print(id(obj2))
    print(obj1.apaga())
    print(type(obj2))
    print(type(obj1))
