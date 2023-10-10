import cv2
import numpy as np

img = np.zeros((600, 900, 3), dtype=np.uint8)

# background
cv2.rectangle(img, (0, 0), (900, 500), (255, 255, 85), -1)
cv2.rectangle(img, (0, 500), (900, 600), (75, 180, 70), -1)

# sun
cv2.circle(img, (200, 150), 60, (0, 255, 255), -1)
cv2.circle(img, (200, 150), 75, (220, 255, 255), 10)

# tree
cv2.line(img, (710, 500), (710, 420), (30, 65, 155), 15)
triangle2 = np.array([[640, 460], [780, 460], [710, 200]], dtype=np.int32)  # array to darw fillpoly
cv2.fillPoly(img, [triangle2], (75, 180, 70))

cv2.line(img, (600, 500), (600, 420), (30, 65, 155), 25)  # darw line
triangle = np.array([[500, 440], [700, 440], [600, 75]], dtype=np.int32)  # tree leafs
cv2.fillPoly(img, [triangle], (75, 200, 70))  # array to darw the second fillpoly

# text
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # text type
cv2.putText(img, "I Love Python", (120, 490), font, 1.5, (255, 255, 255), 2)  # write text on image

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
