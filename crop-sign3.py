import cv2
image = cv2.imread(r"C:\Users\Roshanc\Desktop\ON Pan card\wMHGk.png",1)
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,img)
cv2.bitwise_not(img,img)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
print("ROshan")
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, rect_kernel)
im2, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        if(h>20):
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)

cv2.imshow("Result", image)
cv2.waitKey(0)
