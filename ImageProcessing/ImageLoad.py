import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread('/content/ainstein.jpg')
cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
