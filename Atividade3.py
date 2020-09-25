#crie seu código aqui!
import cv2

#lendo imagem
imagem = cv2.imread("imagem.png")

#Mostrando a imagem e suas propriedades
cv2.imshow("Imagem carregada", imagem)
print ("Altura: %d pixels" % (imagem.shape[0]))
print ("Largura: %d pixels" % (imagem.shape[1]))
print ("Canais: %d" % (imagem.shape[2]))

#Separando Canais da imagem
(imageBlue, imageGreen, imageRed) = cv2.split(imagem)

#Mosrando canais da imagem
cv2.imshow("Canal Vermelho",imageRed)
cv2.imshow("Canal Verde",imageGreen)
cv2.imshow("Canal Azul",imageBlue)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Tamanho da imagem em bytes
print("Tamanho da imagem em bytes:",imagem.size)
