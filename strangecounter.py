#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    start = 1
    counter = 1
    while t >= start:
        start = (3*counter) + start
        counter = counter * 2
    print(start)
    result = 3
    if t == start:
        for i in range(start):
            result = result * 2
        return result
    else:
         return start - t
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

