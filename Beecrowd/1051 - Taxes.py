salary=float(input())
imposto=0
if salary>=0 and salary<=2000.00:
    print('Isento')

elif salary>=2000.01 and salary<=3000.00:
    Tax_free=salary-2000
    imposto=(Tax_free*0.08)
    print(imposto)

elif salary>=3000.01 and salary<=4500.00:
    Tax_free=salary-2000
    tax=Tax_free-1000
    por8=1000*0.08
    por18=tax*0.18
    montante=(por18+por8)
    print(montante)

elif salary>4.500:
    Tax_free=salary-2000
    tax=Tax_free-2500
    por8=1000*0.08
    por18=1500*0.18
    por28=tax*0.28
    montante=(por28+por18+por8)
    print(montante)