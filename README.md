# basic-pipeline
basic-pipeline (or *bpipe*) is a minimal &amp; simple pipeline engine for Python

- [Getting Started](#getting-started)
  - [Example](#example)
  - [Installation](#installation)
  - [Examples](#examples)
  - [Tests](#tests)
- [Reference](#reference)
  

## Getting Started

### Example
```python
from bpipe import *

for r in echo("Hello World") | map_to(lambda x: x.upper()):
    print(r)

# HELLO WORLD
```

### Installation

Just install it with the pip client:

```bash
pip install bpipe
```

Or from source code:

```python
git clone https://github.com/jepemo/basic-pipeline
cd basic-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### Examples
```python
python examples/helloworld.py
python examples/wordcount.py
# etc.
```

### Tests
```python
python setup.py test
```

## Reference

### Sources
#### echo
#### cat
#### get
### Tranformations
#### map_to
#### flatmap
#### flatten
