def main():
    a = set("set one")
    b = set("set two")
    print_set(a)
    print_set(b)
    print_set(a - b)
    print_set(a | b)
    print_set(a ^ b) # exclusive or
    print_set(a & b)

def print_set(o):
    print('{', end = '')
    for x in o:
        print(x, end = '')
    print('}')

if __name__ == '__main__': main()