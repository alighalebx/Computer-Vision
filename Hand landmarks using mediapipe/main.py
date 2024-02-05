import cv2
import time
import mediapipe

result = cv2.VideoWriter('handlandmarks.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (640,480))

cap = cv2.VideoCapture("video.mp4")

mphands = mediapipe.solutions.hands
hands = mphands.Hands()#static_image_mode=False
mpDraw = mediapipe.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    _, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for idd,lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(idd,cx,cy)
                if idd == 0:
                    cv2.circle(img,(cx,cy),9,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(15,60),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255))
    result.write(img)
    cv2.imshow("frame",img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
cap.release()

