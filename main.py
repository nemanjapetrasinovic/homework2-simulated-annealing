import numpy as np
import cv2
import imgLib

image = cv2.imread("C:\Users\Nemanja Petrasinovic\Desktop\Images\/test3.png")
height, width, chanel = image.shape

image2 = np.ones((height, width, 3), np.uint8) * 255

cv2.imshow("image", image)
cv2.imshow("image2", image2)
cv2.waitKey(1)

temperature = 1000
currentState = image2
currentEnergy = imgLib.calculateDifference(image, image2, width, height)

while 1:
    #temperature = temperature - 1
    #if temperature == 0:
       #break

    newState = imgLib.drawTriangle(currentState)
    newEnergy = imgLib.calculateDifference(image, newState, width, height)

    if(newEnergy < currentEnergy):
        currentState = newState
        currentEnergy = newEnergy

    cv2.imshow("image", image)
    cv2.imshow("image2", currentState)
    cv2.waitKey(1)
