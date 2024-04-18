import multiprocessing.process
import time

from mss import mss
import cv2 as cv
import numpy as np
import win32gui, win32ui, win32con
import multiprocessing

class ScreenCaptureAgent:

    w = 0
    h = 0
    hwnd = None
    enable_cv_preview = None

    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        self.enable_cv_preview = True
        self.capture_process = None

    def capture_screen(self, w, h):

        prev_time = 0
        fps_display_delay = 0
        fps_delayed = 0
        fps_list = [0.0] * 10

        with mss() as sct:
            monitor_number = 1
            mon = sct.monitors[monitor_number]

            monitor = {'mon': monitor_number, 'top': mon['top']+25, 'left': mon['left'], 'width': w, 'height': h}

            while True:
                img = np.asarray(sct.grab(monitor))

                # calculate the fps
                curr_time = time.perf_counter()
                fps = 1 / (curr_time - prev_time)
                prev_time = curr_time

                fps_list.append(fps)
                fps_list.pop(0)

                avg_fps = sum(fps_list) / len(fps_list)

                fps_display_delay += 1

                if fps_display_delay >= 3:
                    fps_delayed = avg_fps
                    fps_display_delay = 0

                if self.enable_cv_preview:
                    #draw fps and resize image
                    small_img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
                    cv.putText(small_img, f'FPS: {fps_delayed: .0f}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.putText(small_img, f'width {w: }', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.putText(small_img, f'height {h: }', (10, 110), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.imshow('screen capture', small_img)

                if cv.waitKey(1) & 0xFF == ord("q"):
                    cv.destroyAllWindows()
                    break

    def get_window_size(self):
        return (self.w, self.h)

if __name__ == "__main__":
    window_name = "BLACK DESERT - 466087"

    screen_agent = ScreenCaptureAgent(window_name)

    if screen_agent.capture_process is None:

        screen_agent.capture_process = multiprocessing.Process(
        target= screen_agent.capture_screen,
        args=(screen_agent.w, screen_agent.h),
        name="screen capture process"
        )

        screen_agent.capture_process.start()