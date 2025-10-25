import time
import keyboard
import mouse
import json

with open('actionList.json', 'r') as file:
    keystrokes = json.load(file)

input("Hover over blender and prepear to be blasted away ;))\nenter to start XDD\nalso hold q to stop ;DD")
for keystroke in keystrokes['allOfThingies']:
    if (keyboard.is_pressed('q')): break
    match keystroke[0]:
        case 0:
            keyboard.press_and_release(keystroke[1])
        case 1:
            keyboard.write(keystroke[1], float(keystroke[2]))
        case 2:
            mouse.click('left')
        case 3:
            mouse.click('right')
        case 4:
            for char in str(keystroke[1]):
                if (keyboard.is_pressed('q')): break
                match char:
                    case ' ':
                        keyboard.press_and_release("enter")
                    case '.':
                        keyboard.press_and_release("dot")
                    case '(':
                        keyboard.press("shift")
                        keyboard.press_and_release("9")
                        keyboard.release("shift")
                    case 'T':
                        keyboard.press("shift")
                        keyboard.press_and_release("t")
                        keyboard.release("shift")
                    case '_':
                        keyboard.press("shift")
                        keyboard.press_and_release("underscore")
                        keyboard.release("shift")
                    case ')':
                        keyboard.press("shift")
                        keyboard.press_and_release("0")
                        keyboard.release("shift")
                    case '_':
                        keyboard.press("shift")
                        keyboard.press_and_release("-")
                        keyboard.release("shift")
                    case _:
                        keyboard.press_and_release(char)
                time.sleep(0.05)
        case 5:
            mouse.move(keystroke[1],keystroke[2], absolute = keystroke[3])
    time.sleep(0.05)