# basic-pipeline
basic-pipeline (or *bpipe*) is a minimal &amp; simple pipeline engine for Python

## Getting Started
Just install it with the pip client:

```bash
pip install bpipe
```

Simple example
```python
from bpipe import *

for r in echo("Hello World") | map_to(lambda x: x.upper()):
    print(r)

# HELLO WORLD
```

## Development

* Executing examples:
```python
python3 -m venv venv
source venv/bin/activate
pip install -e .
python examples/first.py
# etc.
```

* Passing tests:
```python
python setup.py test
```
