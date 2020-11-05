[![Build Status](https://travis-ci.org/wandersonsc/python-property-and-setter-decorator.svg?branch=main)](https://travis-ci.org/wandersonsc/python-property-and-setter-decorator)
[![codecov](https://codecov.io/gh/wandersonsc/python-property-and-setter-decorator/branch/main/graph/badge.svg?token=AJKLGKZJLK)](undefined)

# Managing Attribute Access

### Enhancing Class Attribute With Setters & Property Decorator

So, according to Google, Meta Descriptions should be arround 160 characters, therefore, it's best to keep meta descriptions long enough that they're sufficiently descriptive, with that in mind, our primary goal should be to make sure that our Meta Description follows Google's guidelines.

> Meta descriptions can be any length, but Google generally truncates snippets to ~155–160 characters.

**Setters & Property Decorator** really comes in handy when we need to do something special with some attribute. However, there are a couple of caveats when using `@property`, for instance you are locked to this specific class.

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

**Note** that we are using `_meta_description` rather than `meta_description` to avoid name clashing.

### Setup

1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

```
pip3 install -r requirements.txt
```

### This project includes:

1. Setters & Property Decorator
2. Pytest
3. Tracis CI
