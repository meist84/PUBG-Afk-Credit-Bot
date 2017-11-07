import time
import random
import pyautogui

debug_me = 0

def fallback_debug_self_fix():
    if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
        lobby_check() 
    elif pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True: 
        lobby_check()
    else:
        pyautogui.alert(text='You broke it', title='Debug could not fix?', button='OK')

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
        if pyautogui.position() == (0, 0):
            return
        debug_me = 0
        lobby_check()

    if debug_me == 0:
        if pyautogui.pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            pyautogui.moveTo(195, 51)
            time.sleep(1)
            pyautogui.click(77, 715)
            time.sleep(1)
            if pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is True: 
                print('done')
                pyautogui.click(184, 717)
                print('done')
            elif pyautogui.pixelMatchesColor(185, 719, (20, 20, 20)) is not True:
                time.sleep(1)
                #pyautogui.click(195, 51)
                print('wow it worked!')
            else:
                debug_me = 1
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
