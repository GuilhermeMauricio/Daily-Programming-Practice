a,b = map(int,input().split(' '))

if a>b:
    if a%b!=0:
        print('Nao sao Multiplos')
    else:
        print('Sao Multiplos')
else:
    if b%a!=0:
        print('Nao sao Multiplos')
    else:
        print('Sao Multiplos')