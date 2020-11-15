from io import BytesIO
f = BytesIO()
s = f.write('中文'.encode('utf-8'))
print(s)
print(f.getvalue())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
