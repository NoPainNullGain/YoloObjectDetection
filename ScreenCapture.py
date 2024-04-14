import time

from mss import mss
import cv2 as cv
import numpy as np

prev_time = 0
fps_display_delay = 0
fps_delayed = 0
fps_list = [0.0] * 10

with mss() as sct:
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    monitor = {'mon': monitor_number, 'top': mon['top']+140, 'left': mon['left']+5, 'width': 900, 'height': 600}

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

        #draw the fps on image
        cv.putText(img, f'FPS: {fps_delayed: .0f}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv.imshow('screen capture', img)

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break
