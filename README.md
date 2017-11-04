# basic-pipeline
Minimal &amp; Simple Pipeline for Python


```python
from bpipe import Pipe

Pipe(range(0,10))
	.next(lambda x: print(x))
	.start()
```