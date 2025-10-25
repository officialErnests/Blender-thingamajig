import time
import keyboard
import mouse
import json

with open('actionList.json', 'r') as file:
    keystrokes = json.load(file)

input("Hover over blender and prepear to be blasted away ;))\nenter to start XDD\nalso hold q to stop ;DD")
for keystroke in keystrokes['allOfThingies']:
    if (keyboard.is_pressed('q')):
        break
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
                if (char == '(' or
                    char == ')' or 
                    char == '_'):
                    keyboard.press_and_release("shift+"+char)
                else:
                    keyboard.press_and_release(char)
                time.sleep(float(keystroke[3]))
        case 5:
            mouse.move(keystroke[2],keystroke[3], absolute = keystroke[4])
    time.sleep(float(keystroke[1]))