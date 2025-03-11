Positive_values=0
Positive_list=[]

for i in range(6):
    number=float(input())
    if number>0:
        Positive_values=(Positive_values+1)
        Positive_list.append(number)
print(f'{Positive_values} valores positivos')
average=(sum(Positive_list)/len(Positive_list))
print(f'{average:.1f}')