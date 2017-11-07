import random
import time
import pyautogui

debug_me = 0

def lobby_check():
    global debug_me

    if debug_me == 1:
        for i in list(range(4)) [::-1]:
            print(i+i)
            time.sleep(1)
        print(pyautogui.position())
        print(pyautogui.pixel(185, 719)) 
        print('black')
        print(pyautogui.pixel(182, 715)) 
        print('white?')
        if pyautogui.position() == (0,0):
            return
        debug_me = 0
        lobby_check()
    if debug_me == 0:
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) == True:
            pyautogui.moveTo(195, 51)
            time.sleep(1)
            pyautogui.click(77, 715)
            time.sleep(1)
            if pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) == True: 
                pyautogui.click(184, 717)
                lobby_check()
            else:
                time.sleep(1)
                #pyautogui.click(195, 51)
                print('wow it worked!')
                lobby_check()
        else:
            debug_me = 1
            print('trying to find pixel')
            print(debug_me)
            lobby_check()
    else:
        print('Nothing is happening')
        lobby_check()
lobby_check()