attribution
===========


.. image:: https://img.shields.io/pypi/v/attribution.svg
        :target: https://pypi.python.org/pypi/attribution

.. image:: https://img.shields.io/travis/simpeg/attribution.svg
        :target: https://travis-ci.org/simpeg/attribution

.. image:: https://readthedocs.org/projects/attribution/badge/?version=latest
        :target: https://attribution.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/simpeg/attribution/shield.svg
     :target: https://pyup.io/repos/github/simpeg/attribution/
     :alt: Updates


Give credit to people.

A software citation python package, that triggers when you use a function or class.

.. code:: python

    import attribution

    @attribution.cite('simpeg2015', 'haberbook')
    def Mesh(blah):
        return blah * 2

    print(attribution.list())   # nothing
    Mesh(1)
    print(attribution.list())   # bibtex


* Documentation: https://attribution.readthedocs.io.


Features
--------
