def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        #outfile.writelines(line) alternate to print
        print(line.rstrip(), file=outfile) # this strips endings and rewrites for current operating system
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()