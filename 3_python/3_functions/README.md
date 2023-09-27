# Task: help ATM to split given amount into banknotes/coins.
1. write a function, which splits a given amount into the least amount of banknotes/coins.
  The function should receive two parameters:
    `amount` - a number which an ATM user wants to cashout (this value has to be split into banknotes).
    `banknotes` - a list of available banknotes/coins, lets use [1, 2, 5] as a default value for this list.
  The function should return:
    a list, consisting of biggest banknotes/coins, which can be used to split the amount.
    False - if its not possible to split the amount into banknotes.
  For example,
    if amount is 13, available banknotes - [1, 2, 5], the returned value should be [5, 5, 2, 1].

2. update the function (and add new test) to work with any list of banknotes.
  For example,
    if amount is 13, available banknotes - [1, 10], the returned value should be [10, 1, 1, 1].
    if amount is 13, available banknotes - [2, 5], the returned value should be False.

3. update the function (and add new test) to work with cents, i.e. banknotes/coins can be floating point numbers.
  For example,
    if amount is 11.5, available banknotes - [0.5, 1, 10], the returned value should be [10, 1, 0.5].

4. Write unit tests for your function. Most primitive way to do it:

```
def test_split_amount():
    assert(split_amount(11, [5, 2, 1]) == [5, 5, 1])

test_split_amount()
```

5. Write a docstring for your function.

6. Make sure your code works with `amount = 11, banknotes = [5,2]`, solution is `5, 2, 2, 2`.

7. Implement split amount in both recursive and iterative approaches.

8. We have made an assumption that the ATM had an unlimited amount of banknotes.
Update both iterative and recursive versions of split amount function to accept how many banknotes of each type are there in the ATM.
For example, if we try to cash out `amount = 100` and the ATM has `banknotes = {10: 100, 20: 1, 50: 1}`, the result should be `[50, 20, 10, 10, 10]`.
