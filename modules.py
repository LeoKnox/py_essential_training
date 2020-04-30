import sys
import os

def main():
    v = sys.version_info
    p = sys.platform
    n = os.name
    e = os.getenv('PATH')
    u = os.urandom(25).hex()
    print('Python version {}.{}.{}'.format(*v))
    print(f'Platform: {p}')
    print(n)
    print(e)
    print(u)

if __name__ == '__main__': main()