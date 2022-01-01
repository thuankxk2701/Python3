
def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))
class Hello2(object):
    pass

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(Hello2) =', type(Hello2))
h2=Hello2();

print('type(h) =', type(h))
print('type(h2) =', type(h2))