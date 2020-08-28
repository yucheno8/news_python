L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)

print("------------")
l = list(range(1,100,2))
print(l)
print(l[:int(len(l)/2)])
print(l[-int(len(l)/2):-1])

print("------------")
#列表生成式1
L = list(range(1,100,2))
print(L)

#列表生成式2
list = [i for i in range(1,101) if i%2!=0] #range函数包左不包右，右边为101
print(list)

#列表生成式3
list = [i for i in range(1,101,2)]
print(list)
