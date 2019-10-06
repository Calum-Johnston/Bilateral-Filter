import numpy as np
import cv2
import math
import png

def getDistance(x, y, a, b):
    return math.sqrt((x - a) ** 2 + (y - b) ** 2)

def applyGaussianFunction(x, sigma):
    return 1/(math.sqrt(2*math.pi)*sigma)*math.e**(-0.5*(x/sigma)**2)

def calculateSumOfRGB(lst):
    return sum(lst)

def applyIndividualFilter(original_Image, flash_Image, a, b, diameter, sigma_a, sigma_b):
    radius = int(diameter / 2)
    pixel_Filtered = 0
    Wp = 0
     
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            x_Coordinate = a - x
            y_Coordinate = b - y
            if not((x_Coordinate >= len(original_Image)) or (x_Coordinate <  0) or (y_Coordinate >= len(original_Image[0])) or (y_Coordinate < 0)):
                fr = applyGaussianFunction(calculateSumOfRGB(flash_Image[x_Coordinate][y_Coordinate]) - calculateSumOfRGB(flash_Image[a][b]), sigma_a)
                gs = applyGaussianFunction(getDistance(x_Coordinate, y_Coordinate, a, b), sigma_b)
                w = (fr * gs)
                value = w * original_Image[x_Coordinate][y_Coordinate]
                pixel_Filtered += value
                Wp += w
    pixel_Filtered = pixel_Filtered / Wp
    return pixel_Filtered
    
def applyBilateralFilter(original_Image, flash_Image, diameter, sigma_x, sigma_y):
    new_Image = np.zeros(original_Image.shape, dtype="uint8")
    for x in range(0, len(original_Image)):
        for y in range(0, len(original_Image[0])):
            pixelValues = applyIndividualFilter(original_Image, flash_Image, x, y, diameter, sigma_x, sigma_y)
            new_Image[x][y][0] = int(round(pixelValues[0]))
            new_Image[x][y][1] = int(round(pixelValues[1]))
            new_Image[x][y][2] = int(round(pixelValues[2]))
    return new_Image

def loadImage(): 
    original_Image = cv2.imread('./test3a.jpg', cv2.IMREAD_COLOR);
    flash_Image = cv2.imread('./test3b.jpg', cv2.IMREAD_COLOR);
    if not original_Image is None:
        filtered_Image = applyBilateralFilter(original_Image, flash_Image, 15, 80, 16)
        cv2.imwrite("test3_bilateral8016.jpg", filtered_Image)
        cv2.imshow("Bilateral Image", filtered_Image);
        key = cv2.waitKey(0); # wait
        if (key == ord('x')):
            cv2.destroyAllWindows();
    else:
        print("No image file successfully loaded.");


loadImage()




