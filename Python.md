# Python
---
## Overview
![alt text](image-481.png)
![alt text](image-482.png)
![alt text](image-483.png)
![alt text](image-484.png)
![alt text](image-485.png)
![alt text](image-486.png)
![alt text](image-487.png)
![alt text](image-488.png)
![alt text](image-489.png)
![alt text](image-490.png)
![alt text](image-491.png)
![alt text](image-492.png)
![alt text](image-493.png)
## Data types and operators
![alt text](image-494.png)
![alt text](image-495.png)
![alt text](image-496.png)
![alt text](image-497.png)
![alt text](image-498.png)
![alt text](image-499.png)
Although the **last** two of these would **work** in Python, they are not pythonic ways to name variables.
![alt text](image-500.png)
![alt text](image-501.png)
![alt text](image-502.png)
![alt text](image-503.png)
![alt text](image-504.png)
![alt text](image-505.png)
![alt text](image-506.png)
![alt text](image-507.png)
![alt text](image-508.png)
![alt text](image-509.png)
![alt text](image-510.png)
![alt text](image-511.png)
![alt text](image-512.png)
![alt text](image-513.png)
![alt text](image-514.png)
![alt text](image-515.png)
![alt text](image-516.png)
![alt text](image-517.png)
![alt text](image-518.png)
![alt text](image-519.png)
![alt text](image-520.png)
![alt text](image-521.png)
![alt text](image-522.png)
![alt text](image-523.png)
```Python
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))
```
Here's another way you could write the print statements and get the same output. Recall that a string is an ordered datatype, and therefore, each item can be called by a location, and a location is each character.
```Python
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))
```
![alt text](image-524.png)
![alt text](image-525.png)
![alt text](image-526.png)
![alt text](image-527.png)
![alt text](image-528.png)
![alt text](image-529.png)
![alt text](image-530.png)
![alt text](image-531.png)

## Data structures in python
![alt text](image-569.png)
![alt text](image-570.png)
![alt text](image-571.png)
![alt text](image-572.png)
![alt text](image-573.png)
![alt text](image-574.png)
![alt text](image-575.png)
![alt text](image-576.png)
![alt text](image-577.png)
![alt text](image-578.png)
![alt text](image-579.png)
![alt text](image-580.png)
![alt text](image-581.png)
![alt text](image-582.png)
![alt text](image-583.png)
![alt text](image-584.png)
![alt text](image-585.png)
![alt text](image-586.png)
![alt text](image-587.png)
![alt text](image-588.png)
![alt text](image-589.png)
![alt text](image-590.png)
![alt text](image-591.png)
![alt text](image-592.png)
![alt text](image-593.png)
![alt text](image-594.png)
![alt text](image-595.png)
![alt text](image-596.png)
![alt text](image-597.png)
![alt text](image-598.png)
![alt text](image-599.png)
![alt text](image-600.png)
![alt text](image-601.png)
![alt text](image-602.png)
![alt text](image-603.png)
![alt text](image-604.png)
![alt text](image-605.png)
![alt text](image-606.png)
![alt text](image-607.png)
![alt text](image-608.png)
![alt text](image-609.png)
![alt text](image-610.png)
![alt text](image-611.png)
![alt text](image-612.png)
![alt text](image-613.png)
![alt text](image-614.png)
![alt text](image-615.png)
![alt text](image-616.png)
![alt text](image-617.png)
![alt text](image-618.png)
![alt text](image-619.png)
![alt text](image-620.png)
![alt text](image-621.png)
![alt text](image-622.png)
**Solution: Count Unique Words**
```Python
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

## split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

## convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

## print the number of unique words
num_unique = len(verse_set)
print(num_unique)
```
Output
```Python
if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise 

['if', 'you', 'can', 'keep', 'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 'talk', 'too', 'wise'] 

{'or', 'when', 'hating', 'make', 'all', 'head', 'waiting', 'losing', 'don’t', 'to', 'look', 'about', 'yourself', 'by', 'wise', 'doubting', 'trust', 'deal', 'allowance', 'being', 'too', 'wait', 'in', 'nor', 'for', 'theirs', 'and', 'if', 'on', 'lied', 'are', 'your', 'but', 'give', 'yet', 'lies', 'good', 'men', 'tired', 'doubt', 'hated', 'blaming', 'can', 'be', 'keep', 'their', 'not', 'it', 'talk', 'way', 'you'} 

51
```
**Solution: Verse Dictionary**
```Python
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

## find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

## find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

## create and sort a list of the dictionary's keys
items = list(verse_dict.items())
def sort_by_value(item):
    return item[1]
items.sort(key=sort_by_value)
sorted_keys = [item[0] for item in items]

## An alternative solution is to use a lambda function
sorted_keys = [k for k, v in sorted(verse_dict.items(), key=lambda item: item[1])]

## get the first element in the sorted list of keys
print(sorted_keys[0])

## find the element with the highest value in the list of keys
print(sorted_keys[-1]) 
```
Output
```Python
{'make': 1, 'waiting': 1, 'tired': 1, 'when': 2, 'hating': 1, 'give': 1, 'talk': 1, 'losing': 1, 'look': 1, 'too': 3, 'doubting': 1, 'all': 2, 'be': 1, 'wait': 1, 'you': 6, 'it': 1, 'allowance': 1, 'being': 2, 'by': 1, 'for': 1, 'to': 1, 'men': 1, 'in': 1, 'can': 3, 'about': 2, 'are': 1, 'hated': 1, 'wise': 1, 'your': 1, 'yourself': 1, "don't": 3, 'good': 1, 'way': 1, 'keep': 1, 'if': 3, 'blaming': 1, 'nor': 1, 'but': 1, 'or': 2, 'on': 1, 'not': 1, 'deal': 1, 'trust': 1, 'doubt': 1, 'yet': 1, 'lied': 1, 'lies': 1, 'their': 1, 'theirs': 1, 'and': 3, 'head': 1} 

51
False
keep
you
```
![alt text](image-623.png)
![alt text](image-624.png)
## Control flow
![alt text](image-625.png)
![alt text](image-626.png)
![alt text](image-627.png)
![alt text](image-628.png)
![alt text](image-629.png)
![alt text](image-630.png)
![alt text](image-631.png)
![alt text](image-632.png)
![alt text](image-633.png)
![alt text](image-634.png)
![alt text](image-635.png)
![alt text](image-636.png)
![alt text](image-637.png)
![alt text](image-638.png)
![alt text](image-639.png)
![alt text](image-640.png)
![alt text](image-641.png)
![alt text](image-642.png)
![alt text](image-643.png)
![alt text](image-644.png)
![alt text](image-645.png)
![alt text](image-646.png)
![alt text](image-647.png)
![alt text](image-648.png)
![alt text](image-649.png)
![alt text](image-650.png)
![alt text](image-651.png)
![alt text](image-652.png)
![alt text](image-653.png)
![alt text](image-654.png)
![alt text](image-655.png)
![alt text](image-656.png)
![alt text](image-657.png)
![alt text](image-658.png)
![alt text](image-659.png)
![alt text](image-660.png)
![alt text](image-661.png)
![alt text](image-662.png)
![alt text](image-663.png)
![alt text](image-664.png)
![alt text](image-665.png)
![alt text](image-666.png)
![alt text](image-667.png)
![alt text](image-668.png)
![alt text](image-669.png)
![alt text](image-670.png)
![alt text](image-671.png)
![alt text](image-672.png)
![alt text](image-673.png)
![alt text](image-674.png)
![alt text](image-675.png)
![alt text](image-676.png)
![alt text](image-677.png)
![alt text](image-678.png)
![alt text](image-679.png)
![alt text](image-680.png)
![alt text](image-681.png)
![alt text](image-682.png)
![alt text](image-683.png)
![alt text](image-684.png)
![alt text](image-685.png)
![alt text](image-686.png)
![alt text](image-687.png)
![alt text](image-688.png)
![alt text](image-689.png)
![alt text](image-690.png)
![alt text](image-691.png)
![alt text](image-692.png)
![alt text](image-693.png)
![alt text](image-694.png)
![alt text](image-695.png)
```Python
#ALTERNATIVE SECOND PART OF SOLUTION
highest_count = max(win_count_dict.values())

most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]
```

## Functions
![alt text](image-532.png)
![alt text](image-533.png)
![alt text](image-534.png)
![alt text](image-535.png)
![alt text](image-536.png)
![alt text](image-537.png)
![alt text](image-538.png)
![alt text](image-539.png)
![alt text](image-540.png)
![alt text](image-541.png)
![alt text](image-542.png)
![alt text](image-543.png)
![alt text](image-544.png)
![alt text](image-545.png)
```Python
def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
```
![alt text](image-546.png)
```Python
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))
```
![alt text](image-547.png)
![alt text](image-548.png)
![alt text](image-549.png)
![alt text](image-550.png)

```Python
def some_function():
    print(word)

some_function()```
Notice that we can still access the value of the global variable `word` within this function. However, the value of a global variable can not be __modified__ inside the function. If you want to modify that variable's value inside this function, it should be passed in as an argument. You'll see more on this in the next quiz.

Scope is essential to understanding how information is passed throughout programs in Python and really any programming language.
```
![alt text](image-551.png)
![alt text](image-552.png)
![alt text](image-553.png)
![alt text](image-554.png)
![alt text](image-555.png)
![alt text](image-556.png)
![alt text](image-557.png)
![alt text](image-558.png)
![alt text](image-559.png)
```Python
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
```
![alt text](image-560.png)
![alt text](image-561.png)
![alt text](image-562.png)
![alt text](image-563.png)
![alt text](image-564.png)
![alt text](image-565.png)
![alt text](image-566.png)
![alt text](image-567.png)
![alt text](image-568.png)

## Scripting
![alt text](image-696.png)
![alt text](image-697.png)
![alt text](image-698.png)
![alt text](image-699.png)
![alt text](image-700.png)
![alt text](image-701.png)
![alt text](image-702.png)
![alt text](image-703.png)
![alt text](image-704.png)
![alt text](image-705.png)
![alt text](image-706.png)
![alt text](image-707.png)
![alt text](image-708.png)
![alt text](image-709.png)
![alt text](image-710.png)