number=float(input())
resto_por100=(number//100)
resto_por50=((number%100)//50)
resto_por20=(((number%100)%50)//20)
resto_por10=((((number%100)%50)%20)//10)
resto_por5=(((((number%100)%50)%20)%10)//5)
resto_por2=((((((number%100)%50)%20)%10)%5)//2)


print('NOTAS:')
print(f"{resto_por100:.0f} nota(s) de R$ 100.00")
print(f"{resto_por50:.0f} nota(s) de R$ 50.00")
print(f"{resto_por20:.0f} nota(s) de R$ 20.00")
print(f"{resto_por10:.0f} nota(s) de R$ 10.00")
print(f"{resto_por5:.0f} nota(s) de R$ 5.00")
print(f"{resto_por2:.0f} nota(s) de R$ 2.00")

moeda=(((((((number%100)%50)%20)%10)%5)%2)//1)
moeda_por050=((((((((number%100)%50)%20)%10)%5)%2)%1)//0.50)
moeda_por025=(((((((((number%100)%50)%20)%10)%5)%2)%1)%0.50)//0.25)
moeda_por010=((((((((((number%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)//0.10)
moeda_por005=(((((((((((number%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)//0.05)
moeda_por001=((((((((((((number%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)%0.05)/0.01)

print('MOEDAS:')
print(f"{moeda:.0f} moeda(s) de R$ 1.00")
print(f"{moeda_por050:.0f} moeda(s) de R$ 0.50")
print(f"{moeda_por025:.0f} moeda(s) de R$ 0.25")
print(f"{moeda_por010:.0f} moeda(s) de R$ 0.10")
print(f"{moeda_por005:.0f} moeda(s) de R$ 0.05")
print(f"{moeda_por001:.0f} moeda(s) de R$ 0.01")