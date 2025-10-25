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
            keyboard.press_and_release(keystroke[2])
        case 1:
            print(keystroke[2])
            keyboard.write(keystroke[2], float(keystroke[3]))
        case 2:
            mouse.click('left')
        case 3:
            mouse.click('right')
        case 4:
            for char in str(keystroke[2]):
                if (keyboard.is_pressed('q')): break
                match char:
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
                        keyboard.press_and_release("-")
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
                time.sleep(float(keystroke[3]))
        case 5:
            mouse.move(keystroke[2],keystroke[3], absolute = keystroke[4])
    time.sleep(float(keystroke[1]))