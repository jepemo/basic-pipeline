# basic-pipeline
Minimal &amp; Simple Pipeline for Python

## Getting Started
Just install it with the pip client:

```bash
pip install bpipe
```

Simple example
```python
from bpipe import pipe

pipe(range(0,5))
	.map(lambda x: print(x))
	.run()

# Result:
# 0
# 1
# 2
# 3
# 4
```

## Development

* Executing examples:
```python
cd examples
python first.py
# etc.
```

* Passing tests:
```python
python setup.py test
```
