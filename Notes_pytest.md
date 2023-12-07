pytest --version
pip list

pytest - It's a framework for testing (for write test cases) (like TestNG and Junit)

Note - pytest files should have the format "test_*.py or *_test.py
       and test methods/functions should start with Keyword "test".
----------------------------------------------------------------------
For running -
 single file test cases use   -  pytest "file_name"
 for running test cases in all files just use - pytest
 also u can use --  "pytest -v" / "pytest -v -s" 

----------------------------------------------------------------------
Grouping of Test cases -

use "@pytest.mark."marker_name"
to run this -  (pytest -m "marker_name")

Built-In markers -

@pytest.mark.filterwarnings(warning): add a warning filter to the given test. 

@pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") skips the test.

@pytest.mark.skipif(condition, ..., *, reason=...): skip the given test function if any of the conditions evaluate to True. Example: skipif(sys.platform == 'win32') skips the test if we are on the win32 platform. 

@pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict): mark the test function as an expected failure if any of the conditions evaluate to True. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure.

@pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.

@pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures.

@pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible. DEPRECATED, use @pytest.hookimpl(tryfirst=True) instead.

@pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible. DEPRECATED, use @pytest.hookimpl(trylast=True) instead

<hr></hr>

<h3>Fixtures</h3> - 
for running files - "pytest -s 'file_name'"

fixtures are a powerful feature that allows you to set up preconditions or resources needed for your tests. Fixtures are essentially functions marked with the @pytest.fixture decorator.

<h3>setup_and_teardown</h3>


<h3>yield</h3> -
yield statement is often used to provide a setup and teardown mechanism.
When a fixture includes a yield statement, the code before the yield is
executed as setup, and the code after the yield is executed as teardown.
This allows you to perform actions before and after a test using a single
fixture.


------------------------------------------------------------------------
<h3><!-- Conftest.py file -  --></h3>
conftest.py file is a special file that can be used to define fixtures, hooks, and other configurations that are shared across multiple test files or modules within a directory. When Pytest discovers a conftest.py file, it considers it as a configuration file for that directory and its subdirectories.
