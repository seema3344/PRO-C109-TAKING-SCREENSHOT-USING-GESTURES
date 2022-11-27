import numpy as np
import pyautogui
import cv2
import imutils
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)

pyautogui.screenshot("straight_to_disk.png")

image = cv2.imwrite("straight_to_disk.png")
cv2.imshow("Screenshot",imutils.resize(image, width=600))
