#!/bin/bash/env python3

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    total = 0
    num_rolls = 0

    while True:
        input("Press Enter to roll the dice...")

        result = roll_dice()
        print(f"You rolled a {result}!")
        
        total += result
        num_rolls += 1

        average = total / num_rolls
        print(f'Averages after {num_rolls} rolls: {average:.2f}')

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
