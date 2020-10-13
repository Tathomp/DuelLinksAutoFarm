#! python3
# Auto connects to casual duels in duel links, waits for the time to run out and reconnects to a new duel
# This is mainly so that the player can afk farm XP and rewards from casual matches.
import pyautogui, sys, time

casualDuelButton = ("test", (1, 2))
wait_delay = 1
card_pos = ((808, 954), (864, 944), (941, 940), (1022, 937))



duel_count = 0
while True:
    duel_count += 1
    print("Starting duel numer: ", duel_count)
    while True:
        if pyautogui.locateCenterOnScreen("duelbutton.PNG", confidence=0.8) is not None:
            x, y = pyautogui.locateCenterOnScreen("duelbutton.PNG", confidence=0.8)
            pyautogui.click(x, y)
            break


        time.sleep(wait_delay)

    # while pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8) is None:


    while True:
        if pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8) is not None:
            x, y = pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8)
            pyautogui.click(x, y)
            break

        time.sleep(15)


    while True:
        if pyautogui.locateCenterOnScreen("nextbutton.PNG", confidence=0.8) is not None:
            x, y = pyautogui.locateCenterOnScreen("nextbutton.PNG", confidence=0.8)
            pyautogui.click(x, y)
        elif pyautogui.locateCenterOnScreen("duelbutton.PNG", confidence=0.8) is not None:
            break
        time.sleep(wait_delay)


