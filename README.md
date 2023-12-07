<h1>pytest Notes</h1>
<h4>pytest - It's a framework for testing (for write test cases) (like TestNG and Junit)</h4>

<h3>pytest file format</h3>
<h4>Note - pytest files should have the format "test_*.py or *_test.py
       and test methods/functions should start with Keyword "test".</h4>

<h3>Termiinal commands</h3>
<li>pytest --version</li>
<li>pip list</li>
<li>pytest "file_name"</li>
<li>pytest</li><span> Run all test at once</span>
<li>pytest -v -s</li>
<li>pytest -v -s "file_name</li>

<h3>Grouping of Test cases -</h3>

<h4>Built -in markers</h4>
<p>
<h5>@pytest.mark.filterwarnings(warning)</h5>: add a warning filter to the given test. 

<h5>@pytest.mark.skip(reason=None)</h5>: skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") skips the test.

<h5>@pytest.mark.skipif(condition, ..., *, reason=...)</h5>h5>: skip the given test function if any of the conditions evaluate to True. Example: skipif(sys.platform == 'win32') skips the test if we are on the win32 platform. 

<h5>@pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict)</h5>: mark the test function as an expected failure if any of the conditions evaluate to True. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure.

<h5>@pytest.mark.parametrize(argnames, argvalues)</h5>: call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.

<h5>@pytest.mark.usefixtures(fixturename1, fixturename2, ...)</h5>: mark tests as needing all of the specified fixtures.

<h5>@pytest.mark.tryfirst</h5>: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible. DEPRECATED, use @pytest.hookimpl(tryfirst=True) instead.

<h5>@pytest.mark.trylast</h5>: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible. DEPRECATED, use <h5>@pytest.hookimpl(trylast=True)</h5> instead
</p>

<h3>
       For marking test - <h4>"@pytest.mark."marker_name"</h4>
       For running test - <h4>"@pytest -m "marker_name"</h4>
</h3>
