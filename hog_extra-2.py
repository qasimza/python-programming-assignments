_author_ = "Zaina Qasim, Isaac Kirsch"
_credits_ = [""]
_email_ = "qasimza@mail.uc.edu, kirschic@mail.uc.edu"

#######################
# Phase 2: Strategies #
#######################

from hog import *
from random import *


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """

    # BEGIN Question 6
    def average_value(*args):
        return sum([fn(*args) for i in range(num_samples)]) / num_samples

    return average_value
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    avg_list = [make_averaged(roll_dice)(i + 1, dice) for i in range(10)]
    max_dice = max(avg_list)
    return avg_list.index(max_dice) + 1
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2  # Average results


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print(f'always_roll({i}) win rate: {average_win_rate(always_roll(i))}')

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:  # Change to True to test always_roll(8)
        print('final_strategy win rate: ', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    "*** REPLACE THIS LINE ***"
    return 0 if take_turn(0, opponent_score, select_dice(score, opponent_score)) >= margin else num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS if rolling 0 dice results in a harmful swap. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    # BEGIN Question 9
    "*** REPLACE THIS LINE ***"
    if is_swap(score, opponent_score) and score < opponent_score:
        return 0
    elif take_turn(0, opponent_score, select_dice(score, opponent_score)) >= margin:
        return 0
    else:
        return num_rolls
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    By default, rolls 6 for a 6 sided dice and 4 for a 4 sided dice.
    If rolling a lesser number is likely to result in a win, said
    number of dice are rolled.
    If 0 rolls will result in a harmful swap, rolls dice
    Otherwise,
    Swaps if swapping is beneficial.
    Goes for free bacon if it results in a benefical swap
    If the player's score is close to 100, it starts playing safe
    (or using free bacon)
    If bacon strategy gives better result than rolling a 4-sided dice, does not roll
    If bacon strategy will cause the opponent to get a four sided dice
    """

    # BEGIN Question 10

    current_dice = select_dice(score, opponent_score)
    win_margin = 100 - score
    bacon_score = take_turn(0, opponent_score, current_dice)

    if current_dice == six_sided:
        best_num_rolls = 6 if win_margin >= 18 else win_margin // 3
    else:
        best_num_rolls = 4 if win_margin >= 8 else win_margin // 2

    if is_swap(score+bacon_score, opponent_score) and score + bacon_score > opponent_score:
        return best_num_rolls
    elif is_swap(score, opponent_score) and score < opponent_score:  # Swap Strategy
        return 0
    # If bacon strategy will cause a beneficial swap
    elif is_swap(score+bacon_score, opponent_score) and score + bacon_score < opponent_score:
        return 0
    elif take_turn(0, opponent_score, current_dice) >= win_margin/2:  # Bacon Strategy
        return 0
    # If bacon strategy gives better result than rolling a 4-sided dice, does not roll
    elif current_dice == four_sided and bacon_score > 6:
        return 0
    # If bacon strategy will cause the opponent to get a four sided dice
    elif (score + bacon_score + opponent_score) % 7 == 0 and bacon_score > 4:
        return 0
    else:
        return best_num_rolls
    # END Question 10



"""
The section below was commented out because hog eval does not exist.
The file hog_eval as well as hog_gui were not provided. 
"""

##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


# @main
# def run(*args):
#     """Read in the command-line argument and calls corresponding functions.
#
#     This function uses Python syntax/techniques not yet covered in this course.
#     """
#     import argparse
#     parser = argparse.ArgumentParser(description="Play Hog")
#     parser.add_argument('--final', action='store_true',
#                         help='Display the final_strategy win rate against always_roll(5)')
#     parser.add_argument('--run_experiments', '-r', action='store_true',
#                         help='Runs strategy experiments')
#     args = parser.parse_args()
#
#     if args.run_experiments:
#         run_experiments()
#     elif args.final:
#         from hog_eval import final_win_rate
#         win_rate = final_win_rate()
#         print('Your final_strategy win rate is')
#         print('    ', win_rate)
#         print('(or {}%)'.format(round(win_rate * 100, 2)))
