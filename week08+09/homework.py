"""
作业一：区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list tuple str dict collections.deque

答：
容器序列：list tuple dict collections.deque
扁平序列：str

可变序列:list dict collections.deque
不可变序列:str tuple
"""


"""
作业二：自定义一个 python 函数，实现 map() 函数的功能。
"""


def my_map_yield(fun, *seqs):
    for args in zip(*seqs):
        yield fun(*args)


def my_map_return(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def testfun(x, y):
    return x*y


def testfun2(x, y, z):
    return x*y*z


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = [1, 3, 4, 5]


list(my_map_yield(testfun, x, y))
list(my_map_return(testfun, x, y))


list(my_map_yield(testfun2, x, y, z))
list(my_map_return(testfun2, x, y, z))


"""
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""


def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print(f'{func.__name__} 运行时间：{time_spend}秒')
        return result
    return func_wrapper


@timer
def testfun(x, y, z):
    return x**y**z


@timer
def testfun2(x, y):
    return x**y


testfun(2, 2, 2)
testfun2(100, 100)
