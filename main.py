print('''
                  _______________________________________________________
                  |                                                      |
             /    |                                                      |
            /---, |                 Bandit Slaughter                     |
       -----# ==| |                                                      |
       | :) # ==| |                                                      |
  -----'----#   | |______________________________________________________|
  |)___()  '#   |______====____   \___________________________________|
 [_/,-,\"--"------ //,-,  ,-,\\\   |/             //,-,  ,-,  ,-,\\ __#
   ( 0 )|===******||( 0 )( 0 )||-  o              '( 0 )( 0 )( 0 )||
----'-'--------------'-'--'-'-----------------------'-'--'-'--'-'--------------
''')
print("Welcome to Bandit Slaughter!")
print("Your mission is to survive a bandit attack.\n")

print("It's just another day in paradise. No guns, no food, no water. The hot sun beats down on you and the surrounding desert. You spot a shack on a hill in the distance and head towards it to look around for supplies.\n")
print("It's an old rusty metal shack with no door and a window. Hardly a place to sleep. You find nothing of value, except for a few scraps of food. Suddenly, you hear engines in the distance. A bandit patrol is getting closer! They don\'t know you\'re here... you could easily ambush them!\n")

choice1 = input('1. Do you wait for them in the shack, go outside and take cover or try to escape before they arrive? Type "wait", "outside" or "escape" \n')

if choice1 == "wait":
  print("You decide to wait by the window. As you kneel down you notice that a floorboard is loose. You uncover it to find a handgun and 1 magazine! Yes!\n")
  choice2 = input('2. The patrol arrives. There are 2 cars, 2 motorbikes and 6 bandits in total. Do you surprise them by shooting or wait for them to come inside the shack? Type "surprise" or "wait" \n')
  if choice2 == "surprise":
    print("You open fire on the bandits. They scatter and take cover behind their vehicles. A long firefight ensues and you run eventually out of ammo. The bandits rush inside the shack and shoot you dead. Game over.")
  elif choice2 == "wait":
    print("You decide to wait. The bandits take a look around outside before 2 check out the shack. As they enter you open fire and kill them dead.\n")
    choice3 = input('3. The other bandits have taken cover and started firing at the shack. Do you return fire or search the bodies? Type "fire" or "search" \n')
    if choice3 == "fire":
      print("You return fire on the bandits. As you start to get low on ammo, a bandit sneaks up to the doorway beside you and shoots you dead. Game over.")
    elif choice3 == "search":
      print("You search the bodies and find another handgun, some ammo and a grenade!\n")
      choice4 = input('4. The bandits are still taking cover by their vehicles. Do you rush out of the building guns ablazing, wait for them to come to you or chuck a grenade into the middle of their vehicles? Type "rush", "wait" or "grenade" \n')
      if choice4 == "rush":
        print("You rush outside, duel weilding handguns. It probably looks awesome but you get shot down quicker than a cowboy in the wild west. Game over.")
      elif choice4 == "wait":
        print("You wait, but then you realise something. If these dead bandits had a grenade, the other bandits might have o-- BOOM. Game over.")
      elif choice4 == "grenade":
        print("You throw a grenade out the window and it lands right in the middle of their parked vehicles. You hear a big explosion and muffled cries. You take a look out the window and see no signs of life. Luckily, one of the bandit motorbikes wasn't caught in the explosion. You start up the engine and ride off into the distance. Congratulations! You won! ")
elif choice1 == "outside":
  print("You decide to wait for them outside. As you run out the door you notice a big rock to your right. You run over to it and hide.\n")
  choice2 = input('2. The patrol arrives. There are 2 cars, 2 motorbikes and 6 bandits in total. Do you wait for a bandit to walk by and ambush them or throw a small rock to draw their attention? Type "wait" or "throw" \n')
  if choice2 == "wait":
    print("You wait, but none of the bandits come close enough for you to ambush them. You decide to hide whilst they search the shack and leave. Once they leave, you carry on walking into the desert with no food or water. Who knows how long you'll last... Game over. ")
  elif choice2 == "throw":
    print("You throw a rock over towards the shack. It ricochets off the metal and alerts the bandits. Most of them go and check out the sound. One stays behind fairly close to you and the vehicles.\n")
    choice3 = input('3. This is your chance! Do you sneak up behind the bandit and take him out or whistle for him to come closer? Type "sneak" or "whistle" \n')
    if choice3 == "sneak":
      print("You sneak up slowly and quietly behind the bandit. You were almost there until you accidentally kicked a rock. The bandit yells in surprise and shoots you dead. Game over.")
    elif choice3 == "whistle":
      print("You whistle at the nearby bandit. They hear it and start to move towards the rock with their gun ready. As they're about to pass you, you grab their gun and give them a hefty punch, knocking them out cold. You search the bandit and find an uzi, ammo and a grenade.\n")
      choice4 = input('4. The bandits are still searching the shack. There are 2 outside and 3 inside. Do you chuck a grenade at them, open fire at them or try to escape in one of their vehicles? Type "grenade", "fire" or "escape" \n')
      if choice4 == "grenade":
        print("You chuck a grenade at the shack and it explodes, killing the 2 standing outside. The other 3 rush out as you open fire on them. 1 takes cover behind a car, the other two run left and right in an attempt to flank you. You try to hold your ground but they are fast and before you can react, they appear either side and shoot you dead. Nice try. Game over.")
      if choice4 == "fire":
        print("You open fire on the 2 standing outside, killing them quickly. You reload as the other 3 rush out but they are easily gunned down by your superior firepower. You search all the dead bandits before making your escape in one of their cars. Congratulations! You won! ")
      if choice4 == "escape":
        print("You sneak over to one of the motorbikes, praying that they left the keys in the ignition. They did! You start the engine and try to make your getaway but you are gunned down very quickly by the bandits. Did you honestly think that would work? Game over.")
elif choice1 == "escape":
  print("You decide to make a run for it! You quickly gather the scraps of food and run out the door but it's too late! The bandit patrol is here! They gun you down quicker than you can say apocalypse! Game over.")
else:
  print("I suppose you thought that was terribly clever. Restart the game.")