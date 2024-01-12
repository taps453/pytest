# pytest Notes

## pytest  
- It's a framework for testing (for write test cases) [like TestNG and Junit]

## pytest file format
- pytest files should have the format "test_*.py / *_test.py
- Test methods/functions should start with Keyword "test".

## Termiinal commands

```python

pytest --version
```

```python

pip list
```

```python

pytest "file_name"
```

```python

pytest
```

### Run all test at once

```python

pytest -v -s
```

```python

pytest -v -s "file_name"
```

## Grouping of Test cases

### Built -in markers

```python

@pytest.mark.filterwarnings(warning)

- Add a warning filter to the given test. 
```

```python

@pytest.mark.skip(reason=None)

- Skip the given test function with an optional reason.
- Example: skip(reason="no way of currently testing this") skips the test.
```

```python

@pytest.mark.skipif(condition, ..., *, reason=...)

- Skip the given test function if any of the conditions evaluate to True.
- Example: skipif(sys.platform == 'win32') skips the test if we are on the win32 platform. 
```

```python

@pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict)

- Mark the test function as an expected failure if any of the conditions evaluate to True. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure.
```

```python

@pytest.mark.parametrize(argnames, argvalues)

- Call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names.
- Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.
```

```python

@pytest.mark.usefixtures(fixturename1, fixturename2, ...)

- Mark tests as needing all of the specified fixtures.
```


```python

@pytest.mark.tryfirst

-Mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.
- use @pytest.hookimpl(tryfirst=True) instead.
```

```python

@pytest.mark.trylast

- Mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.
- use @pytest.hookimpl(trylast=True) instead
```


## For marking test 

```python

"@pytest.mark."marker_name"
```

## For running Marker test

```python

"@pytest -m "marker_name"
```
