import inquirer
import questions.constants as constants

# Asks the player questions and allows them to choose an answer in the terminal

class Questions:
  @staticmethod
  def difficulty() -> str:
    """
    Asks the player to set the difficulty

    :return str: The difficulty set by the player
    """
    questions = [inquirer.List('difficulty',
                            message='Please select a difficulty:',
                            choices=constants.difficulty_options,
                            )
    ]
    
    difficulty_choice = inquirer.prompt(questions)
    return difficulty_choice['difficulty']

  @staticmethod
  def character_creation() -> dict[str: str]:
    """
    Asks the player to create a character

    :return dict[str, str]: The species and class of the player character
    """
    questions = [
      inquirer.List('species',
                    message="My species is",
                    choices=constants.species_options,
                    ),
      inquirer.List('class',
                    message="My class is",
                    choices=constants.class_options
                    )
    ]

    character_choices=inquirer.prompt(questions)
    return character_choices
  
  @staticmethod
  def choose_ability(abilities: list[str]) -> str:
    """
    Asks the player to choose an ability

    :param list[str] abilities: The names of abilities currently available
    :return str: The name of the ability chosen by the player
    """
    question = [
      inquirer.List('ability',
                    message="Use",
                    choices=abilities
                    )
    ]

    ability_choice = inquirer.prompt(question)
    return ability_choice['ability']