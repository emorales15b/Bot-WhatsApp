import pyautogui
import webbrowser as web
from time import sleep


web.open("https://web.whatsapp.com/send?phone=+523111620975")
sleep(15)

"""
with open("extasis.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
"""
for i in range(10):
    pyautogui.typewrite("Hola Nachin! \nInvita los tacos prro")
    pyautogui.press("enter")