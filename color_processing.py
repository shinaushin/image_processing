# color_processing.py
# @author Austin Shin

import numpy as np
import cv2
import leds

def create_hue_mask(image, lower_color, upper_color):
    """
    Applies hue mask to image

    Params:
        image: source img
        lower_color: lower bound of mask
        upper_color: upper bound of mask
    
    Returns:
        masked image
    """
    lower = np.array(lower_color, np.uint8)
    upper = np.array(upper_color, np.uint8)

    mask = cv2.inRange(image, lower, upper)
    output_image = cv2.bitwise_and(image, image, mask = mask)
    return output_image

def color(image, visualize):
    """
    Isolates LEDs in image and finds coordinates

    Params:
        image: source img
        visualize: show img with isolated LEDs
    
    Returns:
        image with isolated LEDs and LED locations
    """
    blur_image = cv2.medianBlur(image, 3)
    hsv_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2HSV)

    lower_red_hue = create_hue_mask(hsv_image, [0, 100, 100], [10, 255, 255])
    higher_red_hue = create_hue_mask(hsv_image, [160, 100, 100], [179, 255, 255])

    full_image = cv2.addWeighted(lower_red_hue, 1.0, higher_red_hue, 1.0, 0.0)

    h,s,v = cv2.split(full_image)

    # cv2.imshow("IMAGE", full_image)
    # cv2.waitKey(0)

    led_img, regions = leds.find_leds(v, image, visualize)
    centers = leds.leds_positions(regions)

    # print("Total number of LEDs: %d" % (len(centers)))

    # cv2.imshow("With LEDs", led_img)
    # cv2.waitKey(0)

    return led_img, regions
