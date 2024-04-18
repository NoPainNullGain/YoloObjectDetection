import pyautogui
import time

KEY_JUMP = 'space'
KEY_FORWARD = 'w'
KEY_STRAFE_LEFT = 'a'
KEY_STRAFE_RIGHT = 'd'
KEY_SHEATHE_WEAPON = 'tab'

def forward_start():
    pyautogui.keyDown(KEY_FORWARD)

def forward_stop():
    pyautogui.keyUp(KEY_FORWARD)

def strafe_left_start():
    pyautogui.keyDown(KEY_STRAFE_LEFT)

def strafe_left_stop():
    pyautogui.keyUp(KEY_STRAFE_LEFT)

def strafe_right_start():
    pyautogui.keyDown(KEY_STRAFE_RIGHT)

def strafe_right_stop():
    pyautogui.keyUp(KEY_STRAFE_RIGHT)

def jump():
    pyautogui.press(KEY_JUMP)

if __name__ == "__main__":
    time.sleep(10)
    while True:

        jump()