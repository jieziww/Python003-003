from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    size_dict = {'微型': 0,
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
        print(f'{cls.cry_sound}')

    @property
    def ferocious(self):
        if (self.kind == '食肉' and
            self.size_dict[self.size] >= self.size_dict['中型'] and
                self.characteristic == '凶猛'):
            return True
        else:
            return False

    @property
    def suitability_as_pet(self):
        return not self.ferocious


class Cat(Animal):
    cry_sound = "喵喵~"

    def __init__(self, name, kind, size, characteristic):
        super().__init__(name, kind, size, characteristic)


class Dog(Animal):
    cry_sound = "汪汪~"

    def __init__(self, name, kind, size, characteristic):
        super().__init__(name, kind, size, characteristic)


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            setattr(self, animal.__class__.__name__, 'yes')
        else:
            print(f'已经有{animal.name}了，同一只动物不能重复添加！')


if __name__ == '__main__':

    z = Zoo('时间动物园')  # 实例化动物园

    # 动物初始化，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小型', '温顺')
    cat2 = Cat('大花猫 2', '食肉', '小型', '温顺')
    dog1 = Dog('小黄狗 1', '食肉', '小型', '凶猛')
    dog2 = Dog('大狼狗 1', '食肉', '中型', '凶猛')

    z.add_animal(cat1)  # 增加一只猫到动物园

    have_cat = hasattr(z, 'Cat')  # 动物园是否有猫这种动物
    if have_cat:
        print("动物园有猫")

    z.add_animal(cat1)  # 重复添加同一只动物

    have_dog = hasattr(z, 'Dog')
    if have_dog:
        print("动物园有狗")
    else:
        print("动物园还没有狗")

    z.add_animal(dog1)  # 添加一只狗再测试
    have_dog = hasattr(z, 'Dog')
    if have_dog:
        print("动物园有狗")

    z.add_animal(cat2)
    z.add_animal(dog2)
    z.add_animal(dog1)

    for animal in z.animals:
        animal.cry()
        print(f'是否适合当宠物 {animal.name}:{animal.suitability_as_pet}')
