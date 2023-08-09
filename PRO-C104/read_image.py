import cv2

# O imread() ajuda a carregar a imagem de um determinado caminho.
img = cv2.imread("butterfly.jpg")

cv2.imshow("Imagem em exibicao: ", img)

print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("Escala de cinza: ", gray_img)

#print(gray_img)

cv2.waitKey(0)