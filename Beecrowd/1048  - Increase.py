salary=float(input())

if salary>=0 and salary<=400.00:
    newsalary=salary+(salary*0.15)
    print(f'Novo salario: {newsalary:.2f}')
    print(f'Reajuste ganho: {newsalary-salary:.2f}')
    print(f'Em percentual: 15 %')

elif salary>=400.01 and salary<=800.00:
    newsalary=salary+(salary*0.12)
    print(f'Novo salario: {newsalary:.2f}')
    print(f'Reajuste ganho: {newsalary-salary:.2f}')
    print(f'Em percentual: 12 %')

elif salary>=800.01 and salary<=1200.00:
    newsalary=salary+(salary*0.10)
    print(f'Novo salario: {newsalary:.2f}')
    print(f'Reajuste ganho: {newsalary-salary:.2f}')
    print(f'Em percentual: 10 %')


elif salary>=1200.01 and salary<=2000.00:
    newsalary=salary+(salary*0.07)
    print(f'Novo salario: {newsalary:.2f}')
    print(f'Reajuste ganho: {newsalary-salary:.2f}')
    print(f'Em percentual: 7 %')

else:
    newsalary=salary+(salary*0.04)
    print(f'Novo salario: {newsalary:.2f}')
    print(f'Reajuste ganho: {newsalary-salary:.2f}')
    print(f'Em percentual: 4 %')