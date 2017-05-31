import time
import random
import pyautogui

pyautogui.FAILSAFE = True #Para el programa si mueves el ratón a la esquina de arriba a la izquierda
arrows = ['left','right','up','down']
options = ['backspace','enter']
actions = ['Z','X']

#Probabilidades de pulsar cada tipo de botón
arr_prob = 0.6
act_prob = 0.3
opt_prob = 0.1

print('Tienes 3 segundos...')
time.sleep(3)

pyautogui.keyDown('space') #Aprieta espacio
t_end = time.time() + 300
while time.time() < t_end:
    r = random.uniform(0,1)
    if r <= arr_prob:
        rand_num = random.randint(0,len(arrows)-1)
        pyautogui.press(arrows[rand_num])
        print(arrows[rand_num])
    elif r <= (arr_prob + act_prob):
        rand_num = random.randint(0,len(actions)-1)
        pyautogui.press(actions[rand_num])
        print(actions[rand_num])
    elif r <= (arr_prob + act_prob + opt_prob):
        rand_num = random.randint(0,len(options)-1)
        pyautogui.press(options[rand_num])
        print(options[rand_num])
    time.sleep(2)
pyautogui.keyUp('space') #Suelta espacio
