import os
import time
import threading
import pyautogui as py
import keyboard

def take_screenshot(directory, interval):
    while True:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(directory, f"screenshot_{timestamp}.png")
        py.screenshot().save(screenshot_path)
        time.sleep(interval)

def main():
    interval = int(input("Enter interval between screenshots in seconds: "))
    directory = "screenshots"
    if not os.path.exists(directory):
        os.makedirs(directory)

    print(f"Taking screenshots every {interval} seconds. Press 'q' to quit.")

    screenshot_thread = threading.Thread(target=take_screenshot, args=(directory, interval))
    screenshot_thread.start()

    try:
        while True:
            if keyboard.is_pressed("q"):
                break
    except KeyboardInterrupt:
        pass
    finally:
        screenshot_thread.join()
        print("Program ended.")

if __name__ == "__main__":
    main()
