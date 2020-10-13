#! python3
import pyautogui, sys, time
import xlsxwriter
from random import randint

casualDuelButton = ("test", (1, 2))
wait_delay = 1
deck_dic = []




workbook = xlsxwriter.Workbook("DuelLog" + ".xlsx")
worksheet = workbook.add_worksheet()
duels = 10000
i = 1
while i <= duels:
    draw = 0
    deck_dic = [("1" + " zombino"),
                ("2" + " skull_dog"),
                ("3" + " kanna_the_swordmistress"),
                ("4" + " mystical_elf"),
                ("5" + " luster_dragon"),
                ("6" + " trial_of_nightmare"),
                ("7" + " v_tiger_jet"),
                ("8" + " darkfire_soldier_1"),
                ("9" + " divine_dragon_ragnarok"),
                ("10" + " oni_tank_t_34"),
                ("11" + " headless_knight"),
                ("12" + " beaver_warrior"),
                ("13" + " crawling_dragon_2"),
                ("14" + " toon_alligator"),
                ("15" + " flying_kamakiri_2"),
                ("16" + " gazelle_the_king"),
                ("17" + " giant_flea"),
                ("18" + " mystic_horseman"),
                ("19" + " overdrive"),
                ("20" + " ryu_kishin_powered"),
                ]

    print(len(deck_dic))
    worksheet.write(i, 0, i)
    while draw < 4:
        selection = (randint(0, len(deck_dic) - 1))
        print(selection)

        worksheet.write(i, draw + 1, deck_dic[selection])
        deck_dic.remove(deck_dic[selection])
        draw += 1

    i += 1

workbook.close()


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
        col += 1







