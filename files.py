def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())
    g = open('lines.txt', 'r+t') # optional + allows read/write optional t/b opens text binary
    h = open('lines.txt', 'w') #write mode deletes file when opened
    i = open('lines.txt', 'a')

if __name__ == '__main__': main()