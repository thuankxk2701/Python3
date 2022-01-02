import functools;

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__);
        return func(*args,**kw);
    return wrapper;
@log
def now():
    print('2022-1-2');
now();
print(now.__name__);

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2022-1-2')

today()
print(today.__name__)