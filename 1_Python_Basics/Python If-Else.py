# Problem link: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n&1:
        print("Weird")
    elif not n&1 and 2 <= n <= 5:
        print("Not Weird")
    elif not n&1 and 6 <= n <= 20:
        print("Weird")
    elif not n&1 and n > 20:
        print("Not Weird")
