#crie seu código aqui!
import cv2

#lendo imagen
imagem = cv2.imread("imagem.png")

#receber informação do usuario
x = int(input("Informe o a posição x: "))
y = int(input("Informe o a posição y: "))
l = int(input("Informe o a largura: : "))

#modificando a imagem
imagem[x:l, y:l] = (0, 0, 0)

#mostrando a imagem modificada
cv2.imshow("Modificada", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Salvando imagem
cv2.imwrite("imagemModificada.png", imagem)
