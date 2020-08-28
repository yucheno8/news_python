class Student(object):

    def __init__(self):
        self.name = 'Michael'

# 返回未定义的属性
    # def __getattr__(self, attr):
    #     if attr == 'score':
    #         return 99
# ！注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 返回函数
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25

s = Student()
print(s.name)
print(s.age())

# ！注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
print(s.abc)