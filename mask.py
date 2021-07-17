import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sm.png',0)

ret,thresh2 = cv2.threshold(img,5,255,cv2.THRESH_BINARY_INV)

titles = 'BINARY'
images = thresh2

plt.imshow(images,'gray')
plt.title(titles)


plt.show()
cv2.imwrite('thresh.png',images)