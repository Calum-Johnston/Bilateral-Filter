#####################################################################

# A2 : displaying an image from file (and applying Bilateral filter to it)

# Author : Calum Johnston, calum.p.johnston@durham.ac.uk

#####################################################################

import numpy as np
import cv2

#####################################################################

# define display window name

windowName = "Bilateral Image"; # window name

# read an image from the specified file (in colour)

img = cv2.imread('./test2.png', cv2.IMREAD_COLOR);

# check it has loaded
    
if not img is None:

    # performing smoothing on the image using a 5x5 smoothing mark (see manual entry for GaussianBlur())

    blur = cv2.bilateralFilter(img, 15, 200, 20)

    # display this blurred image in a named window

    cv2.imwrite("test2_bilateral2080.png", blur)
    cv2.imshow(windowName, blur);

    # start the event loop - essential

    # cv2.waitKey() is a keyboard binding function (argument is the time in milliseconds).
    # It waits for specified milliseconds for any keyboard event.
    # If you press any key in that time, the program continues.
    # If 0 is passed, it waits indefinitely for a key stroke.

    key = cv2.waitKey(0); # wait

    # It can also be set to detect specific key strokes by recording which key is pressed

    # e.g. if user presses "x" then exit and close all windows

    if (key == ord('x')):
        cv2.destroyAllWindows();
else:
    print("No image file successfully loaded.");

#####################################################################


