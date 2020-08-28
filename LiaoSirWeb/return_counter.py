def createCounter():
    cnt = [0]  # 将cnt设定为数组
    def counter():
        cnt[0] = cnt[0] + 1  # 修改数组中的元素值
        return cnt[0]  # 返回修改的元素值

    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')