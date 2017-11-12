import os
import time
import random
import tkinter
import pyautogui

debug_me = 0
clear = lambda: os.system('cls')
leave_game = 233.0
wait_to_drop = 0.0
grounded_time = 0.0
yn_debug = 2
server_picker = 0, 0


def short_count_down():
    for i in range(1, 6) [::-1]:
        print(str(i)+'..')
        time.sleep(1)

def Stop_Bot():
    print('Stopped THE BOT!')
    time.sleep(1000000)
    Stop_Bot()

def check_if_dead():
    if pyautogui.pixelMatchesColor(1637, 960, (255, 255, 255)) and pyautogui.pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
        time.sleep(0.5)
        pyautogui.click(1710, 951)
        time.sleep(2)
        pyautogui.click(854, 569)
        time.sleep(5)
        fallback_debug_self_fix()
    fallback_debug_self_fix()

def end_game_restart():
    global leave_game
    global grounded_time
    
    print('Bot done Restarting!')
    pyautogui.press('escape')
    time.sleep(3)
    if pyautogui.pixelMatchesColor(875, 591, (255, 255, 255)) and pyautogui.pixelMatchesColor(750, 597, (255, 255, 255)) is True:
        pyautogui.click(841, 572)
        time.sleep(1)
        pyautogui.click()
        time.sleep(5)
        leave_game = 233.0
        grounded_time = 0.0
        fallback_debug_self_fix()
    fallback_debug_self_fix()

def on_land_check():
    global leave_game
    global grounded_time

    if yn_debug == 1:
        print('You have to wait '+str(leave_game)+' Seconds till the bot leaves the game!')
    print('Landed!')
    leave_game -= grounded_time
    if pyautogui.pixelMatchesColor(1805, 889, (17, 48, 62), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (20, 55, 72), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (27, 62, 84), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (23, 58, 78), tolerance=20) is True:
        for i in range(1, round(leave_game)) [::-1]:
            if pyautogui.pixelMatchesColor(1637, 960, (255, 255, 255)) and pyautogui.pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
                check_if_dead()
            if yn_debug == 1:
                print('Time left before restart: '+str(i)+' ')
            pyautogui.keyDown('space')
            time.sleep(0.5)
            pyautogui.keyUp('space')
            time.sleep(0.5)
        end_game_restart()
    else:
        time.sleep(3)
        leave_game -= 3
        pyautogui.press('z')
        for i in range(1, round(leave_game)) [::-1]:
            if pyautogui.pixelMatchesColor(1637, 960, (255, 255, 255)) and pyautogui.pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
                check_if_dead()
            if yn_debug == 1:
                print('Time left before restart: '+str(i)+' ')
            time.sleep(1)
        end_game_restart()
    fallback_debug_self_fix()

def parachute_max_distance():
    global grounded_time

    new_time = 0.0
    for i in range(1, 150):
        new_time += 1.5
        if yn_debug == 1:
            print('Time before you can leave is reduced by: '+str(new_time)+' Seconds.')
        grounded_time += 1.5
        if new_time > 80:
            if pyautogui.pixelMatchesColor(1637, 960, (255, 255, 255)) and pyautogui.pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
                check_if_dead()
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
            print('Check to see if you are in a plane! '+str(i)+' ')
        time.sleep(0.1)
        if pyautogui.pixelMatchesColor(173, 50, (255, 255, 255)) and pyautogui.pixelMatchesColor(167, 47, (255, 255, 255)) is True:
            wait_to_drop = random.randint(1, 32)
            leave_game -= wait_to_drop
            if yn_debug == 1:
                print('You are in the plane.')
            if yn_debug == 1:
                print('the random wait time is '+str(wait_to_drop)+' Seconds.')
            if yn_debug == 1:
                print('You have to wait '+str(leave_game)+' Seconds till the bot leaves the game!')
            time.sleep(23)
            if yn_debug == 1:
                print('Dropping in '+str(wait_to_drop)+' Secconds.')
            time.sleep(wait_to_drop)
            print('Bot made you drop!')
            pyautogui.press('f')
            pyautogui.press('f')
            pyautogui.keyDown('w')
            time.sleep(9)
            pyautogui.keyUp('w')
            pyautogui.press('f')
            pyautogui.press('f')
            if yn_debug == 1:
                print('Bot opened the Parachute!')
            parachute_max_distance()
    if yn_debug == 1:
        print('Never dropped!?')
    fallback_debug_self_fix()

def second_in_game_check():
    for i in range(1, 70):
        if yn_debug == 1:
            print('Times check to see if game started '+str(i)+' seconds')
        time.sleep(1)
        if pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) is not True:
            if pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is not True:
                print('The game has started!')
                playing_game_check()
    if yn_debug == 1:
        print('needed more time to check.')
    fallback_debug_self_fix()

def in_game_check():
    for i in range(1, 60):
        if yn_debug == 1:
            print('Times check to see if you are in game '+str(i)+' Seconds.')
        time.sleep(1)
        if pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) and pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            print('You are in game!')
            second_in_game_check()
    if yn_debug == 1:
        print('Timed out debugging now')
    fallback_debug_self_fix()

def lobby_play_check():
    global debug_me
    global leave_game
    global wait_to_drop

    print('\nDebug level is currently'+'~'+str(debug_me)+'~\n')
    
    if debug_me == 1:
        time.sleep(2)
        fallback_debug_self_fix()
    elif debug_me == 0:
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) and pyautogui.pixelMatchesColor(94, 15, (207, 136, 14)) is True: # Move mouse to play in lobby
            time.sleep(0.1)
            pyautogui.moveTo(195, 51)
            time.sleep(0.5)
            pyautogui.click(86, 203)# clicks na server so rest works
            time.sleep(0.5)
            pyautogui.click(81, 715)# clicks squads
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
            print('Nothing is happening.\n')
        fallback_debug_self_fix()

def start_game_check():
    if pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True:#box is checked and click it then play
        time.sleep(0.5)
        pyautogui.click(184, 717)#clicked the check box
        time.sleep(0.5)
        pyautogui.click(server_picker)# clicks the server you picked
        time.sleep(0.5)
        pyautogui.click(195, 51)#clicked play
        in_game_check()
    elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:#box is not checked and clicked play
        time.sleep(0.5)
        pyautogui.click(server_picker)# clicks the server you picked
        time.sleep(0.5)
        pyautogui.click(195, 51)#clicked play
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
    global leave_game
    print('')
    time.sleep(1)
    if pyautogui.position() == (0, 0):
        Stop_Bot()
    leave_game = 233.0
    for i in range(1, 500):
        time.sleep(0.1)
        if yn_debug == 1:
            print('Times debug check and tried to fix: '+str(i))
        if pyautogui.pixelMatchesColor(892, 591, (255, 255, 255)) and pyautogui.pixelMatchesColor(1005, 584, (48, 48, 48)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#1\n')
            pyautogui.click(892, 591)
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(749, 365, (155, 164, 182)) and pyautogui.pixelMatchesColor(1086, 358, (155, 164, 182)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#2\n')
            pyautogui.click(961, 652)
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(1117, 458, (255, 255, 255)) and pyautogui.pixelMatchesColor(808, 475, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#3\n')
            pyautogui.click(963, 533)
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(1201, 488, (255, 255, 255)) and pyautogui.pixelMatchesColor(961, 510, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#4\n')
            pyautogui.click(1051, 574)
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(892, 591, (255, 182, 0)) and pyautogui.pixelMatchesColor(1005, 584, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#5\n')
            pyautogui.click(892, 591)
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#6\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(963, 363, (155, 164, 182)) and pyautogui.pixelMatchesColor(811, 346, (155, 164, 182)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#7\n')
            pyautogui.click(968, 649)
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#8\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#9\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(86, 720, (159, 159, 159)) and pyautogui.pixelMatchesColor(44, 722, (164, 164, 163)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#10\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(86, 720, (255, 255, 255)) and pyautogui.pixelMatchesColor(44, 722, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#11\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(851, 678, (160, 255, 226)) and pyautogui.pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#12\n')
            time.sleep(1)
            in_game_check()
        elif pyautogui.pixelMatchesColor(173, 50, (255, 255, 255)) and pyautogui.pixelMatchesColor(167, 47, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#13\n')
            print('Timer is probably broken but the bot will keep going and fix it')
            time.sleep(1)
            playing_game_check()
        elif pyautogui.pixelMatchesColor(172, 38, (255, 255, 255)) and pyautogui.pixelMatchesColor(165, 41, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#14\n')
            print('Timer is probably broken but the bot will keep going and fix it')
            time.sleep(1)
            parachute_max_distance()
        elif pyautogui.pixelMatchesColor(1805, 889, (17, 48, 62), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (20, 55, 72), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (27, 62, 84), tolerance=20) is True or pyautogui.pixelMatchesColor(1805, 889, (23, 58, 78), tolerance=20) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#15\n')
            print('Timer is probably broken but the bot will keep going and fix it')
            time.sleep(1)
            on_land_check()
        elif pyautogui.pixelMatchesColor(38, 1032, (206, 204, 199), tolerance=30) and pyautogui.pixelMatchesColor(45, 1002, (248, 248, 248), tolerance=30) is True:
            time.sleep(0.5)
            pyautogui.press('z')
            time.sleep(1)
            if pyautogui.pixelMatchesColor(38, 1032, (206, 204, 199), tolerance=30) is not True:
                if pyautogui.pixelMatchesColor(45, 1002, (248, 248, 248), tolerance=30) is not True:
                    debug_me = 0
                    print('\nFound and Fixed The Issue!#16\n')
                    print('Timer is probably broken but the bot will keep going and fix it')
                    time.sleep(1)
                    on_land_check()
        elif pyautogui.pixelMatchesColor(875, 591, (255, 255, 255)) and pyautogui.pixelMatchesColor(750, 597, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#17\n')
            time.sleep(1)
            end_game_restart()
        elif pyautogui.pixelMatchesColor(1637, 960, (255, 255, 255)) and pyautogui.pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#18\n')
            time.sleep(1)
            check_if_dead()
        elif pyautogui.pixelMatchesColor(840, 345, (155, 164, 182)) and pyautogui.pixelMatchesColor(818, 364, (155, 164, 182)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!#19\n')
            pyautogui.click(960, 646)
            time.sleep(1)
            lobby_play_check()
        else:
            if yn_debug == 1:
                print('Cant find anything. Looping over again now!')
    print('Tried to fix for 1min+ and could not fix the issue\n'+
          'Can you please report what happened to Dustyroo? Take screenshots if you can.')
    Stop_Bot()

def bot_third_start():
    global yn_debug
    print('Do you want all of the constole functions showing(Spaming constole and more lag)\n1) Yes\n2) No(recommended)')
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
        print('You put '+'~'+yn_debug+'~'+' this is not one of the options\nPlease try again in:')
        short_count_down()
        clear()
        bot_third_start()

def bot_second_start():
    global server_picker
    print('What server do you want to be playing in?')
    print('1) NA Servers\n2) EU Servers\n3) AS Servers\n4) KR/JP Servers\n'+
          '5) OC Servers\n6) SA Servers\n7) SEA Servers\n')
    server_picker = input('Please enter your Server Choice: ')
    if server_picker == '1':
        server_picker = 86, 203
        print('You have chosen: NA Servers\n')
        bot_third_start()
    elif server_picker == '2':
        server_picker = 91, 243
        print('You have chosen: EU Servers\n')
        bot_third_start()
    elif server_picker == '3':
        server_picker = 91, 285
        print('You have chosen: AS Servers\n')
        bot_third_start()
    elif server_picker == '4':
        server_picker = 86, 326
        print('You have chosen: KR/JP Servers\n')
        bot_third_start()
    elif server_picker == '5':
        server_picker = 92, 364
        print('You have chosen: OC Servers\n ')
        bot_third_start()
    elif server_picker == '6':
        server_picker = 92, 403
        print('You have chosen: SA Servers\n ')
        bot_third_start()
    elif server_picker == '7':
        server_picker = 95, 444
        print('You have chosen: SEA Servers\n ')
        bot_third_start()
    else:
        print('You put '+'~'+server_picker+'~'+' this is not one of the options\n'+
              'Please try again in:')
        short_count_down()
        clear()
        bot_second_start()

def bot_first_start():
    print('Made by: Dustyroo\nVer. 1.21+\nDebug current level is '+'~'+str(debug_me)+'~\n\n'+
          'Screen Resolution Choices are:\n1) 1080p\n2) 1440p\n3) 720p'+
          '\n4) Other/ None of the above fit my Screen')
    resolution_choice = input('Please enter your Resolutin Choice: ')
    if resolution_choice == '1':
        print('You have chosen: 1080p\n ')
        bot_second_start()
    elif resolution_choice == '2':
        print('You have chosen: 1440p\nSorry I have not made a support for this resolution.\n'+
              'Please contant dustyroo if you want this resolution implemented!')
        Stop_Bot()
    elif resolution_choice == '3':
        print('You have chosen: 720p\nSorry I have not made a support for this resolution.\n'+
              'Please contant dustyroo if you want this resolution implemented!')
        Stop_Bot()
    elif resolution_choice == '4':
        print('If I do not support your resolution contant dustyroo about it in detail and it will be implemented.')
        Stop_Bot()
    else:
        print('You put '+'~'+resolution_choice+'~'+' this is not one of the options\nPlease try again in:')
        short_count_down()
        clear()
        bot_first_start()
bot_first_start()
