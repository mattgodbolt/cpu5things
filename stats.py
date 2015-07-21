#!/usr/bin/env python
import time
from argparse import ArgumentParser

def test(array):
    total = 0
    num_clipped = 0
    clipped_total = 0

    for i in array:
        total += i
        if i < 128:
            num_clipped += 1
            clipped_total += i

    return {'avg': total / len(array), 'clipped': clipped_total / num_clipped }

if __name__ == '__main__':
    parser = ArgumentParser(description="Print some data about a file")
    parser.add_argument("file", help="Read data from FILE", metavar="FILE")
    parser.add_argument("--reps", help="Read file NUM times", metavar="NUM", type=int,
            default=50)
    args = parser.parse_args()
    with open(args.file, "r") as inp:
        array = [int(x) for x in inp]
    before = time.time()
    for i in range(args.reps):
        result = test(array)
    after = time.time()
    print "Took %.2fs" % (after - before)
    print result
