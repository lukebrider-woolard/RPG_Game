import player.constants as constants
from dice.dice import Dice

# Defines the player's character and abilities

class Ability:
  def __init__(self, ability_tuple : tuple):
    """
    Ability object

    :param tuple ability_tuple: Hard-coded tuple of abilities consisting of
      name str: The name of the ability
      damage int: The amount of damage the ability causes - negative value for heal
      initiative int: Whether the ability is performed before or after the monster's turn
      verb str: Whether the ability is used or cast
    """
    self.name, self.damage, self.initiative, self.verb = ability_tuple

class Player:
  def __init__(self, selected_species: str, selected_class: str):
    """
    Player object

    :param Player self: The player object
    :param str selected_species: The species of the player character
    :param str selected_class: The class of the player character
    """
    self.player_species = selected_species
    self.player_class = selected_class
    self.hit_points = 25
    self.last_used_ability = ""
    self.abilities: list[Ability] = []

    for ability in constants.abilities[selected_class.lower()]:
      self.abilities.append(Ability(ability))

  def set_hit_points(self, damage: int):
    """
    Sets the player's hit points after taking damage - min 0

    :param Player self: The player object
    :param int damage: The amount of damage
    """
    if damage < self.hit_points:
      self.hit_points -= damage
    else:
      self.hit_points = 0

  def set_last_used_ability(self, ability_name: str):
    """
    Used to prevent a player using the same ability twice in a row

    :param Player self: The player object
    :param str ability_name: The ability the player just used
    """
    self.last_used_ability = ability_name

  def get_current_abilities(self):
    """
    Return a list of ability names available to the player

    :param Player self: The player object
    :return list[str]: The list of ability names
    """
    available_abilities: list[str] = []
    for ability in self.abilities:
      if ability.name != self.last_used_ability:
        available_abilities.append(ability.name)
    
    return available_abilities

  def use_ability(self, ability_name: str):
    """
    Return an ability object based on the name

    :param Player self: The player object
    :param str ability_name: The name of the ability the player is using
    :return Ability: The ability object the player is using
    """
    for ability in self.abilities:
      if ability_name == ability.name:
        self.set_last_used_ability(ability_name)

        return ability
  
  def calc_damage(self, ability: Ability):
    """
    Determines how much damage the player's attack deals

    :param Player self: The player object
    :param Ability ability: The ability the player is using
    :return int: Damage dealt by the player
    """
    damage = ability.damage + Dice.roll_dice_d(3)
    return damage
  
  def calc_heal(self, ability: Ability):
    """
    Determines how much health the player heals

    :param Player self: The player object
    :param Ability ability: The ability the player is using
    :return int: Heal to be applied to the player
    """
    heal = ability.damage - Dice.roll_dice_d(3)
    return heal