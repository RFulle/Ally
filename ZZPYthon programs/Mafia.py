import random

def jacksrandom():
    players = ['Jack', 'Raegan', 'Kaylee', 'Rhys', 'Rhett']
    mafiaplayer = random.choice(players)
    nurse = random.choice(players)
    vil3 = random.choice(players)
    vil1 = random.choice(players)
    vil2 = random.choice(players)
    if mafiaplayer == nurse or mafiaplayer == vil1 or mafiaplayer == vil2 or mafiaplayer == vil3:
        mafiaplayer = random.choice(players)
    if nurse == mafiaplayer: 
        nurse = random.choice(players)
    elif nurse == vil1 or nurse == vil2 or nurse == vil3:
        nurse = random.choice(players)
    if vil1 == nurse or vil1 == mafiaplayer or vil1 == vil2 or vil1 == vil3:
        vil1 = random.choice(players)
    if vil2 == nurse or vil2 == mafiaplayer or vil2 == vil1 or vil2 == vil3:
        vil2 = random.choice(players)
    if vil3 == nurse or vil3 == mafiaplayer or vil3 == vil2 or vil3 == vil1:
        vil3 = random.choice(players)
        
    print(players)
    print(mafiaplayer)
    print(nurse)
    print(vil1)
    print(vil2)
    print(vil3)
#jacksrandom()


players = ['You Are The MAFIA', 'You are the Sheriff', 'YOU ARE A VILLAGER', 'YOU ARE A VILLAGER', 'YOU ARE A VILLAGER']


#@print(random.choice(players))
#Look at that!


def randomlist(a):
    b = []
    for i in range(len(a)):
        element = random.choice(a)
        a.remove(element)
        b.append(element)
        print(element)
        print('''
              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ''')
randomlist(players)