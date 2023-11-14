# Abilities [Name, Damage, Initiative, Verb]
# If Damage is negative ability is a heal.
# Damage (and inverse of heal) should add up to 7.
# Initiative should be 1 or 2, heals are always 1

abilities = {
  "warrior": [("Charge", 1, 1, "use"), ("Mortal Strike", 4, 2, "use"), ("Warcry", -2, 1, "use")],
  "ranger": [("Quick Shot", 2, 1, "use"), ("Ranged Shot", 3, 2, "use"), ("Nature Mend", -2, 1, "use")],
  "mage": [("Fire Bolt", 3, 1, "cast"), ("Frost Bolt", 2, 2, "cast"), ("Protective Ward", -2, 1, "cast")],
  "cleric": [("Holy Fire", 2, 1, "cast"), ("Smite", 2, 2, "cast"), ("Cure Wounds", -3, 1, "cast")],
  "rogue": [("Throwing Knives", 4, 1, "use"), ("Slash", 2, 2, "use"), ("Bottle of Rum", -1, 1, "use")],
}
