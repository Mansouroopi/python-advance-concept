def outer(msg):
    print('i am outer...')
    def inner():
        print('print from inner {}'.format(msg))
    return inner


hi = outer('Hi')
hi()
