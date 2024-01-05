#!/bin/bash/env python3

bottles = 99

while bottles > 0:
    print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    action = input("Take one down and pass it around, or type 'q' to quit: ")

    if action.lower() == 'q':
        break

    bottles -= 1
    print(f"{bottles} bottles of beer on the wall.\n")

if bottles == 0:
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
else:
    print("Song interrupted. You can continue next time!")

