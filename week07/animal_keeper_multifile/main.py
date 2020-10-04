from zoo import Zoo
from cat import Cat
from dog import Dog

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
