def main():
    x = 'meow', 'hiss', 'purrr'
    kitten(*x)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('yakk')

if __name__ == '__main__': main()