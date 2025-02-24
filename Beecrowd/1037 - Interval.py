number=float(input())

if number>=0 and number<=25:
    print('Intervalo [0,25]')

elif number>=25.01 and number<=50:
    print('Intervalo (25,50]')

elif number>=50.01 and number<=75:
    print('Intervalo (50,75]')

elif number>=75.01 and number<=100:
    print('Intervalo (75,100]')

else:
    print('Fora de intervalo')