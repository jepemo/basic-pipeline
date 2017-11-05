# basic-pipeline
Minimal &amp; Simple Pipeline for Python


```python
from bpipe import pipe

pipe(range(0,5))
	.next(lambda x: print(x))
	.run()

# Result:
# 0
# 1
# 2
# 3
# 4
```