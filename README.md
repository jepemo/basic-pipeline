# basic-pipeline
basic-pipeline (or *bpipe*) is a minimal &amp; simple pipeline engine for Python

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Tests](#tests)
- [Reference](#reference)
  - [Sources](#sources)
  - [Transformations](#transformations)

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

## Reference

### Sources
#### echo
```
echo("input string") | <transformations>
```
Initializes the pipe with an input string.

#### cat
```
cat(filepath) | <transformations>
```
Initializes the pipe with the content of a file

#### curl
```
curl(url) | <transformations> 
```
Initializes the pipe with the contents of a url.

### Tranformations
#### map_to
```
<source> | <transformations> | map_to(function) | ...
```
Aplies some tranformation.
#### flatten
```
<source> | <transformations> | flatten() | ...
```
Unbox the element of the stream if it is boxed.

#### flat_map
```
<source> | <transformations> | flat_map(function) | ...
```
First unbox the element and then applies the function.
