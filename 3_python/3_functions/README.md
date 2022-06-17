# Task: help ATM to split given amount into banknotes/coins.
1. write a function, which splits a given amount into banknotes/coins.
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

4. Write unit tests for your function.

5. Write a docstring for your function.

6. Make sure your code works with `amount = 11, banknotes = [5,2]`, solution is `5, 2, 2, 2`.

7. Implement split amount in both recursive and iterative approaches.
