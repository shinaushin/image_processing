# detect_overlap.py
# @author Austin Shin

import cv2
import gray_processing
import color_processing
import numpy as np
import sys

image = sys.argv[1] # path of image
visualize = int(sys.argv[2]) # boolean option for visualization

im = cv2.imread(image)
led_color, regions = color_processing.color(im, visualize)

mask = np.zeros(im.shape, np.uint8)
for region in regions:
    x = region[0]
    y = region[1]
    w = region[2]
    h = region[3]
    mask[y:y+h, x:x+w] = im[y:y+h, x:x+w]

# cv2.imshow("Blacked Out", mask)
# cv2.waitKey(0)

final_leds, regions = gray_processing.gray(mask, visualize)

for x,y,width,height in regions:
    pt1 = x,y
    pt2 = x+width, y+height
    color = (0,0,255,0)
    cv2.rectangle(im, pt1, pt2, color, 2) 

print("Total number of LEDs : %d" % (len(regions)))
# still detects extra LEDs, can filter out by size or
# by first detecting where robot is

im = cv2.resize(im, (640, 480))
cv2.imshow("Final LED locations", im)
cv2.waitKey(0)
