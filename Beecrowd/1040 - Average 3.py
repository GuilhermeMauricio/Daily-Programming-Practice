n1,n2,n3,n4 = map(float,input().split(' '))

average=((n1*2)+(n2*3)+(n3*4)+(n4*1))/(2+3+4+1)

if average>=7 and average<=10:
    print(f'Media: {average:.1f}')
    print('Aluno aprovado.')

elif average<5:
    print(f'Media: {average:.1f}')
    print('Aluno reprovado.')

elif average>=5 and average<=6.9:
    print(f'Media: {average:.1f}')
    print('Aluno em exame.')
    exam=float(input())
    print(f'Nota do exame: {exam:.1f}')
    final_Average=(exam+average)/2
    if final_Average>=5:
        print('Aluno aprovado.')
        print(f'Media final: {final_Average:.1f}')
    else:
        print('Aluno reprovado')
        print(f'Media final: {final_Average:.1f}')