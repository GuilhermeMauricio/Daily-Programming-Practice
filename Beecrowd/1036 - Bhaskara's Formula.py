from math import sqrt
A, B, C= map(float,(input()).split(' '))
if A!=0:
    delta=(B**2)-(4*A*C)
    if delta>0:
        r1=((-B)+sqrt(delta))/(2*A)
        r2=((-B)-sqrt(delta))/(2*A)
        print(f'R1 = {r1:.5f}')
        print(f'R2 = {r2:.5f}')
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')