from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    sizedict = {'微型': 0,
                '小型': 1,
                '中型': 2,
                '大型': 3,
                '巨型': 4}

    @abstractmethod
    def __init__(self, name, kind, size, characteristic):
        self.name = name
        self.kind = kind
        self.size = size
        self.characteristic = characteristic

    @classmethod
    def cry(cls):
        print(f'{cls.crysound}')

    @property
    def ferocious(self):
        if (self.kind == '食肉' and
            self.sizedict[self.size] >= self.sizedict['中型'] and
                self.characteristic == '凶猛'):
            return True
        else:
            return False

    @property
    def suitability_as_pet(self):
        return not self.ferocious
