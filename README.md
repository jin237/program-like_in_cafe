# Program-like in Cafe

### ターミナルの横幅サイズにの桁の乱数を0.2秒毎に出力するプログラム(do_in_cafe.py)
```python
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
```


