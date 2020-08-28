def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


max, min = min, max

print(max(1, 2, 3, 4, 5))