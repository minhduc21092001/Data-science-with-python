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