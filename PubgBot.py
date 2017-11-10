import os
import time
import random
import tkinter
import pyautogui

debug_me = 0
clear = lambda: os.system('cls')
leave_game = int
wait_to_drop = int
grounded_time = 0
fuck_nig = int

def short_count_down():
    for i in range(1, 6) [::-1]:
        print(str(i)+'..')
        time.sleep(1)

def Stop_Bot():
    print('Stopped THE BOT!')
    time.sleep(1000000)
    Stop_Bot()

def end_game_restart():
    time.sleep(3)
    if pyautogui.pixelMatchesColor(875, 591, (255, 255, 255)) and pyautogui.pixelMatchesColor(750, 597, (255, 255, 255)) is True:
        pyautogui.click(841, 572)
        time.sleep(1)
        pyautogui.click()
        time.sleep(5)
        fallback_debug_self_fix()

def on_land_check():
    global leave_game
    global grounded_time
    print('Are you on land?')
    print(leave_game)
    leave_game -= grounded_time
    print(leave_game)
    print(grounded_time)
    if pyautogui.pixelMatchesColor(1805, 889, (17, 48, 62), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (20, 55, 72), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (27, 62, 84), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (23, 58, 78), tolerance=20) is True:
        for i in range(1, leave_game) [::-1]:
            print('Time left before restart:'+str(i)+'')
            pyautogui.keyDown('space') 
            time.sleep(0.5)
            pyautogui.keyUp('space')
            time.sleep(0.5) 
        pyautogui.press('escape')        
        end_game_restart()
    else:
        time.sleep(5)
        leave_game -= 5
        pyautogui.press('z')
        for i in range(1, leave_game) [::-1]:
            print('Time left before restart:'+str(i)+'')
            time.sleep(1)
        pyautogui.press('escape')
        end_game_restart()

def parachute_max_distance():
    global grounded_time
    print('now we have to press w alot faggot')
    for i in range(1, 150) :
        print('You pressed W this many times:'+str(i)+'')
        grounded_time += 1
        if pyautogui.pixelMatchesColor(172, 38, (255, 255, 255)) and pyautogui.pixelMatchesColor(172, 53, (255, 255, 255)) is True:
            
            pyautogui.keyDown('w') 
            time.sleep(0.5)
            pyautogui.keyUp('w')
            time.sleep(1)
        else:
            on_land_check()
    fallback_debug_self_fix()

def playing_game_check():
    global wait_to_drop
    global leave_game
    print('game started!')
    for i in range(1, 1000):
        print('Check to see if over water yet! '+str(i)+'')
        if pyautogui.pixelMatchesColor(1805, 889, (25, 61, 82), tolerance=20) is True:
            wait_to_drop = random.randint(1, 32)
            leave_game = 265 - wait_to_drop
            leave_game -= 24
            print(leave_game)
            print(wait_to_drop)
            print('this is how long you have till you leave in seconds!')
            print('you are flying over water')
            time.sleep(23)
            print('dont sleeping?')
            time.sleep(wait_to_drop)
            pyautogui.press('f')
            time.sleep(9)
            pyautogui.press('f')
            print('F was hit')
            parachute_max_distance()
    print('can you drop!?')
    fallback_debug_self_fix()

def second_in_game_check():
    for i in range(1, 80):
        print('Times check to see if game started '+str(i)+'seconds')
        time.sleep(1)
        if pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) is not True:
            if pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is not True:
                print('found it')
                playing_game_check()
    print('TF is happening?')
    second_in_game_check()
def in_game_check():
    for i in range(1, 80):
        print('Times check to see if you are in game '+str(i)+'seconds')
        time.sleep(1)
        if pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) and pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            print('found it!')
            second_in_game_check()
    fallback_debug_self_fix()

def lobby_play_check():
    global debug_me
    global leave_game
    global wait_to_drop
    global grounded_time
    print('\nDebug level is currently'+'~'+str(debug_me)+'~\n')
    leave_game = 0
    wait_to_drop = 0
    grounded_time = 0
    if debug_me == 1:
        time.sleep(2)
        fallback_debug_self_fix()
    elif debug_me == 0:
        pyautogui.tripleClick(956, 539)
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) and pyautogui.pixelMatchesColor(94, 15, (207, 136, 14)) is True:
            time.sleep(0.5)
            pyautogui.moveTo(195, 51)
            time.sleep(0.5)
            pyautogui.click(81, 715)
            time.sleep(0.5)
            start_game_check()
        else:
            time.sleep(1)
            debug_me = 1
            print('Issue found we are starting to debug!\nThis will take less than a minute!\n')
            lobby_play_check()
    else:
        time.sleep(1)
        print('Nothing is happening\n')
        fallback_debug_self_fix()

def start_game_check():
    if pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True:
        time.sleep(0.5)
        pyautogui.click(184, 717)
        start_game_check()
    elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:
        time.sleep(0.5)
        pyautogui.click(195, 51)
        print('wow it worked!')
        time.sleep(0.5)
        in_game_check()
    else:
        time.sleep(1)
        print('WTF IS GOING ON!')
        debug_me = 1
        lobby_play_check()

def long_start_delay():
    for i in range(1, 10) [::-1]:
        print(str(i)+'..')
        time.sleep(1)
    lobby_play_check()


def fallback_debug_self_fix():
    global debug_me
    print('')
    time.sleep(1)
    if pyautogui.position() == (0, 0):
        Stop_Bot()
    for i in range(1, 500):
        print('Times debug check and tried to fix: '+str(i))
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#1\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#2\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#3\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(86, 720, (159, 159, 159)) and pyautogui.pixelMatchesColor(44, 722, (164, 164, 163)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#4\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(86, 720, (255, 255, 255)) and pyautogui.pixelMatchesColor(44, 722, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#5\n')
            time.sleep(1)
            lobby_play_check()
        else:
            print('Cant find anything. Looping over again now!')
    print('Tried to fix for 20 seconds and could not fix the issue\n'+
          'Can you please report what happened to Dustyroo? Take screenshots if you can.')
    Stop_Bot()

def test():

    print('Made by: Dustyroo\ndebug current level is '+'~'+str(debug_me)+'~\n\n'+
          'Screen Resolution Choices are:\n1) 1080p\n2) 1440p\n3) 720p'+
          '\n4) Other/ None of the above fit my Screen')
    resolution_choice = input('Please enter your Resolutin Choice: ')
    if resolution_choice == '1':
        print('You have chosen: 1) 1080p\nThere is a 10s delay before starting The Bot'+
              ' \nOpen the game and Wait!')
        long_start_delay()
    elif resolution_choice == '2':
        print('You have chosen: 2) 1440p\nSorry I have not made a support for this resolution.\n'+
              'Please contant dustyroo if you want this resolution implemented!')
        Stop_Bot()
    elif resolution_choice == '3':
        print('You have chosen: 3) 720p\nSorry I have not made a support for this resolution.\n'+
              'Please contant dustyroo if you want this resolution implemented!')
        Stop_Bot()
    elif resolution_choice == '4':
        print('If I do not support your resolution contant dustyroo about it in detail and it will be implemented.')
        Stop_Bot()
    else:
        print('you put '+'~'+resolution_choice+'~'+' this is not one of the options\nPlease try again in:')
        short_count_down()
        clear()
        test()
test()
