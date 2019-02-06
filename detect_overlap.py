import cv2
import gray_processing
import color_processing
import numpy as np
import sys

visualize = int(sys.argv[1])

image = "../darknet/data/HopkinsAIBig/123245088834.jpg"
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

cv2.imshow("Final LED locations", im)
cv2.waitKey(0)

