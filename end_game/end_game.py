import time

class EndGame:
  @staticmethod
  def run_lose(monster_name: str):
    """
    Ends the game when the player loses

    :param str monster_name: The name of the monster
    :return print:
    """
    print(f"Oh no! You've been slain by the {monster_name}. You lose the game. \n")
    time.sleep(1)
    print("Thank you for playing.")
    exit()

  @staticmethod
  def run_win():
    """
    Ends the game when the player wins

    :return print:
    """
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("Congratulations! You've beaten the game. \n")
    time.sleep(1)
    print("Thank you for playing.")
    exit()