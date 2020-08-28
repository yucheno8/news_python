from functools import reduce

def str2float(s):
    dotdigit = s.index('.')
    s = list(s)
    s.remove('.')
    def fn(x,y):
        return x*10+y
    return reduce( fn ,map(int,s))/(10**dotdigit)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')