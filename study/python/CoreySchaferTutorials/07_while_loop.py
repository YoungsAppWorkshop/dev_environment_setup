#!/usr/bin/env python3

# While Loop
x = 0
while x < 10:
    print(x)
    x += 1


# While Loop with break statement
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Infinite while loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
