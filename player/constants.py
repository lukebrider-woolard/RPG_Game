# Abilities [Name, Damage, Initiative, Verb]
# If Damage is negative ability is a heal.
# Total damage of all abilities for a class should equal 3
# Initiative should be 1 or 2, heals are always 1

abilities = {
  "warrior": [("Mortal Strike", 4, 2, "use"), ("Charge", 1, 1, "use"), ("Warcry", -2, 1, "use")],
  "hunter": [("Ranged Shot", 3, 2, "use"), ("Quick Shot", 2, 1, "use"), ("Nature Mend", -2, 1, "use")],
  "mage": [("Frost Bolt", 3, 2, "cast"), ("Fire Bolt", 2, 1, "cast"), ("Protective Ward", -2, 1, "cast")],
  "priest": [("Smite", 2, 2, "cast"), ("Holy Fire", 2, 1, "cast"), ("Heal Wounds", -3, 1, "cast")],
  "rogue": [("Slash", 2, 2, "use"), ("Throwing Knife", 3, 1, "use"), ("Bottle of Rum", -2, 1, "use")],
}
