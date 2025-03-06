a,b,c = map(float,input().split(' '))

lista=[]
lista.append(a)
lista.append(b)
lista.append(c)

lista_ordenada=sorted(lista)

if lista_ordenada[2]>=lista_ordenada[1]+lista_ordenada[0]:
    print('NAO FORMA TRIANGULO')

elif lista_ordenada[2]**2 == (lista_ordenada[1]**2)+(lista_ordenada[0]**2):
    print('TRIANGULO RETANGULO')

elif lista_ordenada[2]**2 > (lista_ordenada[1]**2)+(lista_ordenada[0]**2):
    print('TRIANGULO OBTUSANGULO')

elif lista_ordenada[2]**2 < (lista_ordenada[1]**2)+(lista_ordenada[0]**2):
    print('TRIANGULO ACUTANGULO')

if lista_ordenada[2]==lista_ordenada[1]==lista_ordenada[0]:
    print('TRIANGULO EQUILATERO')

if lista_ordenada[1]==lista_ordenada[0] and lista_ordenada[2]!=lista_ordenada[1]:
    print ('TRIANGULO ISOSCELES')

if lista_ordenada[2]==lista_ordenada[0] and lista_ordenada[1]!=lista_ordenada[0]:
    print ('TRIANGULO ISOSCELES')

if lista_ordenada[2]==lista_ordenada[1] and lista_ordenada[0]!=lista_ordenada[2]:
     print ('TRIANGULO ISOSCELES')


