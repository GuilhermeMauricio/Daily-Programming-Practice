X,Y = map(int,input().split(' '))

if X==1:
    total=4*Y
    print(f'Total: R$ {total:.2f}')

elif X==2:
    total=4.50*Y
    print(f'Total: R$ {total:.2f}')

elif X==3:
    total=5*Y
    print(f'Total: R$ {total:.2f}')

elif X==4:
    total=2*Y
    print(f'Total: R$ {total:.2f}')

elif X==5:
    total=1.50*Y
    print(f'Total: R$ {total:.2f}')


