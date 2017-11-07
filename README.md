# basic-pipeline
basic-pipeline (or *bpipe*) is a minimal &amp; Simple Pipeline Engine for Python

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
	.go()

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
