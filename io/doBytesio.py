
from io import BytesIO;

f = BytesIO()
# print(f.read())
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = 'Hey. My name KeyXK.I\'m to coder.I\'m to nineteen years old!'.encode('utf-8')
f = BytesIO(data)
print(f.read())