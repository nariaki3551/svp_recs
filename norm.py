#!/usr/local/bin/python3
from sys import argv, stdin
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

__doc__ = """
Usage:
    cat base filename | python3 {f} [-n <Int>]

Options:
    -n              上位n行のベクトルのノルムを表示(Default=1)
    -h --help       Show this screen and exit.

Note:
    標準入力の基底のノルムを表示する
""".format(f=__file__)


def usage():
    print(__doc__)
    exit()

def main(n):
    for m, line in enumerate(stdin.readlines()):
        line = line.strip()
        line = line.replace('[', '').replace(']', '')
        if line !='':
            vector = np.array(list(map(float, line.split())))
            print(linalg.norm(vector))
        if m+1 >= n:
            break

if __name__ == '__main__':
    n = 1
    for v in argv[1:]:
        if {'-h', '--help'} & set(v):
            usage()
        if '-n' in v:
            n = int(argv[argv.index('-n')+1])
    main(n)
