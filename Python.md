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
![alt text](image-1092.png)
![alt text](image-1093.png)
![alt text](image-1094.png)
![alt text](image-1095.png)
![alt text](image-1096.png)
```Python
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
```
![alt text](image-1097.png)
![alt text](image-1098.png)
![alt text](image-1099.png)
![alt text](image-1100.png)
![alt text](image-1101.png)
![alt text](image-1102.png)
![alt text](image-1103.png)
![alt text](image-1104.png)
![alt text](image-1105.png)
![alt text](image-1106.png)
![alt text](image-1107.png)
![alt text](image-1108.png)
![alt text](image-1109.png)
![alt text](image-1110.png)
![alt text](image-1111.png)
![alt text](image-1112.png)
![alt text](image-1113.png)
![alt text](image-1114.png)
![alt text](image-1115.png)
![alt text](image-1116.png)
![alt text](image-1117.png)
![alt text](image-1118.png)
![alt text](image-1119.png)
Here is my solution:
```Python
user_list = []
list_sum = 0
for i in range(10):
    userInput = int(input("Enter any number: "))
    try:
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError:
        print("Incorrect value. That's not an int!")
print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))
```
![alt text](image-1120.png)
![alt text](image-1121.png)
![alt text](image-1122.png)
![alt text](image-1123.png)
![alt text](image-1124.png)
![alt text](image-1125.png)
![alt text](image-1126.png)
![alt text](image-1127.png)
```Python
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
```
![alt text](image-1128.png)
![alt text](image-1129.png)
![alt text](image-1130.png)
![alt text](image-1131.png)
![alt text](image-1132.png)
![alt text](image-1133.png)
![alt text](image-1134.png)
![alt text](image-1135.png)
![alt text](image-1136.png)
![alt text](image-1137.png)
![alt text](image-1138.png)
![alt text](image-1139.png)
![alt text](image-1140.png)
![alt text](image-1141.png)
![alt text](image-1142.png)
![alt text](image-1143.png)
Quiz Solution:
Here's one way you can implement this program!
```Python
## function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

## Main function that prompts for user input, parses out the first letter
## includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
## print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()
```
## Numpy
![alt text](image-1144.png)
![alt text](image-1145.png)
![alt text](image-1146.png)
![alt text](image-1147.png)
![alt text](image-1148.png)
![alt text](image-1149.png)
![alt text](image-1150.png)
![alt text](image-1151.png)
![alt text](image-1152.png)
![alt text](image-1153.png)
![alt text](image-1154.png)
![alt text](image-1155.png)
![alt text](image-1156.png)
![alt text](image-1157.png)
![alt text](image-1158.png)
![alt text](image-1159.png)
![alt text](image-1160.png)
![alt text](image-1161.png)
![alt text](image-1162.png)
![alt text](image-1163.png)
![alt text](image-1164.png)
![alt text](image-1165.png)
![alt text](image-1166.png)
![alt text](image-1167.png)
![alt text](image-1168.png)
![alt text](image-1169.png)
![alt text](image-1170.png)
![alt text](image-1171.png)
![alt text](image-1172.png)
![alt text](image-1173.png)
![alt text](image-1174.png)
![alt text](image-1175.png)
![alt text](image-1176.png)
![alt text](image-1177.png)
![alt text](image-1178.png)
```Python
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
```
![alt text](image-1179.png)
![alt text](image-1180.png)
![alt text](image-1181.png)
![alt text](image-1182.png)
![alt text](image-1183.png)
![alt text](image-1184.png)
![alt text](image-1185.png)
![alt text](image-1186.png)
![alt text](image-1187.png)
![alt text](image-1188.png)
![alt text](image-1189.png)
![alt text](image-1190.png)
![alt text](image-1191.png)
![alt text](image-1192.png)
![alt text](image-1193.png)
![alt text](image-1194.png)
![alt text](image-1195.png)
![alt text](image-1196.png)
![alt text](image-1197.png)
![alt text](image-1198.png)
![alt text](image-1199.png)
![alt text](image-1200.png)
![alt text](image-1201.png)
![alt text](image-1202.png)
![alt text](image-1203.png)
```Python
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We print x with the first and last element deleted
print()
print('Modified x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We delete the first row of y
w = np.delete(Y, 0, axis=0)

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)
```
![alt text](image-1204.png)
![alt text](image-1205.png)
```Python
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray 
Y = np.array([[1,2,3],[4,5,6]])

# We print x
print()
print('Original x = ', x)

# We append the integer 6 to x
x = np.append(x, 6)

# We print x
print()
print('x = ', x)

# We append the integer 7 and 8 to x
x = np.append(x, [7,8])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)

# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)

# We print v
print()
print('v = \n', v)

# We print q
print()
print('q = \n', q)
```
![alt text](image-1206.png)
![alt text](image-1208.png)
```Python
# We create a rank 1 ndarray 
x = np.array([1, 2, 5, 6, 7])

# We create a rank 2 ndarray 
Y = np.array([[1,2,3],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We insert the integer 3 and 4 between 2 and 5 in x. 
x = np.insert(x,2,[3,4])

# We print x with the inserted elements
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We insert a row between the first and last row of y
w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,5, axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)
```
![alt text](image-1209.png)
![alt text](image-1210.png)
```Python
# We create a rank 1 ndarray 
x = np.array([1,2])

# We create a rank 2 ndarray 
Y = np.array([[3,4],[5,6]])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Y = \n', Y)

# We stack x on top of Y
z = np.vstack((x,Y))

# We stack x on the right of Y. We need to reshape x in order to stack it on the right of Y. 
w = np.hstack((Y,x.reshape(2,1)))

# We print z
print()
print('z = \n', z)

# We print w
print()
print('w = \n', w)
```
![alt text](image-1211.png)
![alt text](image-1213.png)
```Python
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
# (The 1st being index 0)
Z = X[1:4,2:5]

# We print Z
print('Z = \n', Z)

# We can select the same elements as above using method 2
W = X[1:,2:5]

# We print W
print()
print('W = \n', W)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
Y = X[:3,2:5]

# We print Y
print()
print('Y = \n', Y)

# We select all the elements in the 3rd row
v = X[2,:]

# We print v
print()
print('v = ', v)

# We select all the elements in the 3rd column
q = X[:,2]

# We print q
print()
print('q = ', q)

# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]

# We print R
print()
print('R = \n', R)
```
![alt text](image-1214.png)
![alt text](image-1215.png)
![alt text](image-1216.png)
```Python
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 4th columns
Z = X[1:4,2:5]

# We print Z
print()
print('Z = \n', Z)
print()

# We change the last element in Z to 555
Z[2,2] = 555

# We print X
print()
print('X = \n', X)
print()
```
![alt text](image-1217.png)
![alt text](image-1218.png)
```Python
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# create a copy of the slice using the np.copy() function
Z = np.copy(X[1:4,2:5])

#  create a copy of the slice using the copy as a method
W = X[1:4,2:5].copy()

# We change the last element in Z to 555
Z[2,2] = 555

# We change the last element in W to 444
W[2,2] = 444

# We print X
print()
print('X = \n', X)

# We print Z
print()
print('Z = \n', Z)

# We print W
print()
print('W = \n', W)
```
![alt text](image-1219.png)
![alt text](image-1220.png)
```Python
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1,3])

# We print X
print()
print('X = \n', X)
print()

# We print indices
print('indices = ', indices)
print()

# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices,:]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]

# We print Y
print()
print('Y = \n', Y)

# We print Z
print()
print('Z = \n', Z)
```
![alt text](image-1221.png)
![alt text](image-1222.png)
```Python
# Create a rank 1 ndarray that contains a randomly chosen 10 values between `0` to `len(X)` (50)
# The row_indices would represent the indices of rows of X
row_indices = np.random.randint(0,50, size=10)
print("Random 10 indices are: ", row_indices)
```
![alt text](image-1223.png)
```Python
# To Do 1 - Print those rows of X whose indices are represented by entire row_indices ndarray
# Hint - Use the row_indices ndarray to select specified rows of X
X_subset = X[row_indices, :]
print(X_subset)

# To Do 2 - Print those rows of X whose indices are present in row_indices[4:8]
X_subset = X[row_indices[4:8], :]
print(X_subset)
```
![alt text](image-1224.png)
![alt text](image-1225.png)
![alt text](image-1226.png)
![alt text](image-1227.png)
```Python
numpy.unique(array, return_index=False, return_inverse=False, return_counts=False, axis=None)
```
![alt text](image-1228.png)
![alt text](image-1229.png)
```Python
# We create a 5 x 5 ndarray that contains integers from 0 to 24
X = np.arange(25).reshape(5, 5)

# We print X
print()
print('Original X = \n', X)
print()

# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# We use Boolean indexing to assign the elements that are between 10 and 17 the value of -1
X[(X > 10) & (X < 17)] = -1

# We print X
print()
print('X = \n', X)
print()
```
![alt text](image-1230.png)
```Python
# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))
```
![alt text](image-1231.png)
![alt text](image-1232.png)
```Python
# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a function.
print()
print('Sorted x (out of place):', np.sort(x))

# When we sort out of place the original array remains intact. To see this we print x again
print()
print('x after sorting:', x)
```
![alt text](image-1233.png)
```Python
# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a method.
x.sort()

# When we sort in place the original array is changed to the sorted array. To see this we print x again
print()
print('x after sorting:', x)
```
![alt text](image-1234.png)
![alt text](image-1235.png)
![alt text](image-1236.png)
![alt text](image-1237.png)
![alt text](image-1238.png)
![alt text](image-1239.png)
![alt text](image-1240.png)
![alt text](image-1241.png)
![alt text](image-1242.png)
![alt text](image-1243.png)
![alt text](image-1244.png)
![alt text](image-1245.png)
![alt text](image-1246.png)
```Python
# We create a 2 x 2 ndarray
X = np.array([[1,2], [3,4]])

# We print x
print()
print('X = \n', X)
print()

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))
print()
print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X,axis=0))
print('Median of all elements in the rows of X:', np.median(X,axis=1))
print()
print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))
print()
print('Minimum value of all elements in X:', X.min())
print('Minimum value of all elements in the columns of X:', X.min(axis=0))
print('Minimum value of all elements in the rows of X:', X.min(axis=1))
```
![alt text](image-1247.png)
![alt text](image-1248.png)
![alt text](image-1249.png)
![alt text](image-1250.png)
![alt text](image-1251.png)
![alt text](image-1252.png)
![alt text](image-1253.png)
![alt text](image-1254.png)
![alt text](image-1255.png)
![alt text](image-1256.png)
![alt text](image-1257.png)
![alt text](image-1258.png)
![alt text](image-1259.png)
![alt text](image-1260.png)
![alt text](image-1261.png)
![alt text](image-1262.png)
![alt text](image-1263.png)

## Pandas
![alt text](image-1264.png)
![alt text](image-1265.png)
![alt text](image-1266.png)
![alt text](image-1267.png)
Example 1 - Create a Series
```Python
# We import Pandas as pd into Python
import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We display the Groceries Pandas Series
groceries
```
![alt text](image-1268.png)
![alt text](image-1269.png)
![alt text](image-1270.png)
![alt text](image-1271.png)
```Python
# We access elements in Groceries using index labels:

# We use a single index label
print('How many eggs do we need to buy:', groceries['eggs'])
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']]) 
print()

# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']]) 
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]]) 
print()

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0]) 
print()
# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]]) 
```
![alt text](image-1272.png)
![alt text](image-1273.png)
![alt text](image-1274.png)
```Python
# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples out of place:\n', groceries)
```
```Python
![alt text](image-1275.png)
# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace = True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples in place:\n', groceries)
```
![alt text](image-1276.png)
![alt text](image-1277.png)
```Python
# We create a Pandas Series that stores a grocery list of just fruits
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

# We display the fruits Pandas Series
fruits
```
![alt text](image-1278.png)
```Python
# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits  *2:\n', fruits*  2) # We multiply each item in fruits by 2 
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()
```
![alt text](image-1279.png)
![alt text](image-1280.png)
```Python
# We import NumPy as np to be able to use the mathematical functions
import numpy as np

# We print fruits for reference
print('Original grocery list of fruits:\n', fruits)

# We apply different mathematical functions to all elements of fruits
print()
print('EXP(X) = \n', np.exp(fruits))
print() 
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of fruits to the power of 2
```
![alt text](image-1281.png)
![alt text](image-1282.png)
```Python
# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)
```
![alt text](image-1283.png)
![alt text](image-1284.png)
![alt text](image-1285.png)
![alt text](image-1286.png)
```Python
# We import Pandas as pd into Python
import pandas as pd

# We create a dictionary of Pandas Series 
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

# We print the type of items to see that it is a dictionary
print(type(items))
```
![alt text](image-1287.png)
```Python
# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
shopping_carts
```
![alt text](image-1288.png)
![alt text](image-1289.png)
![alt text](image-1290.png)
Example 3. Demonstrate a few attributes of DataFrame
```Python
# We print some information about shopping_carts
print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)
```
![alt text](image-1291.png)
![alt text](image-1292.png)
```Python
# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# We display sel_shopping_cart
sel_shopping_cart
```
![alt text](image-1293.png)
Example 5. Selecting specific columns of a DataFrame
```Python
# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# We display alice_sel_shopping_cart
alice_sel_shopping_cart
```
![alt text](image-1294.png)
![alt text](image-1295.png)
![alt text](image-1296.png)
![alt text](image-1297.png)
![alt text](image-1298.png)
![alt text](image-1299.png)
```Python
# We print the store_items DataFrame
print(store_items)

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
```
![alt text](image-1300.png)
![alt text](image-1301.png)
```Python
# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
store_items['shirts'] = [15,2]

# We display the modified DataFrame
store_items
```
![alt text](image-1302.png)
```Python
# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['pants'] + store_items['shirts']

# We display the modified DataFrame
store_items
```
![alt text](image-1303.png)
```Python
# We create a dictionary from a list of Python dictionaries that will contain the number of different items at the new store
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3'])

# We display the items at the new store
new_store
```
![alt text](image-1304.png)
Example 5. Add new column that has data from the existing columns
```Python
# We add a new column using data from particular rows in the watches column
store_items['new watches'] = store_items['watches'][1:]

# We display the modified DataFrame
store_items
```
![alt text](image-1305.png)
Example 6. Add new column at a specific location
```Python
# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

# we display the modified DataFrame
store_items
```
![alt text](image-1306.png)
![alt text](image-1307.png)
![alt text](image-1308.png)
![alt text](image-1309.png)
![alt text](image-1310.png)
![alt text](image-1311.png)
```Python
# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items
```
![alt text](image-1312.png)
![alt text](image-1313.png)
![alt text](image-1314.png)
![alt text](image-1315.png)
```Python
# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())
```
![alt text](image-1316.png)
![alt text](image-1317.png)
![alt text](image-1318.png)
![alt text](image-1319.png)
![alt text](image-1320.png)
![alt text](image-1321.png)
![alt text](image-1322.png)
![alt text](image-1323.png)
```Python
# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)
```
![alt text](image-1324.png)
```Python
# We replace NaN values by using linear interpolation using row values
store_items.interpolate(method = 'linear', axis = 1)
```
![alt text](image-1325.png)
![alt text](image-1326.png)
![alt text](image-1327.png)
![alt text](image-1328.png)
![alt text](image-1329.png)
![alt text](image-1330.png)
![alt text](image-1331.png)
![alt text](image-1332.png)
![alt text](image-1333.png)
![alt text](image-1334.png)
![alt text](image-1335.png)
![alt text](image-1336.png)
![alt text](image-1337.png)
![alt text](image-1338.png)
![alt text](image-1339.png)
![alt text](image-1340.png)
```Python
# We display the total salary each employee received in all the years they worked for the company
data.groupby(['Name'])['Salary'].sum()
```
![alt text](image-1341.png)
![alt text](image-1342.png)
![alt text](image-1343.png)
![alt text](image-1344.png)
![alt text](image-1345.png)
![alt text](image-1346.png)
![alt text](image-1347.png)
![alt text](image-1348.png)
![alt text](image-1349.png)
![alt text](image-1350.png)
Quiz Solution: Implement my_enumerate
```Python
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
```
![alt text](image-1351.png)
![alt text](image-1352.png)
![alt text](image-1353.png)
```Python
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
```
This can help you save time and create efficient code!
