# Review Fundamental Python:

This warmup exercise is meant to refresh your memory about:

* Creating and modifying data in lists and dictionaries.
* Using loops.
* Using if statements.
* Creating and calling functions.
* Creating classes, instantiating objects, and using those objects.

## Part 1: Lists, Loops, and aggregating

* Create a list with 5 numbers in it and assign it to a variable.
* Create a variable called `list_sum` and assign it the value `0`
* Using a for loop, the `list_sum` variable and the `+=` operator, compute the sum of the values in your list.
* Using the `len` function, `list_sum`, and the `/` operator, compute the average of the values in your list and store it into a variable.
* Using another loop and an if statement inside the loop print all the values in your list that are less than the average.

## Part 2: Nested Data

Often times data is provided in strange, and sometimes deeply nested formats. Lists inside of lists, lists inside of dictionaries, dictionaries inside of dictionaries... and so on. Examining and understanding this kind of data is a skill programmers have to use frequently... Lets practice. Copy this python code into a new script:

```python
dictionary_challenge = {
    'key': 'value',
    'hello': 'world',
    'target': [
        {
            'this_is': 'getting',
            'sort': 'of',
            'tricky': ['Hello Earth', 'Hello Detroit', 'Hello World!']
        },
        {
            'too': 'far'
        }
    ]
}
```

* Using bracket notation to select each of the follow values from the above data structure and then print them to check your work:
    * `'world'`
    * `'far'`
    * `'Hello World!'`

* Now, instead of simply printing the values, modify them!
    * Replace `'world'` with `'friends'`
    * Replace `'far'` with `'cool'`
    * Replace `'Hello World!'` with `'So long and thanks for all the fish'`
    * Then, print the entire data structure to check your work.

Pro-tip, use the following code to "pretty print" the dictionary instead of the standard print:

```
from pprint import pprint
pprint(dictionary_challenge)
```


## Part 3: Standalone Functions

Many functions are useful entirely on their own, and don't need to be part of a class. To practice creating and using standalone functions write the following two functions. Make sure to test each one by creating input and checking that it's output is what you expect.

> Hint: some of Python's built in functions may help you write this code faster. See: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

### Mean

Create a function called mean that accepts a list of numbers and returns the mean of those numbers. Remember, the mean is the sum of the values divided by the number of values. 

You should be able to use your function like this:

```python
numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10
```

**Be sure to test your code with more than just this single test case!**

> Hint: consider using the `sum` and `len` built in functions...

### Median

Create a function called median that accepts a list of numbers and returns the median of those numbers. Remember, the median is the value at the center of the sorted dataset. If there are an even number of values in the dataset the median is the mean of the two center values.

You should be able to use your function like this:

```python
numbers = [5, 10, 15]
m = median(numbers)
print(m) # 10
```

**Be sure to test your code with more than just this single test case!**

> Hint: Consider using the `sorted` built in function.
> Hint: You can determine if a list has an even number of items with `is_even = len(numbers) % 2 == 0`. See: [The modulo operator](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)

## Part 4: Classes

Now we're going to take the two functions you created and turn them into a class! Consider this incomplete class stub:

```python
class Averages:
    def __init__(self, input_data):
        pass # replace with your code

    def mean(self):
        pass # replace with your code

    def median(self):
        pass # replace with your code
```

Create a new python file and, using the code you wrote in part one, complete this class stub such that:

* When you create a new instance of the `Averages` class the input_data is copied and stored on `self.data`. Hint, there are [several ways to make a copy](https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list). 
* When a user calls the mean and median methods, the appropriate value is returned. You may reuse your code from part 1.

Example use, when your class is complete you should be able to use it as follows:

```python
avgs = Averages([5,10,15])
print(avgs.mean()) # 10
print(avgs.median()) # 10
```