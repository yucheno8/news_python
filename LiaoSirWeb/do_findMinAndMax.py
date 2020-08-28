def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    i = L[0]
    k = L[0]
    for m in L:
        i = min(i,m)
        k = max(k,m)
    return (i, k)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')