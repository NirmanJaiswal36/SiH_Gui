import imageio.v3 as iio
import numpy as np

frames = np.vstack([
    iio.imread("giff 1.gif"),
    iio.imread("giff 2.gif"),
])

# get duration each frame is displayed
iio.imwrite("imageio_combined.gif", frames)