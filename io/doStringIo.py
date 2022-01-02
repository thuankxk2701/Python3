


from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('Tes1，\n Test2\ntest3，\ntest4')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())