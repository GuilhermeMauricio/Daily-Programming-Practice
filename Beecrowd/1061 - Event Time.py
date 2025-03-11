ini_dia=int(input('Dia '))
ini_horas,ini_minutos,ini_segundos=map(int,input().split(' : '))


fim_dia=int(input('Dia '))
fim_horas,fim_minutos,fim_segundos=map(int,input().split(' : '))


print(fim_dia-ini_dia,'dia(s)')
print(fim_horas-ini_horas,'hora(s)')
print(fim_minutos-ini_minutos,'minuto(s)')
print(fim_segundos-ini_segundos,'segundo(s)')