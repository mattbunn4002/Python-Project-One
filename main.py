import Mandelbrot

sampleSize = int(input("Please input the desired sampling size (the higher the number the higher the resolution, default 1000): ").strip() or 1000)
complexSeedReal = float(input("Please input the real component of the seed complex number (default 0): ").strip() or 0)
complexSeedIm = float(input("Please input the imaginary component of the seed complex number (default 0): ").strip() or 0)

mandelbrot = Mandelbrot.Mandelbrot(-2, 2, -2, 2, 100, sampleSize, complex(complexSeedReal, complexSeedIm))
mandelbrot.renderMandelbrotPlot()

