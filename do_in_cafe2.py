#!/usr/bin/env python
# coding: utf-8


import shutil
import time
import random, string


def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)


tm_size = shutil.get_terminal_size()


for j in range(1000):
    print('#'*(tm_size.columns-6) + ' ' + 'done!')
    time.sleep(0.2)
    print('')
    for l in range(random.randint(1,8)):
        print(randomname(tm_size.columns))
    time.sleep(0.5)
    

    

