import os
import time
import random
import tkinter
import pyautogui

debug_me = 0
clear = lambda: os.system('cls')

def short_count_down():
    for i in range(1, 6) [::-1]:
        print(str(i)+'..')
        time.sleep(1)

def Stop_Bot():
    print('Stopped THE BOT!')
    time.sleep(1000000)
    Stop_Bot()


def lobby_play_check():
    global debug_me
    print('\nDebug level is currently'+'~'+str(debug_me)+'~\n')
    if debug_me == 1:
        time.sleep(2)
        fallback_debug_self_fix()
    elif debug_me == 0:
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            time.sleep(1)
            pyautogui.moveTo(195, 51)
            time.sleep(1)
            pyautogui.click(81, 715)
            time.sleep(1)
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
        time.sleep(1)
        pyautogui.click(184, 717)
        start_game_check()
    elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:
        time.sleep(1)
        #pyautogui.click(195, 51)
        print('wow it worked!')
        time.sleep(1)
        lobby_play_check()
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
    
def debug_level():
    print('Debug Starting in:')
    short_count_down()
    print('')
    print(pyautogui.position())
    print(pyautogui.pixel(185, 719))
    print('black')
    print(pyautogui.pixel(182, 715))
    print('white?')
    if pyautogui.position() == (0, 0):
        Stop_Bot()
    else:
        debug_me = 0
        lobby_play_check()

def fallback_debug_self_fix():
    global debug_me
    print('')
    time.sleep(1)
    for i in range(1, 300):
        print('Times debug check and tried to fix: '+str(i))
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!\n')
            time.sleep(1)
            lobby_play_check()
        elif pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!\n')
            time.sleep(1)
            start_game_check()
        elif pyautogui.pixelMatchesColor(185, 719, (255, 255, 255)) is True:
            debug_me = 0
            print('\nFound and Fixed The Issue!\n')
            time.sleep(1)
            start_game_check()
        else:
            print('Cant find anything. Looping over again now!')
    print('Tried to fix for 20 seconds and could not fix the issue\n'+
    'Can you please report what happened to Dustyroo? Take screenshots if you can.')
    Stop_Bot()
#lobby_play_check()

def test():

    print('Made by: Dustyroo\ndebug current level is '+'~'+str(debug_me)+'~\n\n'+
    'Screen Resolution Choices are:\n1) 1080p\n2) 1440p\n3) 720p'+
    '\n4) Other/ None of the above fit my Screen')
    resolution_choice = input('Please enter your Resolutin Choice: ')
    if resolution_choice == '1':
        print('You have chosen: 1) 1080p\nThere is a 10s delay before starting The Bot'
        + ' \nOpen the game and Wait!')
        long_start_delay()
    elif resolution_choice == '2':
        print('Sorry I have not made a support for this resolution.\n'+
        'Please contant dustyroo if you want this resolution implemented!')
        Stop_Bot()
    elif resolution_choice == '3':
        print('Sorry I have not made a support for this resolution.\n'+
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

