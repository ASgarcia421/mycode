#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt

def main():
    """run time code"""

    # create lists to store the scores
    player1_dice = []
    player2_dice = []

    for i in range(3):
        player1_dice.append(random.randint(1, 6))  # 1 to 6 inclusive
        player2_dice.append(random.randint(1, 6))  # 1 to 6 inclusive

    print("Player 1 rolled", player1_dice)
    print("Player 2 rolled", player2_dice)

    # Plot the scores
    plot_scores(player1_dice, player2_dice)

    # determine which player won
    if sum(player1_dice) == sum(player2_dice):
        print("Draw")
    elif sum(player1_dice) > sum(player2_dice):
        print("Player 1 wins")
    else:
        print("Player 2 wins")

def plot_scores(player1_scores, player2_scores):
    """Plot line chart for scores"""
    rounds = list(range(1, len(player1_scores) + 1))

    plt.plot(rounds, player1_scores, label='Player 1')
    plt.plot(rounds, player2_scores, label='Player 2')

    plt.xlabel('Round')
    plt.ylabel('Score')
    plt.title('Scores Over Rounds')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

