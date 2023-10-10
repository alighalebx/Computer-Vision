
import cv2

img = cv2.imread('./apple.jpg',0)  # 0 for gray scale , 1 for color , -1 for alpha channel

cv2.imshow('image', img)


k = cv2.waitKey(0)

if k == 27:  # esc in keyboard
    cv2.destroyAllWindows()  # close the window

elif k == ord('s'):  # if order is s save the image
    cv2.imwrite('lena_copy.png', img)  # write image in your pc
    cv2.destroyAllWindows()  # close the window