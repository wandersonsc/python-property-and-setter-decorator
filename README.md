[![Build Status](https://travis-ci.org/wandersonsc/python-property-and-setter-decorator.svg?branch=main)](https://travis-ci.org/wandersonsc/python-property-and-setter-decorator)
[![codecov](https://codecov.io/gh/wandersonsc/python-property-and-setter-decorator/branch/main/graph/badge.svg?token=AJKLGKZJLK)](undefined)

# Managing Attribute Access

### Enhancing Class Attribute With Setters & Property Decorator

```python
   @property
    def meta_description(self):

        return self._meta_description
```

```python
    @meta_description.setter
    def meta_description(self, meta_description):

        self._meta_description = textwrap.shorten(
            meta_description, width=160)
```

### Setup

1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

```
pip3 install -r requirements.txt
```

### This project includes:

1. Class Methods
2. Pytest
3. Tracis CI
