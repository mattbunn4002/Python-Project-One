import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:
    def __init__(self, xLower, xUpper, yLower, yUpper, maxIter=500, sampleSize=1000, complexSeed=0):
        self.xLower = xLower
        self.xUpper = xUpper
        self.yLower = yLower
        self.yUpper = yUpper
        self.maxIter = maxIter
        self.sampleSize = sampleSize
        self.complexSeed = complexSeed

    # Takes a complex number and determines the number of iterations required before exceeding our bound of 2, or the max iterations if it does not exceed the bound
    def iterateMandelbrot(self, c):
        z = self.complexSeed
        for n in range(self.maxIter):
            if abs(z) > 2:
                return n
            z = (z * z) + c
        return self.maxIter

    def isInMandelbrot(self, c):
        iterations = Mandelbrot.iterateMandelbrot(self, c)
        if (iterations < 500):
            print(str(c) + " is not in the mandelbrot set.")
        else:
            print(str(c) + " is in the mandelbrot set.")
        

    def mandelbrotSet(self):
        xInputs = np.linspace(self.xLower, self.xUpper, self.sampleSize)
        yInputs = np.linspace(self.yLower, self.yUpper, self.sampleSize)
        resultSet = np.zeros((self.sampleSize, self.sampleSize))

        for n in range(self.sampleSize):
            for m in range(self.sampleSize):
                # Construct the complex number
                complexNum = complex(xInputs[m], yInputs[n])

                # Is this number in the mandelbrot set?
                resultSet[n, m] = Mandelbrot.iterateMandelbrot(self, complexNum)

        return resultSet


    def renderMandelbrotPlot(self):
        mandelbrotPlot = Mandelbrot.mandelbrotSet(self)

        plt.imshow(mandelbrotPlot, extent=[self.xLower, self.xUpper, self.yLower, self.yUpper], cmap="viridis")
        plt.title("Mandelbrot Plot")
        plt.colorbar().set_label("# of iterations", rotation=270)
        plt.xlabel("Re(c)")
        plt.ylabel("Im(c)")
        plt.show()