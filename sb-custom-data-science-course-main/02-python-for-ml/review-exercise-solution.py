# Don't look at this until you've attempted a solution yourself.

# Part 1: Lists, Loops, and aggregating

student_ages = [13, 7, 22, 28, 42]
list_sum = 0
for age in student_ages:
    list_sum += age

avg_age = list_sum / len(student_ages)

for age in student_ages:
    if age < avg_age:
        print(f'{age} is less than the avg age of {avg_age}')

## Part 2: Nested Data
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

print(dictionary_challenge['hello']) # prints world
print(dictionary_challenge['target'][1]['too']) # prints far
print(dictionary_challenge['target'][0]['tricky'][2]) # prints Hello World!

# Part 2.2
dictionary_challenge['hello'] = 'friends'
dictionary_challenge['target'][1]['too'] = 'cool'
dictionary_challenge['target'][0]['tricky'][2] = 'So long and thanks for all the fish'

from pprint import pprint
pprint(dictionary_challenge)


## Part 3: Standalone Functions

### Mean

def mean(input_list):
    return sum(input_list) / len(input_list)

# Provided test, you should add more.
numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10

### Median

def median(input_list):
    n = len(input_list)
    sorted_list = sorted(input_list)

    # No elements, no median
    if n == 0:
        return None
    # Even case
    elif n % 2 == 0:
        a = sorted_list[n // 2]
        b = sorted_list[n // 2 - 1]
        return (a + b) / 2
    # Odd case
    else:
        return sorted_list[n // 2] # Note: Integer division is needed for odd n

# Provided test, you should add more.
numbers = [5, 10, 15]
m = median(numbers)
print(m) # 10

# ## Part 4: Classes

class Averages:
    def __init__(self, input_data):
        self.data = input_data.copy()

    def mean(self):
        return sum(self.data) / len(self.data) # replace with your code

    def median(self):
        n = len(self.data)
        sorted_list = sorted(self.data)

        # No elements, no median
        if n == 0:
            return None
        # Even case
        elif n % 2 == 0:
            a = sorted_list[n // 2]
            b = sorted_list[n // 2 - 1]
            return (a + b) / 2
        # Odd case
        else:
            return sorted_list[n // 2] # Note: Integer division is needed for odd n



# Sample tests, you should add more.
l_one = [5,10,15]
avgs = Averages(l_one)
print(avgs.mean()) # 10
print(avgs.median()) # 10

# Prove that we made a copy of the list, no side effects.
l_one.append(25)
print(avgs.mean()) # 10
print(avgs.median()) # 10
