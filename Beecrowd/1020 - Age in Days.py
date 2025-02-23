days=int(input())

Year=days//365
month=((days%365)//30)
day=((days%365)%30)

print(f'{Year} ano(s)')
print(f'{month} mes(es)')
print(f"{day} dia(s)")