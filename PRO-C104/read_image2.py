import numpy as np
import cv2

# O NumPy possui muitos métodos; por enquanto, usaremos seu
# método .zeros() para criar um array preenchido com todos os zeros.


black = np.zeros([600,600])
#print(black)

#f_row = black[1:2]
#print(f_row)

#f_col = black[:,1:2]
#print(f_col)

black[200:400,200:400] = 255
print(black)

cv2.imshow("preto", black)
cv2.waitKey(0)