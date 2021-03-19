# Program-like in Cafe

### 80桁の乱数を0.2秒毎に出力するプログラム(do_in_cafe.py)
```python
import random
import time

value = list()
for i in range(50):
    value.append(random.randint(10**79,10**80))

for k in range(1000):
    x = random.randint(0,49)
    print(value[x])
    time.sleep(0.2)
```


