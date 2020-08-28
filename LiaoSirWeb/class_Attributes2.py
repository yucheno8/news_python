class Student(object):

    count = 0

    def __init__(self, name):

        self.name = name

        self.add_count()

    # 类方法（不需要实例化类就可以被类本身调用）

    @classmethod

    def add_count(cls):  # cls : 表示没用被实例化的类本身

        cls.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')