#crie seu código aqui!
import cv2

#lendo imagen
imagem = cv2.imread("imagem.png")

#Mostrando imagen
cv2.imshow("Imagem carregada", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
