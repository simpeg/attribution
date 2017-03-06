# attribution
Give credit to people

A software citation python package, that triggers when you use a function or class.

```python
import attribution

@attribution.cite('simpeg2015', 'haberbook')
def Mesh(blah):
    return blah * 2

print(attribution.list())   # nothing
Mesh(1)
print(attribution.list())   # bibtex
```

Should link into sphinx (gallery) documentation.
