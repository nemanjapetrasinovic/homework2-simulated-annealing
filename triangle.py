import random


class Triangle:
    def __init__(self, imageWidth, imageHeight):
        self.pt1 = (random.randint(0, imageWidth - 1), random.randint(0, imageHeight - 1))
        self.pt2 = (random.randint(0, imageWidth - 1), random.randint(0, imageHeight - 1))
        self.pt3 = (random.randint(0, imageWidth - 1), random.randint(0, imageHeight - 1))

        self.rgbaColor = [random.randint(0, 255), random.randint(0, 255),
                     random.randint(0, 255), random.uniform(0.1, 0.9)]

    def setRandomVertexes(self, imageWidth, imageHeight):
        self.pt1 = (random.randint(0, imageWidth - 1), random.randint(0, imageHeight - 1))
        self.pt2 = (random.randint(0, imageWidth - 1), random.randint(0, imageHeight - 1))
        self.pt3 = (random.randint(0, imageWidth - 1), random.randint(0, imageHeight - 1))


class TriangleArray:
    def __init__(self):
        self.triangles = []
        self.count = 0
        self.inuse = 0
