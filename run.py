import time
from helpers import ay_or_an
from questions.questions import Questions
import questions.constants as q_const
from player.player import Player
from monsters.monsters import Monsters
from combat.combat import *
from end_game.end_game import EndGame

# Triggers the entire game
# Do this by python run.py

def run():
  print("Welcome to this Fantasy Adventure Game! \n")
  time.sleep(1)

  # Select difficulty - changes no of enemies faced
  print("You will face a number of enemies which you must vanquish.")
  print("The number depends on which difficulty you pick... \n")
  selected_difficulty = Questions.difficulty()
  no_of_enemies = 3 + q_const.difficulty_options.index(selected_difficulty)
  print(f"Your game difficulty is set to {selected_difficulty}. \n")
  time.sleep(1)

  # Create character - class determines abilities
  print("Now, let's create your character.")
  print("Please select a species and class... \n")
  selected_character = Questions.character_creation()
  print("Great! You will be playing as {} {} {}.".format(
                                                    ay_or_an(selected_character["species"]),
                                                    selected_character["species"],
                                                    selected_character["class"])
  )

  # Initialise game
  player = Player(selected_character["species"], selected_character["class"])
  monsters_list = Monsters.create_lineup(no_of_enemies)
  level = 1

  # Start combat
  print(f"You will now face {no_of_enemies} enemies. Defeat them all to win the game. \n")
  time.sleep(2)

  # Continue until all monsters are defeated
  while level <= no_of_enemies:
    monster = monsters_list[level - 1] # zero index
    print("The {} enemy approaches... It's {} {} with {} Hit Points. \n".format(
                                                                          monster.position,
                                                                          ay_or_an(monster.name),
                                                                          monster.name,
                                                                          monster.hit_points)
    )
    time.sleep(1)

    # Continue until this monster is defeated
    while monster.hit_points > 0:
      print("Which ability will you use? \n")

      abilities = player.get_current_abilities()
      chosen_ability_name = Questions.choose_ability(abilities)
      ability = player.use_ability(chosen_ability_name)

      if ability.initiative == 1:
        # player goes first
        if ability.damage < 0:
          player_heal(player, ability)
        else:
          player_attack(player, ability, monster)
        time.sleep(1)

        # monster goes second
        if monster.hit_points == 0:
          break
        monster_attack(monster, player)
        if player.hit_points == 0:
          EndGame.run_lose(monster.name)
        time.sleep(1)

      else:
        # monster goes first
        monster_attack(monster, player)
        if player.hit_points == 0:
          EndGame.run_lose(monster.name)
        time.sleep(1)

        # player goes second
        if ability.damage < 0:
          player_heal(player, ability)
        else:
          player_attack(player, ability, monster)
        time.sleep(1)
    
    print(f"Well Done! You defeated the {monster.name}. \n")
    level += 1
    time.sleep(2)

  EndGame.run_win()

if __name__ == "__main__":
  run()