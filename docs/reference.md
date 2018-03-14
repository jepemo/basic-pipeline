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
