#! python3
import pyautogui, sys, time
import xlsxwriter

casualDuelButton = ("test", (1, 2))
wait_delay = 1
card_pos = ((808, 954), (864, 944), (941, 940), (1022, 937))


deck_dic = (("1", "zombino"),
            ("2", "skull_dog"),
            ("3", "kanna_the_swordmistress"),
            ("4", "mystical_elf"),
            ("5", "luster_dragon"),
            ("6", "trial_of_nightmare"),
            ("7", "v_tiger_jet"),
            ("8", "darkfire_soldier_1"),
            ("9", "divine_dragon_ragnarok"),
            ("10", "oni_tank_t_34"),
            ("11", "headless_knight"),
            ("12", "beaver_warrior"),
            ("13", "crawling_dragon_2"),
            ("14", "toon_alligator"),
            ("15", "flying_kamakiri_2"),
            ("16", "gazelle_the_king"),
            ("17", "giant_flea"),
            ("18", "mystic_horseman"),
            ("19", "overdrive"),
            ("20", "ryu_kishin_powered"),
            )

def safety_catches():
    if pyautogui.locateCenterOnScreen("duelmenubutton.PNG") is not None:
        x, y = pyautogui.locateCenterOnScreen("duelmenubutton.PNG")
        pyautogui.click(x, y)

    if pyautogui.locateCenterOnScreen("nextbutton.PNG") is not None:
        x, y = pyautogui.locateCenterOnScreen("nextbutton.PNG")
        pyautogui.click(x, y)

    if pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8) is not None:
        x, y = pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8)
        pyautogui.click(x, y)



def record_duel(duel_num, ws):

    hand = list()
    for card in card_pos:
        pyautogui.click(card)
        for slots in deck_dic:
            if pyautogui.locateCenterOnScreen(slots[1] + ".PNG", confidence=0.8, region=(162, 123, 459, 252)) is not None:
                hand.append(slots)
                print("Found: ", slots[1])
                time.sleep(.5)
                break

        # register what card is used
    print(hand)
    col = 0
    ws.write(duel_num, col, duel_num)

    for card in hand:
        ws.write(duel_num, col+1, card[0] + " " + card[1])
        col += 1




curr_batch = 0
batch_num = 2
batch_size = 3

while curr_batch <= batch_num:
    i = 0
    workbook = xlsxwriter.Workbook("DuelLog" + str(curr_batch) + ".xlsx")
    worksheet = workbook.add_worksheet()
    while i <= batch_size:

        print("Duel: ", i)
        x, y = 0,0
        while True:
            if pyautogui.locateCenterOnScreen("duelbutton.PNG", confidence=0.8) is not None:
                x, y = pyautogui.locateCenterOnScreen("duelbutton.PNG", confidence=0.8)
                pyautogui.click(x, y)
                break
            #else:
               # safety_catches()

            print("Delay: looking for start duel button.")
            time.sleep(wait_delay)

        while True:
            if pyautogui.locateCenterOnScreen("duelmenubutton.PNG") is not None:
                x, y = pyautogui.locateCenterOnScreen("duelmenubutton.PNG")
                record_duel(i, worksheet)
                pyautogui.click(x, y)
                break
           # else:
             #   safety_catches()
            print("Delay: Looking for in duel menu button")
            time.sleep(wait_delay)

        # Click on cards, register their order and all that

        while True:
            if pyautogui.locateCenterOnScreen("surrender.PNG", confidence=0.8) is not None:
                x, y = pyautogui.locateCenterOnScreen("surrender.PNG", confidence=0.8)
                break
            #else:
            #    safety_catches()
            print("Delay: Looking for surrender button")
            time.sleep(wait_delay)

        pyautogui.click(x, y)

        while True:
            if pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8) is not None:
                x, y = pyautogui.locateCenterOnScreen("okgameover.PNG", confidence=0.8)
                break
           # else:
            #    safety_catches()
            print("Delay: Looking for surrender button\n")
            time.sleep(wait_delay)

        pyautogui.click(x, y)

        i += 1

    curr_batch += 1
    workbook.close()



