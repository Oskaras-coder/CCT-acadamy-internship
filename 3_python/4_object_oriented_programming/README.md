# 1. Task: Real estate company
===============================
Real estate company sells flats for its customers.
1. Create an empty `Customer` class.
2. Add a constructor to a `Customer` class, which would accept:
    a. customer's email
    b. optionally customer's name
    c. tax percent for services with default value of 2
3. Add a method `total_amount()` to `Customer` class. This method has to accept a price of a flat and return total amount including tax for service.
4. Create three `Customer` instances (also called as objects) with chosen data.
5. Call `total_amount()` method for one of the instances with flat price of `100000` to test if it works correctly.
6. Create a `LoyalCustomer` class, which inherits from `Customer` class. `LoyalCustomer` should have default tax percent for service equal to 1.
7. Create two `LoyalCustomer` instances.
8. Call `total_amount()` method for one of the `LoyalCustomer` instances with flat price of `100000` to test if it works correctly.
9. Create class `Flat` with a constructor, which gets the price of a flat and its address.
10. Create class `RealEstateCompany`, which receives a list of flats and a list of its clients.
11. Add `cheapest()` method to a `RealEstateCompany` class. This method should find and return a flat with the smallest price.
12. Add `sell()` method to a `RealEstateCompany` class. This method should accept a flat and a client. This method should print a 
message with a flat address, customer email address (and name if its present) and total amount that the customer has paid.
Also a flat should be removed from the list of flats for sold after it is sold to a customer.
11. Create `RealEstateCompany` instance with 3 customers (one of which is loyal) and 3 available flats with different prices.
12. Sell the cheapest flat to a simple customer.
13. Sell the cheapest flat from the remaining ones to a loyal customer.


# 2. Task: Train operations
The train consists of locomotives and wagons. Create classes for locomotive, wagon and train (composition of locomotive and wagons).
Each wagon has a specific mass, the mass of the load carried, the maximum mass of the load and a unique wagon number. The locomotive has its own mass and maximum towable mass.

Write classes for work with train, locomotive and wagons. Write a program to demonstrate the operation of classes.

## Requirements
- Objects and methods are documented (docstring)
- Possibility to save train data to a file in json format (selected file structure of your choice)
- Ability to upload data from a file in json format. You must correctly scan the file you created while saving the data
- The file can be opened for writing and reading
- Meaningful __add__, __sub__, __repr__, __str __ / __ unicode__, __len__, __bool__ methods must be described for the train and, if necessary, for wagons and locomotives
- Once you have created several trains, they can be sorted (you can choose according to what).
- In case of errors - objects described by the programmer inherited from the exception class must be created and raised. Also - caught in the main program
- Error handling must be implemented
- Use at least one of each instance, class, and static methods
- The program must meet the PEP8 standard.
- At least one property must be described for working with attributes (value validation, value recalculation, or other)
- The program code must be neat and systematic.
- After the program - let’s print out all locomotives with sorted locomotives by their wagons' specific mass sum
- There must be instructions
- Let’s add unit tests!

## Goals
1. Revise Python basics
2. Understand basic data types, immutable vs mutable data types
3. Get a deeper understanding of OOP: what is OOP, what is the difference between OOP and functional programming, what are classes in Python, how you can work with classes, what are class/instance/static methods, what are magic methods, etc.
4. Get confident when working with lists and dictionaries
5. Get initial understanding of PEP8

## Additional karma points for
1. Getting familiar with Lambda functions
2. Play around with Sets, use functions as union, intersection
3. What are generators? How they are created?
4. What are decorators? How they are created?

# Material
- https://docs.python.org/3/tutorial/classes.html
- https://www.w3schools.com/python/python_classes.asp
- https://rszalski.github.io/magicmethods/

