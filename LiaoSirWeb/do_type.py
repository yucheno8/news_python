class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()

print(type(Hello))
print(type(h))


print('\n==========')
# 要创建一个class对象，type()函数依次传入3个参数：
#
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hi上。
def fn(self, name='jack'): # 先定义函数
    print('Hi, %s.' % name)

Hi = type('Hi', (object,), dict(hi=fn)) # 创建Hi class
h = Hi()
h.hi()

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

print(type(Hi))
print(type(h))

