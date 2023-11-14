import random

class Dice:
  @staticmethod
  def roll_dice_d(no_of_sides: int):
    """
    Roll a dice with a set number of sides

    :param int no_of_sides: The number of sides of the dice
    :return int: The dice result
    """
    return random.randint(1,no_of_sides)