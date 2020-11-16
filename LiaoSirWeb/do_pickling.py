#尝试把一个对象序列化写入文件
import pickle
d = dict(name = 'Bob', age = 20, score = 88)
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
s = pickle.dumps(d)
print(s)

#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt','wb')
pickle.dump(d,f)

f.close()
re = f.readline()
print(re)

