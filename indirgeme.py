import numpy
import cv2

img =  cv2.imread("/Users/altun/Desktop/kimlik.jpeg")

imgRsz = cv2.resize(img,(1024,1024))
cv2.imshow("rsize",imgRsz)
cv2.imwrite("/Users/altun/Desktop/kimlik2.jpeg",imgRsz)


cv2.waitKey(0)
cv2.destroyAllWindows()

