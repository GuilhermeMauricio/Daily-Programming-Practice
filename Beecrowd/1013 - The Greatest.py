a,b,c = map(int,input().split(' '))

MaiorAB=(((a+b)+(abs(a-b)))/2)
maior = (MaiorAB + c + abs(MaiorAB-c))/2
maior=int(maior)
print(maior,'eh o maior')