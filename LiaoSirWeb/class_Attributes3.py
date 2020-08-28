class Student(object):

    count = 0

    def __init__(self, name):

        self.name = name

        Student.add_count()

    # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）

    def add_count():

        Student.count += 1  # 属性是可以直接用类本身调用的

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