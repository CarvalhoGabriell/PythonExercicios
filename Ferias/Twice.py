


def do_twice(f):
    f()
    f()

def print_apan():
    print('SPAM')

#do_twice(print_apan)

def do_four(f):
    do_twice(f)
    do_twice(f)

do_four(print_apan)