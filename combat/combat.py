from player.player import Player, Ability
from monsters.monsters import Monster

def player_heal(player: Player, ability: Ability):
  """
  Heal the player, healing hit points - used when ability damage is negative

  :param Player player: The player object
  :param Ability ability: The ability object
  :return print:
  """
  heal = player.calc_heal(ability)
  player.set_hit_points(heal)
  heal_text = heal * -1 # convert to positive num
  print("\nYou {} {}. It heals you for {} hit points up to {}. \n".format(
                                                                  ability.verb,
                                                                  ability.name,
                                                                  heal_text,
                                                                  player.hit_points)
  )

def player_attack(player: Player, ability: Ability, monster: Monster):
  """
  Player attacks monster, dealing damage - used when ability damage is positive

  :param Player player: The player object
  :param Ability ability: The ability object
  :param Monster monster: The monster object
  :return print:
  """
  damage = player.calc_damage(ability)
  monster.set_hit_points(damage)
  print("You {} {}. It deals {} damage to the enemy! The {} is reduced to {} hit points. \n".format(
                                                                                              ability.verb,
                                                                                              ability.name,
                                                                                              damage,
                                                                                              monster.name,
                                                                                              monster.hit_points)
  )

def monster_attack(monster: Monster, player: Player):
  """
  Monster attacks player, dealing damage

  :param Monster monster: The monster object
  :param Player player: The player object
  :return print:
  """
  damage = monster.calc_damage()
  player.set_hit_points(damage)
  print("\nThe enemy {} attacks you for {} damage. Your hit points are reduced to {}. \n".format(
                                                                                            monster.name,
                                                                                            damage,
                                                                                            player.hit_points)
  )