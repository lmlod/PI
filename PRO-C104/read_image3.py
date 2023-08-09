import cv2


img = cv2.imread("poster.jpg")

rocket = img[120:360,400:500]

img[0:240,500:600] = rocket

#print(img)

text_to_show = "FOGUETE"

cv2.putText(img,
            text_to_show,
            (20,220),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.9,
            color=(0,0,255))

cv2.imshow("Resultado: ", img)

cv2.waitKey(0)