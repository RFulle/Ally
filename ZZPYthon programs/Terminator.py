# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:45:03 2019

@author: rhysa
"""
import time


def COMMAND_(user):
  order = input("PLEASE GIVE A COMMAND_ ")
  if order == "terminate":
    target1 = input("PLEASE IDENTIFY TARGET:_")
    target1 = target1.upper()
    if target1 == user:
        print("Invalid. Computer cannot target prime user.")
        COMMAND_(user)
    else:
        print("UNDERSTOOD. POWERING UP DRONES...")
        time.sleep(2)
        print("DRONES POWERED UP. MOVING TO POSITION...")
        time.sleep(4)
        weapon = input("CHOOSE WEAPON: SNIPER RIFLE OR ROCKET PROPELLED GRENADE(RPG)_")
    if weapon == "sniper rifle":
        time.sleep(1)
        print("UNDERSTOOD.")
        print("DRONES IN POSITION.")
        time.sleep(.4)
        print("OTHER CIVILIANS IN AREA, INCLUDING PRIMARY USER.")
        print("GETTING LIST...")
        time.sleep(.3)
        print('''LIST: : : : :
               {}, TARGET
               :
               RAEGAN NELLE FULLER, CIVILIAN, NON-TARGET
               :
               RHETT BUTLER FULLER, CIVILIAN, NON-TARGET
               :
               RHYS ANDREW FULLER, PRIMARY USER, NON-TARGET
               : : : : : : : : : : : : :
               '''.format(target1))
        time.sleep(4)
        ords = input("ENGAGE ALL IN AREA, OR ENGAGE SINGLE TARGET_")
    else:
        print("OUT OF AMMO, RETURNING TO BASE..")
        time.sleep(1)
        print("AT BASE. RESTARTING...")
        COMMAND_('rhys')
    if ords == "target":
        print("UNDERSTOOD. WEAPONS POWERING UP...")
        time.sleep(2)
        print("WEAPONS STILL POWERING UP...")
        time.sleep(1)
        print("WEAPONS POWERED ON. LOADING WEAPONS")
        time.sleep(1)
        print("WEAPONS LOADED.")
        time.sleep(.7)
        print("TARGET: {}".format(target1))
        time.sleep(.5)
        print("TARGET IDENTIFIED...")
        time.sleep(.6)
        print("TARGET IN PROXIMITY...")
        ods = input("ENGAGE TARGET: Y/N_")
        print("TERMINATING...........")
        print('-')
        time.sleep(.2)
        print('/')
        time.sleep(.2)
        print('|')
        time.sleep(.2)
        print(''' \ ''')
        time.sleep(.2)
        timer = 4
        while timer > 0:
               print('-')
               time.sleep(.25)
               timer = timer - 1
        print("TERMINATED.")


COMMAND_('Rhys')