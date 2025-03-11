Even_numbers=0
Odd_numbers=0
Positive_numbers=0
Negative_numbers=0

for i in range(5):
    number=int(input())
    
    if number%2==0:
        Even_numbers=(Even_numbers+1)
    else:
        Odd_numbers=(Odd_numbers+1)
    
    if number>0:
        Positive_numbers=(Positive_numbers+1)
    
    elif number<0:
        Negative_numbers=(Negative_numbers+1)

print(Even_numbers,' valor(es) par(es)')
print(Odd_numbers,' valor(es) impar(es)')
print(Positive_numbers,' valor(es) positivo(s)')
print(Negative_numbers,' valor(es) negativo(s)')