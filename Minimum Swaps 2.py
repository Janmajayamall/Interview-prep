#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):


def minimumSwaps(arr):
    count = 0
    i = 0

    while(i<len(arr)):

        if (i+1)!=arr[i]:
            temp = arr[arr[i]-1]
            arr[arr[i]-1]=arr[i]
            arr[i]=temp
            count+=1
            continue
        i+=1

    return count

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
