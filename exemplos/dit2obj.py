import pytest

# class ObjDct:
#     def __init__(self, dct):
#         self.__dict__ = dct


class ObjDct:
    def __init__(self, dct):
        self._dct = dct

    def __getattr__(self, item):
        if item in self._dct:
            return self._dct[item]


def to_obj(dct):
    return ObjDct(dct)


@pytest.mark.parametrize(
    'dct',
    [
        {'a': 1},
        {'a': 1, 'b': 2, 'c': 3},
    ]
)
def test_acesso_atributos(dct):
    obj = to_obj(dct)
    # assert obj.__dict__ == dct
    for key, value in dct.items():
        assert value == getattr(obj, key, None)
