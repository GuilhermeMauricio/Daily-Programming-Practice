a,b,c,d=list(map(int,input().split()))

if(a<c):
    time=(c-a)
    if time == 1:
        time-=1 

    if (b<d):
        minutos=(d-b)
    else:
        minutos=(d+60)-b
    
else:
    time=c+24-a
    if (b<d) or (b==d):
        minutos=(d-b)
    else:
        minutos=(d+60)-b
        time -= 1

print(f"O JOGO DUROU {time} HORA(S) E {minutos} MINUTO(S)")