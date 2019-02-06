import cv2

def leds_positions(regions):
    centers = []
    for x,y,width,height in regions:
        centers.append([x+(width/2),y+(height/2)])

    return centers

def find_leds(thresh_img, img, visualize):
    print(visualize)
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regions = []
    for contour in contours:
        x = []
        y = []
        for i in range(len(contour)):
            x.append(contour[i][0][0])
            y.append(contour[i][0][1])
        min_x, min_y = min(x), min(y)
        # print(min_x, min_y)
        width, height = max(x) - min_x + 1, max(y) - min_y + 1
        regions.append((min_x, min_y, width, height))

    if visualize:
        for x,y,width,height in regions:
            pt1 = x,y
            pt2 = x+width, y+height
            color = (0,0,255,0)
            cv2.rectangle(img, pt1, pt2, color, 2)

    return img, regions
