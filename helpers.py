# Not foolproof --- can result in 'an unicorn'. 
def ay_or_an(noun):
  """
  Returns 'a' or 'an' depending on what letter the following noun starts with

  :param str noun: The noun that will go after the 'a' or 'an'
  :return str: 'a' or 'an'
  """
  vowel = ["A","E","I","O","U"]
  if noun[0].upper() in vowel:
    return "an"
  else:
    return "a"