#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
const = 1 <= n <= 100
if n%2 != 0 and const:
    print("Weird")
elif n%2 == 0 and const and ((n>2)and(n<=5)):
    print("Not Weird")
elif n%2 == 0 and const and ((n>6)and(n<=20)):
    print("Weird")
elif n>20 and const:
    print("Not Weird")
