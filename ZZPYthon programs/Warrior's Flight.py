#Chris's Game
#
#Warrior's Flight
#
#Programmed by Ally Coding (C)
import time, random
def goblinai(goblin1, hp):
       print()
       if goblin1 <= 0:
              return 0
       elif goblin1 > hp:
              print("The Goblin cackles, for he knows you're at his mercy!")
              return 100
       elif goblin1 < hp:
              print("The Goblin feels threatened! He attacks!")
              return 50
       else:
              print("ULTRA CRITICAL!!!!")
              return 100000000
def weaponchooser():
       while 1 == 1:
              print("What weapon would you like?")
              print()
              print('''OPTIONS:
                     Knife
                     Sword
                     Bow
                     Spear
                     Axe
                     ''')
              weapon = input("_")
              weapon = weapon.lower()
              if weapon != 'knife' and weapon != 'sword' and weapon and 'bow' and weapon != 'spear' and weapon !='axe':
                     print("We don't have that in our armory. Please choose another weapon from the OPTIONS list.")
              else:
                     break
       return weapon
goblin1 = 100
macho = False
beauty = False
halfelf = False
goblin = False
defensive = False
dwarf = False
elf = False
human = False
shade = False
dryad = False
natureblessing = False
darkness = False
shadelore = False
ingenuity = False
sturdiness = False
time.sleep(.1)
print()
print("Please select your race: ")
print()
race = input('''OPTIONS:
              Half Elf
              Goblin
              Dwarf
              Elf
              Human
              Shade
              Dryad
              _''')
race = race.lower()
if race == 'half elf':
       halfelf = True
elif race == 'goblin':
       goblin = True
elif race == 'dwarf':
       dwarf = True
elif race == 'elf':
       elf = True
elif race == 'human':
       human = True
elif race == 'shade':
       shade = True
elif race == 'dryad':
       dryad = True
print()
print("Please Select Your Gender: ")
sex = input("OPTIONS: {M}ale or {F}emale")
sex = sex.lower()
if sex == 'm' and (dwarf == True or elf == True):
       roll = random.randint(1,2)
       if roll == 2:
              macho = True
              print("Due to your inherent manliness, you are gifted with the ability Macho.")
elif sex == 'm' and dwarf != True:
       roll = random.randint(1,10)
       if roll == 2:
              macho = True
              print("Due to your inherent manliness, you are gifted with the ability Macho.")
elif sex == 'f' and (dryad == True or elf == True):
       beauty = True
       print("Due to your inherent beauty and charm, you are gifted with the ability Beauty.")
elif sex == 'f' and dryad != True and elf != True:
       roll = random.randint(1,2)
       if roll == 2:
              beauty = True
              print("Due to your inherent beauty and charm, you are gifted with the ability Beauty.")
print("You are a {} {}".format(sex, race))
print()
while 1 == 1:
       print("You have 20 points to use. If the point totals do not add up to 20, you will have to redo this step.")
       print('''There are 6 categories:
              STRENGTH
              AGILITY
              INTELLIGENCE
              WILLPOWER
              LUCK
              CHARISMA
              ''')
       strth = int(input("How many points do you want to put in Strength? "))
       agi = int(input("How many points do you want to put in Agility? "))
       intel = int(input("How many points do you want to put in Intelligence?"))
       wilpw = int(input("How many points do you want to put in Willpower? "))
       luck = int(input("How many points do you want to put in Luck? "))
       chari = int(input("How many points do you want to put in Charisma? "))
       totalpoints = strth + agi + intel + wilpw + luck + chari
       if totalpoints == 20:
              break
       else:
              print("I'm afraid that doesn't equal 20. Try again.")
              time.sleep(1)
print()
time.sleep(1)
print("Now let's decide your attribute(s). It will randomely be decided based on your gender, race, and your Luck point value.")
print()
if elf == True or halfelf == True or dryad == True:
       natureblessing = True
       print("You have been gifted with Nature's Blessing! This will allow you to positively interact with certain creatures of the light! It also gives you plus 3 luck! If your luck is greater than or equal to 5 before the added luck you will also get 10 agility!")
       if luck >= 5:
              agi = agi + 5
       luck = luck + 3
if halfelf == True or human == True:
       print("You have been gifted with Ingenuinty! Plus 3 Intelligence and 4 Willpower!")
       intel = intel + 3
       wilpw = wilpw + 4
       ingenuity = True
time.sleep(1)
if dwarf == True or goblin == True:
       print("You have been gifted with Sturdiness! Plus 3 Strength! Ability to withstand KO attacks with more than one HP!")
       strth = strth + 1
       sturdiness = True
if goblin == True or shade == True:
       print("You have been gifted with Darkness! This will unlock the ability to positively interact with certain dark beasts.")
       darkness = True
if shade == True:
       print("Due to your Shaden upbringing, you have extensive knowledge of Shade Lore. This gives the battle ability 'Shadow Merge,' which will allow you confuse your enemy and stab them in the back.")
       shadelore = True
time.sleep(1)
print()
print("Now it is time to arm you. Some races do not have a choice on what weapons they will get. If you are one of those races, you will simply be told what your weapon is and then move on.")
time.sleep(1)
if dwarf == True:
       weapon = 'axe'
elif shade == True:
       weapon = 'knife'
elif elf == True:
       weapon = 'bow'
else:
       weapon = weaponchooser()
time.sleep(2)
print("You are armed with a {}!".format(weapon))
time.sleep(1)
print("Please choose your class: ")
print()
time.sleep(.5)
print(''' OPTIONS:
       RANGER
       MAGE
       BRAWLER
       ''')
clas = input("_")
clas = clas.lower()
if clas == 'ranger':
       agi = agi * 3
       luck = intel * 4
elif clas == 'mage':
       intel = intel * 3
       chari = wilpw * 4
elif clas == 'brawler':
       strth = strth * 3
       wilpw = chari
print("Your class is {}".format(clas))
print("You are now ready to start adventuring!")
time.sleep(1)
print("Welcome, Traveler. ")
hp = 100 * strth
endurance = (20 + intel) * wilpw
print("You have {} health remaining and {} endurance left.".format(hp, endurance))
print()
time.sleep(1)
print("You set out in quest of finding the secret of the Warrior's Flight, a mystical power that enables infinite agility. Your sensai has suggested that you find Celestia, an immortal guardian of wisdom. Celestia lives in the 10th level of the dungeons of Fel Kim.")
time.sleep(2)
print("You enter the first level of Fel Kim. You hold your {} close, for you know that mobs and baddies lurk in every corner. Suddenly, a goblin attacks!".format(weapon))
time.sleep(1)
while goblin1 > 0 and hp > 0:
       print("Ready thyself! Do you want to (1) Use a Physical Move, (2) Use a Magic Move, or (3) Use an Ability or Item?")
       myaction = int(input())
       if myaction == 1:
              print("You chose Physical Move! Do you want to (1) use your {} or (2) move to a defensive position?".format(weapon))
              myaction = int(input())
              if myaction == 1:
                     damage = (strth * 3) - 5
                     print("You dealt {} damage!".format(damage))
                     goblin1 = goblin1 - damage
              elif myaction == 2:
                     defensive = True
              else:
                     print("Your indecision made you loose your turn!")
       elif myaction == 2:
              print("You chose Magical Move! Do you want to (1) Heal, or (2) Use FireBlast?")
              myaction = int(input())
              if myaction == 1:
                     if hp < (100 * strth):
                            hp = hp + 50
                     print("You are healed! Your health now equals {}!".format(hp))
              elif myaction == 2:
                     print("You attack with FireBlast! Since Goblins are dumb, it is especially effective!")
                     damage = intel * 3
                     goblin1 = goblin1 - damage
       elif myaction == 3:
              if shade == True:
                     print("You use Shadow Merge! You disappear into the darkness and then reamerge to stab the goblin in the back!")
                     goblin1 = 0
              else:
                     print("You have no battle abilities and while you were checking your bag the goblin attacked!")
       damagetkn = goblinai(goblin1, hp)
       dmg = damagetkn - strth
       dodge = random.randint(1, agi)
       if luck > dodge or dodge > 7:
              print("You dodged the attack! No damage taken!")
       else:
              print("You took {} damage!".format(dmg))
if hp <= 0:
       print("You have died.")
       time.sleep(3)
       exit()
else:
       time.sleep(2)
       print("The goblin has been defeated!")
print("Congratulations! You have gained enough experience to increase a level! You now have 5 skill points to use!")
time.sleep(1)
counter = 5
while counter != 0:
       print('''Please choose which skill you'd like to add 1 point to:
              OPTIONS:
                     (S)trength
                     (A)gility
                     (I)ntelligence
                     (W)illpower
                     (L)uck
                     (C)harisma''')
       op = input()
       op = op.lower()
       if op == 's':
              strth = strth + 1
       elif op == 'a':
              agi = agi + 1
       elif op == 'i':
              intel = intel + 1
       elif op == 'w':
              wilpw = wilpw + 1
       elif op == 'l':
              luck = luck + 1
       else:
              chari = chari + 1
       counter = counter - 1
print("You carry on through the dungeon!")