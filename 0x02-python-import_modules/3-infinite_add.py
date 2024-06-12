#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    args = sys.argv[1: ]
   ## if len(args) < 1:
     ##   print("0")
    print(sum(map(int, args)))
