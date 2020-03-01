# gray_processing.py
# @author Austin Shin

import sys
import leds
import cv2

def extract_bright(grey_img):
    """
    Thresholds image based on brightness

    Params:
        grey_img: grayscale image

    Returns:
        thresholded image
    """
    [minVal, maxVal, minLoc, maxLoc] = cv2.minMaxLoc(grey_img)
    margin = 0.8

    thresh = int(maxVal*margin)

    ret, thresh_img = cv2.threshold(grey_img, thresh, 255, cv2.THRESH_BINARY)
    return thresh_img

def gray(img, visualize):
    """
    Converts image to grayscale and finds red LEDs based on brightness and color

    Params:
        img: source image
        visualize: boolean option for visualization 

    Returns:
        image with LEDs extracted and LED locations
    """
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh_img = extract_bright(grey_img)

    led_img, regions = leds.find_leds(thresh_img, img, visualize)
    centers = leds.leds_positions(regions)

    # print("Total number of LEDs : %d" % (len(centers)))
    # print("LED positions :")
    # for c in centers:
        # print "x : %d; y : %d" % (c[0], c[1])

    # cv2.imshow("With LEDs", led_img)
    # cv2.waitKey(0)

    return led_img, centers
