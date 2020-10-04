## 学习笔记



### 面向对象编程

• 现实世界的对象和 Python 世界的对象

• 对象是一个**数据**以及**相关行为**的**集合**

• Python 的**经典类**与**新式类**（2.2以后默认都是新式类，不管写不写object）

• 类的两大成员： 属性和方法



### 属性

• 类属性与对象属性

• 类属性字段在内存中只保存一份**（静态字段）**

• 对象属性在每个对象都保存一份

```python
class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):
        # 普通字段
        self.name = name
        
# 有静态字段,live属性
Human.__dict__
# 有普通字段,name属性
man.__dict__

# 实例可以使用普通字段也可以使用静态字段
man.name
man.live = False
# 查看实例属性
man.__dict__ #普通字段有live变量
man.live
woman.live

# 类可以使用静态字段
Human.live

# 可以为类添加静态字段
Human.newattr = 1
dir(Human)
Human.__dict__

# 内置类型不能增加属性和方法
setattr(list, 'newattr', 'value')
# TypeError

# 显示object类的所有子类
print( ().__class__.__bases__[0].__subclasses__() )
```

如果静态字段在实例中如果进行了修改，在实例中进行了创建，已经不是类的静态字段。

man.live = False

Human.live  True

woman.live True



```python
class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

# 不同内存地址，两个不同对象
type(a)
id(a)
a.__class__()
b.__class__()

# 类也是对象
c = MyFirstClass
d = c()
d.__class__()
```

dir函数，得到类的属性列表

```python
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'live', 'newattr']
```



### 属性作用域

作用域：

>   • _name  **人为**约定不可修改

>   • __name  **私有**属性

>   • `__name__` 魔术方法

魔术方法：

>   • **双下划线开头和结尾的方法，实现了类的特殊成员**，这类称作魔术方法
>
>   • **不是所有的**双下划线开头和结尾的方法**都是魔术方法**
>
>   • **魔术方法类似其他语言的接口**
>
>   私有属性是可以访问到的，Python 通过改名机制隐藏了变量名称

```python
print( ().__class__.__bases__[0].__subclasses__() )  # 显示object类的所有子类
```



### 方法

#### 三种方法：

• 普通方法 至少一个 **self 参数**，表示该方法的**对象**，代表不同的实例

• 类方法 至少一个 **cls 参数**，表示该方法的**类**，代表当前的类  @classmethod

用法：当你的类需要一系列的构造环节的时候。由于python类中只能有一个初始化方法，不能按照不同的情况初始化类

```python
class Kls2():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me = Kls2('wilson','yin')
me.print_name()

# 输入改为  wilson-yin 如果用户的参数和类的参数不同的时候，三种解决方法。

解决方法1: 修改 __init__() 来适应新的输入，重构程序。不优雅。
解决方法2: 增加 __new__() 构造函数
解决方法3: 增加 提前处理的函数

obj 类 name 名字
    
def pre_name(obj,name):
    fname, lname = name.split('-')
    return obj(fname, lname)

me2 = pre_name(Kls2, 'wilson-yin')
me2.print_name()


# 改进

class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @classmethod
    def pre_name(cls,name):
        fname, lname = name.split('-')
        return cls(fname, lname)
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me3 = Kls3.pre_name('wilson-yin')
me3.print_name()


'''
类方法用在模拟java定义多个构造函数的情况。
由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。
'''
class Book(object):
    def __init__(self, title):
        self.title = title
    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book


book1 = Book("python")
book2 = Book.create("python and django")
print(book1.title)
print(book2.title)
```

调用父类方法：

```python
class Fruit(object):
    total = 0
    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))
    @classmethod
    def set(cls, value):
        print(f'calling {cls} ,{value}')
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

Apple.set(100)
# calling <class '__main__.Apple'> ,100
Orange.set(200)
# calling <class '__main__.Orange'> ,200
org=Orange()
org.set(300)
```

• **静态方法 由类调用，无参数** @staticmethod

用来做一些功能的转化和判断，不是一条语句能够写完的，额外处理的一些内容。这种情况下采取使用staticmethod。

没有cls和self，不能引用类的属性。

```python
import datetime
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 静态的方法
    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2 :
            print('god is coming')
        else:
            print('god is going')

Story.god_come_go()

```

**三种方法在内存中都归属于类**



### 特殊属性与方法

#### • __init__()

>   • __init__() 方法所做的工作是在类的对象创建好**之后**进行变量的**初始化**。 
>
>   • __init__() 方法**不需要显式返回**，默认为 None，否则会在运行时抛出 TypeError。 

#### • self

>   • self 表示实例对象本身
>
>   • self 不是 Python 的关键字（cls也不是），可以将 self 替换成任何你喜欢的名称，
>
>   如 this、obj 等，实际效果和 self 是一样的（不推荐）。 
>
>   • 在方法声明时，需要定义 self 作为第一个参数，调用方法的时候不用传入 self。



### 属性的处理

#### 在类中，需要对**实例获取属性**这一行为进行操作，可以使用：

>   • __getattribute__() 
>
>   • __getattr__()

#### 异同：

>   • 都可以对实例属性进行获取拦截
>
>   • __getattr__() 适用于**未定义**的属性，**`__dict__`还是没有这个属性。**
>
>   • __getattribute__() 对**所有属性**的访问都会调用该方法
>
>   **如果同时存在，执行顺序是 getattribute > getattr > dict**

```python
>>> class Human2(object):
...     def __getattribute__(self, item):
...         """
...         将不存在的属性设置为100并返回,模拟getattr行为
...         """
...         print('Human2:__getattribute__')
...         try:
...             return super().__getattribute__(item)
...         except Exception as e:
...             self.__dict__[item] = 100
...             return 100
...
>>>
>>>
>>> h1 = Human2()
>>>
>>> print(h1.noattr)
Human2:__getattribute__
Human2:__getattribute__
100

```



### 属性描述符 property

#### 描述符：实现特定协议的类

#### property 类需要实现 __get__、__set__、 __delete__ 方法

将方法封装成属性，只考虑赋值和读取，删除属性即可。经常会用到。

被装饰函数建议使用相同的名字

使用setter 并不能真正意义上实现无法写入，gender被改名为 _Article__gender

property本质并不是函数，而是特殊类（实现了数据描述符的类）

如果一个对象同时定义了__get__()和__set__()方法，则称为数据描述符，

如果仅定义了__get__()方法，则称为非数据描述符

property的优点：
1 代码更简洁，可读性、可维护性更强。
2 更好的管理属性的访问。
3 控制属性访问权限，提高数据安全性。



### 面向对象编程的特性

#### 封装

• 将内容封装到某处

• 从某处调用被封装的内容

#### 继承

• 基本继承

• 多重继承

#### 重载

• Python 无法在语法层面实现数据类型重载，需要在代码逻辑上实现

• Python 可以实现参数个数重载

#### 多态

• Pyhon 不支持 Java 和 C# 这一类强类型语言中多态的写法，

• Python 使用“鸭子类型”



### 新式类

#### 新式类和经典类的区别

• 当前类或者父类继承了 object 类，那么该类便是新式类，否则便是经典类

#### object 和 type 的关系

• object 和 type **都属于 type 类** (class 'type')

• type 类由 type 元类自身创建的。object 类是由**元类 type** 创建

• **object 的父类为空，没有继承任何类**

• **type 的父类为 object 类 (class 'object')**



### 类的继承

#### • 单一继承 a b

#### • 多重继承 a b c

#### • 菱形继承（钻石继承）

#### • 继承机制 MRO

#### • MRO 的 C3 算法

>   ##### Python的方法解析顺序(MRO)
>
>   ##### https://hanjianwei.com/2013/07/25/python-mro/



### SOLID 设计原则

• 单一责任原则 The Single Responsibility Principle

• 开放封闭原则 The Open Closed Principle

• 里氏替换原则 The Liskov Substitution Principle

• 依赖倒置原则 The Dependency Inversion Principle

• 接口分离原则 The Interface Segregation Principle



### 设计模式

• 设计模式用于解决普遍性问题

• 设计模式保证结构的完整性



### 单例模式

#### 1. 对象只存在一个实例

#### 2. __init__ 和 __new__ 的区别：

• __new__ 是**实例创建之前被调用**，返回该实例对象，是**静态方法**

• __init__ 是**实例对象创建完成后被调用，是实例方法**

• __new__ 先被调用，__init__ 后被调用

• __new__ 的返回值（实例）将传递给 __init__ 方法的第一个参数，__init__ 给这个实例设置相关参数



### 元类

• 元类是关于类的类，是类的模板。

• 元类是用来控制如何创建类的，正如类是创建对象的模板一样。

• 元类的实例为类，正如类的实例为对象

• 创建元类的两种方法

>   1.  class
>
>   2.  type
>
>       • type（类名，父类的元组（根据继承的需要，可以为空，包含属性的字典（名字和值））



### 抽象基类

• 抽象基类（abstract base class，ABC）用来确保派生类实现了基类中的特定方法。

• 使用抽象基类的好处：

>   • 避免继承错误，使类层次易于理解和维护。
>
>   • 无法实例化基类。
>
>   • 如果忘记在其中一个子类中实现接口方法，要尽早报错。

```python
from abc import ABC
class MyABC(ABC):
	pass

MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
```



### Mixin 模式

在程序运行过程中，重定义类的继承，即动态继承。好处：

• 可以在不修改任何源代码的情况下，对已有类进行扩展进行组件的划分

