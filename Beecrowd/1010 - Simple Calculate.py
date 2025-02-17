code, units, price =input().split(' ')
code=int(code)
units=int(units)
price=float(price)
First=(units*price)


code2, units2, price2 =input().split(' ')
code2=int(code2)
units2=int(units2)
price2=float(price2)
Second=(units2*price2)

print(f'VALOR A PAGAR: R$ {First+Second:.2f}')