# Decorators
# can be used for log test performance, perform caching, verify permissions, etc.. Can also be used when you run the same code on multiple functions

def logtime(func):
    def wrapper():
        print('<- header ->')
        val = func()
        print('>- footer -<')
        return val
    return wrapper

@logtime
def hello():
    print('Hello')

hello()