import random
import time
import shutil


terminal_size = shutil.get_terminal_size()


value = list()
for i in range(50):
    value.append(random.randint(10**(terminal_size.columns-1),10**terminal_size.columns))

for k in range(5000):
    x = random.randint(0,49)
    print(value[x])
    time.sleep(0.2)
