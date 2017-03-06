from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import functools

_registry = set()


def cite(key):
    def citation_wrapper(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            _registry.add(key)
            return f(*args, **kwargs)
        return wrapper
    return citation_wrapper


def list():
    return _registry

if __name__ == '__main__':
    @cite('simpeg2015')
    def Mesh(blah):
        return blah * 2

    print(list())   # nothing
    Mesh(1)
    print(list())   # bibtex
