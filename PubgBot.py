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
yn_debug = int

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
    print('Landed!')
    if yn_debug == 1:
        print(leave_game)
    leave_game -= grounded_time
    if yn_debug == 1:
        print(leave_game)
    if yn_debug == 1:
        print(grounded_time)
    if pyautogui.pixelMatchesColor(1805, 889, (17, 48, 62), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (20, 55, 72), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (27, 62, 84), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (23, 58, 78), tolerance=20) is True:
        for i in range(1, leave_game) [::-1]:
            if yn_debug == 1:
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
            if yn_debug == 1:
                print('Time left before restart:'+str(i)+'')
            time.sleep(1)
        pyautogui.press('escape')
        end_game_restart()

def parachute_max_distance():
    global grounded_time
    print('Waiting till you land on ground')
    for i in range(1, 150) :
        if yn_debug == 1:
            print('Time before you can leave is now less by:'+str(i)+'')
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
    for i in range(1, 1000):
        if yn_debug == 1:
            print('Check to see if you are in a plane! '+str(i)+'')
        if pyautogui.pixelMatchesColor(173, 50, (255, 255, 255)) and pyautogui.pixelMatchesColor(167, 47, (255, 255, 255)) is True:
            wait_to_drop = random.randint(1, 32)
            leave_game = 265 - wait_to_drop
            leave_game -= 24
            if yn_debug == 1:
                print('the random wait time is'+str(wait_to_drop)+' Seconds')
            if yn_debug == 1:
                print('You have to wait'+str(leave_game)+' Seconds till you leave the game!')
            if yn_debug == 1:
                print('you are flying')
            time.sleep(23)
            if yn_debug == 1:
                print('Dropping in a few secconds')
            time.sleep(wait_to_drop)
            pyautogui.press('f')
            time.sleep(9)
            pyautogui.press('f')
            print('You have dropped')
            parachute_max_distance()
    print('can you drop!?')
    fallback_debug_self_fix()

def second_in_game_check():
    for i in range(1, 80):
        if yn_debug == 1:
            print('Times check to see if game started '+str(i)+'seconds')
        time.sleep(1)
        if pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) is not True:
            if pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is not True:
                print('The game has started!')
                playing_game_check()
    if yn_debug == 1:
            print('needed more time to check')
    fallback_debug_self_fix()

def in_game_check():
    for i in range(1, 80):
        if yn_debug == 1:
            print('Times check to see if you are in game '+str(i)+'seconds')
        time.sleep(1)
        if pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) and pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            print('You are in game!')
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
        if yn_debug == 1:
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
        print('Starting Game!')
        time.sleep(0.5)
        in_game_check()
    else:
        time.sleep(1)
        if yn_debug == 1:
            print('Nothing worked trying to debug now!')
        debug_me = 1
        fallback_debug_self_fix()

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
        time.sleep(0.1)
        if yn_debug == 1:
            print('Times debug check and tried to fix: '+str(i))
        if pyautogui.pixelMatchesColor(892, 591, (255, 255, 255)) and pyautogui.pixelMatchesColor(1005, 584, (48, 48, 48)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#1\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(892, 591, (255, 182, 0)) and pyautogui.pixelMatchesColor(1005, 584, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#2\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#3\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#4\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#5\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(86, 720, (159, 159, 159)) and pyautogui.pixelMatchesColor(44, 722, (164, 164, 163)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#6\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(86, 720, (255, 255, 255)) and pyautogui.pixelMatchesColor(44, 722, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#7\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) and pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#8\n')
            time.sleep(1)
            in_game_check()
        elif pyautogui.pixelMatchesColor(173, 50, (255, 255, 255)) and pyautogui.pixelMatchesColor(167, 47, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#9\n')
            print('Timer is probably broken but the bot will keep going and fix it')
            time.sleep(1)
            playing_game_check()
        elif pyautogui.pixelMatchesColor(172, 38, (255, 255, 255)) and pyautogui.pixelMatchesColor(172, 53, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#10\n')
            print('Timer is probably broken but the bot will keep going and fix it')
            time.sleep(1)
            parachute_max_distance()
        elif pyautogui.pixelMatchesColor(1805, 889, (17, 48, 62), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (20, 55, 72), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (27, 62, 84), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (23, 58, 78), tolerance=20) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#11\n')
            print('Timer is probably broken but the bot will keep going and fix it')
            time.sleep(1)
            on_land_check()
        elif pyautogui.pixelMatchesColor(38, 1032, (206, 204, 199), tolerance=30) and pyautogui.pixelMatchesColor(45, 1002, (248, 248, 248), tolerance=30) is True:
            print('Check Worked!')
            time.sleep(0.5)
            pyautogui.press('z')
            time.sleep(1)
            if pyautogui.pixelMatchesColor(38, 1032, (206, 204, 199), tolerance=30) is not True:
                if pyautogui.pixelMatchesColor(45, 1002, (248, 248, 248), tolerance=30) is not True:
                    debug_me = 0
                    print('\nFound and Fixed The Issue!#12\n')
                    print('Timer is probably broken but the bot will keep going and fix it')
                    time.sleep(1)
                    on_land_check()
        else:
            if yn_debug == 1:
                print('Cant find anything. Looping over again now!')
    print('Tried to fix for 1min+ and could not fix the issue\n'+
          'Can you please report what happened to Dustyroo? Take screenshots if you can.')
    Stop_Bot()

def bot_second_start():
    global yn_debug
    print('Do you want all of the constole functions showing(Spam)\n1) Yes\n2) No(recommended)')
    yn_debug = input('Please enter your Constole Choice: ')
    if yn_debug == '1':
        yn_debug = 1
        print('There is a 10s delay before starting The Bot'+' \nOpen the game and Wait!\nBot Starting in:')
        long_start_delay()
    elif yn_debug == '2':
        yn_debug = 2
        print('There is a 10s delay before starting The Bot'+' \nOpen the game and Wait!\nBot Starting in:')
        long_start_delay()
    else:
        print('you put '+'~'+yn_debug+'~'+' this is not one of the options\nPlease try again in:')
        short_count_down()
        clear()
        bot_second_start()

def bot_first_start():

    print('Made by: Dustyroo\ndebug current level is '+'~'+str(debug_me)+'~\n\n'+
          'Screen Resolution Choices are:\n1) 1080p\n2) 1440p\n3) 720p'+
          '\n4) Other/ None of the above fit my Screen')
    resolution_choice = input('Please enter your Resolutin Choice: ')
    if resolution_choice == '1':
        print('You have chosen: 1) 1080p\n ')
        bot_second_start()
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
        bot_first_start()
bot_first_start()
