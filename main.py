import datetime
import pyautogui
import numpy as np

x_start = 740
dx = 80
y_low_start = 440
dy_low = -30
dy_high = -30

# defining check points for pixel control
low_check_points = [(int(x), int(y))
                    for y in np.linspace(y_low_start, y_low_start + dy_low, 1, endpoint=True)
                    for x in np.linspace(x_start, x_start + dx, 8, endpoint=True)]
high_check_points = [(int(x), int(y))
                     for y in np.linspace(y_low_start + dy_low, y_low_start + dy_low + dy_high, 1, endpoint=True)
                     for x in np.linspace(x_start, x_start + dx, 8, endpoint=True)]

bg_color = (247, 247, 247)

while True:
    timer_start = datetime.datetime.now()

    # checking check points for air and ground obstacles
    area_low_checks = [pyautogui.pixelMatchesColor(*cor, bg_color, tolerance=10) for cor in low_check_points]
    area_high_checks = [pyautogui.pixelMatchesColor(*cor, bg_color, tolerance=10) for cor in high_check_points]

    is_low_safe = all(area_low_checks)
    is_high_safe = all(area_high_checks)

    if not is_low_safe:
        pyautogui.press('up')

    if not is_high_safe:
        pyautogui.press('down')

    timer_end = datetime.datetime.now()
    # passed time for each loop
    print(timer_end - timer_start)