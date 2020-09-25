# lista_exemplo = [7, 3, 1, 4, 5]
#crie seu algoritmo ruim logo abaixo e ordene a lista acima!
import random

#ordenação
def ordenar_embaralhando(lista):
    while (esta_ordenado(lista) == False):
        embaralhar (lista)

#Verificar se esta ordenado
def esta_ordenado(lista): 
    n = len(lista) 
    for i in range(0, n-1): 
        if (lista[i] < lista[i+1] ): 
            return False
    return True

#Embaralhar a lista
def embaralhar(lista):
    n = len(lista)
    for i in range (0,n): 
        r = random.randint(0,n-1) 
        lista[i], lista[r] = lista[r], lista[i] 

#cria a lista
lista = [7, 3, 1, 4, 5]

#chamada da função  ordenar
ordenar_embaralhando(lista)

#imprime a lista ordenada 
print("Lista ordenada :") 
for i in range(len(lista)): 
    print (lista[i]), 


