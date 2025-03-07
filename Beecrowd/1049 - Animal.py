info1=input()
info2=input()
info3=input()


if info1=='vertebrado':
    if info2 == 'ave':
        if info3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if info3 =='onivoro':
            print('homem')

        else:
            print('vaca')

else:
    if info2 =='inseto':
        if info3 =='hematofago':
            print('pulga')
        else:
            print('lagarta')
    else: 
        if info3=='hematofago':
            print('sanguessuga')
        else:
            print('minhoca')