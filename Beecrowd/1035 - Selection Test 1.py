A,B,C,D = map(int,input().split(' '))

if B>C and D>A:
    if C+D>A+B:
        if A%2==0:
            print('Valores aceitos')
        else:
            print('Valores nao aceitos')
    else:
            print('Valores nao aceitos')
else:
            print('Valores nao aceitos')