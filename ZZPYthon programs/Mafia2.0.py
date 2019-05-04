import random
accuselist = ["I think it is him!!", "I'm not sure who it is, but we have to find out quick!", "It's got to be Jack!", "SOMEONE GET ME BACON.", "I think it is her!!"]
playerrole = random.randint(1, 5)     
vilcount = 5
kaylee = True
jack = True
raegan = True
rhett = True   
k1 = 0
j1 = 0
r2 = 0
r3 = 0
r1 = 0


def jury(jurylist, vils, killorder, playars, k1, j1, r1, r2, r3, kaylee, jack, raegan, rhett, accuselist):
    choice1 = random.choice(jurylist)
    choice1 = choice1 + 1
    
    
    

def killmech(killorder, playars, k1, j1, r1, r2, r3, kaylee, jack, raegan, rhett, accuselist):
    vils = 5
    jurylist = [k1, r1, j1, r2, r3]
    if killorder.lower() == 'kaylee' and kaylee == True:
        kaylee = False
        playars.remove('kaylee')
        jurylist.remove(k1)
        vils -= 1
        print("Kaylee has been killed.")
        print("Everyone else, {}, is delibrating to find out who killed Kaylee. If the villagers reach a majority, the person will be executed.".format(playars))
        jury(jurylist, vils, killorder, playars, k1, j1, r1, r2, r3, kaylee, jack, raegan, rhett, accuselist)

def gameplay():
    playars = ['kaylee', 'jack', 'raegan', 'rhett']
    playername = input("Please enter your name ")
    if 1 == 1:# playerrole == 1 or playerrole == 5:
        print("You are the mafia, {}. You must kill all of the villagers without being found out.".format(playername))
        print("There are 4 other players, Kaylee, Jack, Raegan, and Rhett.")
        killorder = input("Choose a player to kill.")
        killmech(killorder, playars, k1, j1, r1, r2, r3, kaylee, jack, raegan, rhett, accuselist)
#Design this for single player


        
gameplay()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        