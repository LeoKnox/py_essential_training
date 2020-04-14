import platform

#print('This is python version {}'.format(platform.python_version()))

#alternate version
def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()