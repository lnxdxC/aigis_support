#!/usr/bin/env python
"""
Script to copy the image coordinates (pixel) into the clipboard. \n
Left mouse click copies and puts text with the image coordinates. Left click puts color (RGB) on the image. \n
__author__ = "Daniel Schneider"
__copyright__ = "Copyright 2022, AVL"
__credits__ = "Daniel Schneider"
__license__ = "Confidential"
__version__ = "1.0.0"
__maintainer__ = "Daniel Schneider"
__email__ = "daniel.schneider@avl.com"
__status__ = "Develop"
"""

import cv2
import pyperclip


def click_event(event, x, y, flags, params):
    # Checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        string = str(x) + ', ' + str(y)
        pyperclip.copy(string)
        print(string)

        # Put the coordinates
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)

        cv2.imshow('image', img)

    # Checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        string = str(x) + ', ' + str(y)
        pyperclip.copy(string)
        print(string)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 1,
                    (255, 255, 0), 2)

        cv2.imshow('image', img)


if __name__ == "__main__":
    img = cv2.imread(r"./herold.png", 1)

    cv2.imshow('image', img)

    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
