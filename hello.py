def main():
    try:
        x = 7/0
    except ValueError:
        print('Value error stupid .. V A L U E   E R R O R')
    except ZeroDivisionError:
        print('don\'t divide by 0 zero')
    else:
        print('Works move along')
        print(x)

if __name__ == '__main__': main()