import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread('/content/ainstein.jpg')
negative_image = abs(255-img)
cv2_imshow(img)
cv2_imshow(negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
