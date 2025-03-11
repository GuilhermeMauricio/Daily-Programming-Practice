Even_count=0

for i in range(5):
    number=int(input())
    if number%2==0:
        Even_count=(Even_count+1)

print(f'{Even_count} valores pares')