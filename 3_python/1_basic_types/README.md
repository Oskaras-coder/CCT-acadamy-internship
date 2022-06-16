# Task: Fix the test.
- step 1. Open Terminal
- step 2. Go to project dir: `cd ~/Desktop/task1`
- step 3. Create virtual environment by running `$ python3 -m venv venv`
- step 4. Install `pytest` package by running `$ venv/bin/pip install pytest`
- step 5. Run the test using test collector `$ venv/bin/pytest task1.py` to see how a test fails.
The test collector callets all functions starting with `test_` and runs them.
- step 6. Fix the test and run `$ venv/bin/pytest task1.py` to see how the test succeeds.

```
def hello(to_great):
    return 'Hello ' + to_great + '!'

def test_hello_world():
    assert(hello('world') == 'Hello world')
```

# Task: Execute `hello` function using Interactive Python shell.
- step 1: Run Interactive Python shell `$ venv/bin/python3`
- step 2: Import `hello` function: `>>> from task1 import hello`
- step 3: Call `hello` function: `>>> hello('world')`
- step 4: See parameters of the `print` function: `>>> help(print)`
- step 5: Press `q` to exit the help window.
- step 6: See parameters of the string `upper` function: `>>> help('world'.upper)`
- step 7: Press `q` to exit the help window.
- step 8: Call `upper` method for a string: `>>> 'world'.upper()
- step 9: See a list of string methods: `>>> dir('world')
- setp 10: exit the Interactive Python shell: `>>> exit()`


# Task: Call `hello` function by executing your file.
- step 1: Uncomment these two lines to call `hello` function only when file is
executed and ignore it when the file is loaded (i.e. something is imported
from this file):

```
if __name__ == '__main__':
    print(hello('world'))
```

- step 2: Run the file `$ venv/bin/python task1.py`
- step 3: Run the test again `$ venv/bin/pytest -s task1.py`


# Task: Try out The Python Debugger.
- step 1: add a line `import pdb; pdb.set_trace()` in the `hello` function, just before `return` statement.
- step 2: Run the test again `$ venv/bin/pytest task1.py`
- step 3: The execution of the test will be interupted and you will be able to change variable values. Press `l` to see where the debugger is at.
- setp 4: Change the `to_great` value and press `b` to return one line back,
`n` to move one line forward and `c` to continue the execution. You will see
that the value was successfuly changed and the test fails.


# Task: setup environment
- step1: Setup Python virtual environment by running `$ make` command
- step2: See list of available make commands by running `$ make help`
- step3: Run tests by running `$ make test` command to see how tests succeed.

```
def get_sum(elements):
    return sum(elements)
```

# Task: using lists.
- step1: Create a test in test_task2.py file for a function, which returns
average value of a provided list
- step2: Run tests to see how they fail
- step3: Create a function which calculates the average of a provided list
- step4: Run tests to see how they succeed.
- step5: Create a function (and its test), which calculates average of even
list elements (with indexes 0, 2, 4, ..).
- step6: Create a function (and its test), which returns the average value of the
provided list, ignoring the 25% smallest and 25% highest list values.
- step7: Test your functions with the ranks list, to see whether they are corect
```
ranks = [22, 83, 60, 15, 29, 89, 93, 86, 33, 39, 77, 61, 83, 77, 65, 42, 14, 33, 20, 86,
         4, 13, 29, 40, 85, 92, 56, 94, 82, 98, 20, 41, 50, 4, 3, 48, 15, 29, 40, 90]
```
Returned values should be equal to: 51.0 (step3), 44.0 (step5) and 50.7 (step6).


# Task: Write docstrings for your functions.
- step1: write a docstrings for your functions.
- step2: insert debuger `import pdb; pdb.set_trace()` in one of your tests and run tests.
- step3: run `help(<your_function>)` to see the description of your function.
- step4: press `q` to exit and `c` to continue.


# Task: using dictionaries.
- step1: write a function (and its test), which gets a dictionary and returns
a sub-dictionary with two keys 'name' and 'karma', if a key is not present assign None.
- step2: test your function with these dictionaries:
```
p1 = {'name': 'Foo', 'karma': 123, 'value': -1}
p2 = {'karma': 123, 'value': -1}
p3 = {'name': 'Foo', 'value': -1}
```

# Links for further reading:
# - First 3 chapters of: https://docs.python.org/3.6/tutorial/index.html
# - Style Guide for Python Code: https://pep8.org/
