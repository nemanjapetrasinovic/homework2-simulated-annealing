import math
import numpy as np
import random
import cv2
import gmpy2

def calculateDifference(imageA, imageB, width, height):
    d = 0
    vectorA = cv2.reduce(imageA, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)
    vectorB = cv2.reduce(imageB, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)

    for i in range(len(vectorA[0])):
        pixelA = vectorA[0][i]
        pixelB = vectorB[0][i]

        db = pixelA[0] - pixelB[0]
        dg = pixelA[1] - pixelB[1]
        dr = pixelA[2] - pixelB[2]

        d = d + gmpy2.isqrt(dr*dr+dg*dg+db*db)
    return d


def drawTriangle(image):
    height, width, chanel = image.shape
    overlay = image.copy()
    newImage = image.copy()

    pt1 = (random.randint(0, width - 1), random.randint(0, height - 1))
    pt2 = (random.randint(0, width - 1), random.randint(0, height - 1))
    pt3 = (random.randint(0, width - 1), random.randint(0, height - 1))

    triangle_cnt = np.array([pt1, pt2, pt3])
    cv2.drawContours(overlay, [triangle_cnt], 0,\
    ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))), -1)

    opacity = random.uniform(0.1, 1)
    cv2.addWeighted(overlay, opacity, newImage, 1 - opacity, 0, newImage)

    return newImage

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x