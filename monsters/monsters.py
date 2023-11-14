import random
import monsters.constants as constants
from dice.dice import Dice

# Defines the monster line-up the player will face

class Monster:
  def __init__(self, name: str, position: str):
    """
    Monster object

    :param Monster self: The monster object
    :param str name: The name of the monster
    :param str position: The position of the monster in the queue
    """
    self.name = name
    self.position = position
    self.hit_points = random.randint(5,10)

  def calc_damage(self):
    """
    Determines how much damage the monster's attack deals

    :param Monster self: The monster object
    :return int: Damage dealt by the monster
    """
    damage = Dice.roll_dice_d(6)
    return damage
  
  def set_hit_points(self, damage: int):
    """
    Sets the monster's hit points after taking damage - min 0

    :param Monster self: The monster object
    :param int damage: The amount of damage
    """
    if damage < self.hit_points:
      self.hit_points -= damage
    else:
      self.hit_points = 0

class Monsters:
  @staticmethod
  def create_lineup(number: int):
    """
    Creates a list of monsters from a pool of names - number determined by difficulty

    :param int number: The number of monsters
    :return list[Monster]: A list of the monsters the player must face
    """
    lineup: list[Monster] = []
    queue_position = ["first", "second", "third", "forth", "final"]
    for i in range(number):
      index = i if i != number - 1 else -1 # follow queue position unless final monster
      no_of_options = len(constants.enemy_names) - 1 # zero index
      rand_monster_from_list = constants.enemy_names[random.randint(0, no_of_options)]
      monster = Monster(rand_monster_from_list, queue_position[index])
      lineup.append(monster)

    return lineup