import os
import time
import pyautogui as gui
print("Strawberry Ultimate Blooket Bot")
gameid = input("Enter your game ID:\n")
url = ("https://play.blooket.com/play?id=%s" % gameid)
path = input("Enter the path to the exe of your browser:\n")
browse_path = path + ' %s'
input("Enter to flood")
count = 0
def flood():
    global count
    name = input("What do you want the bot name to be?\n")
    os.system("start " + '"' + browse_path + '"' + " " + url)
    time.sleep(3)
    gui.typewrite(f"{name}%d" % count)
    gui.press("Enter")
    count = count + 1
    flood()

flood()