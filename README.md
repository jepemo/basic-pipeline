# basic-pipeline
basic-pipeline (or *bpipe*) is a minimal &amp; simple pipeline engine for Python

[![Build Status](https://travis-ci.org/jepemo/basic-pipeline.svg?branch=master)](https://travis-ci.org/jepemo/basic-pipeline)

- [Getting Started](#getting-started)
  - [Examples](#examples)
  - [Installation](#installation)
  - [Tests](#tests)
- [Tutorial](#tutorial)
- [Reference](#reference)

## Getting Started

## Examples
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

### Tests
```python
python setup.py test
```

## [Tutorial](docs/tutorial.md)
## [Reference](docs/reference.md)
