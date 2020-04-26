def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'expected one argument got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expect at most 3 got {numargs} args')

    i = start
    while i <= stop:
        yield i
        i += step
def main():
    try:
        for i in inclusive_range(25, 1, 1, 1, 1):
            print(i, end = ' ')
        print()
    except TypeError as e:
        print (f'range error: {e}')

if __name__ == '__main__': main()