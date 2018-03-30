import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage.transform import resize
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage import restoration
from skimage import measure
import argparse
from skimage import data, io
from matplotlib import pyplot as plt

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
args = vars(ap.parse_args())

img = imread(args["image"], as_grey=True)
io.imshow(img)
plt.show()
image = restoration.denoise_tv_chambolle(img, weight=0.1)
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(2))
cleared = bw.copy()
io.imshow(cleared)
plt.show()

label_image = measure.label(cleared)
borders = np.logical_xor(bw, cleared)
label_image[borders] = -1

coordinates = []
i = 0

for region in regionprops(label_image):
    if region.area > 50:
        minr, minc, maxr, maxc = region.bbox
        margin = 3
        minr, minc, maxr, maxc = minr - margin, minc - margin, maxr + margin, maxc + margin
        roi = img[minr:maxr, minc:maxc]
        io.imshow(roi)
        plt.show()
        if roi.shape[0] * roi.shape[1] == 0:
            continue
        else:
            if i == 0:
                samples = resize(roi, (20, 20))
                coordinates.append(region.bbox)
                i += 1
            elif i == 1:
                roismall = resize(roi, (20, 20))
                samples = np.concatenate((samples[None, :, :], roismall[None, :, :]), axis=0)
                coordinates.append(region.bbox)
                i += 1
            else:
                roismall = resize(roi, (20, 20))
                samples = np.concatenate((samples[:, :, :], roismall[None, :, :]), axis=0)
                coordinates.append(region.bbox)
