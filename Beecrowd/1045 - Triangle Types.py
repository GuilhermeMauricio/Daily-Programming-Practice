a,b,c = map(float,input().split(' '))

if a>=b+c:
    print('NAO FORMA TRIANGULO')

if a**2 == (b**2)+(c**2):
    print('TRIANGULO RETANGULO')

if a**2 > (b**2)+(c**2):
    print('TRIANGULO OBTUSANGULO')

if a**2 < (b**2)+(c**2):
    print('TRIANGULO ACUTANGULO')

if a==b==c:
    print('TRIANGULO EQUILATERO')


if b==c and a!=b:
    print ('TRIANGULO ISOSCELES')

if a==c and b!=c:
    print ('TRIANGULO ISOSCELES')

if a==b and c!=b:
     print ('TRIANGULO ISOSCELES')


