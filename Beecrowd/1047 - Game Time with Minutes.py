a, b, c, d = map(int, input().split())

# Calculando as horas
if a < c or (a == c and b < d):  # Jogo termina no mesmo dia
    time = c - a
else:  # Jogo passa pela meia-noite
    time = (c + 24) - a

# Calculando os minutos
if b > d:
    minutos = (d + 60) - b
    time -= 1  # Remove 1 hora porque pegamos emprestado 60 minutos
else:
    minutos = d - b

# Correção para evitar 60 minutos (transformar em 1 hora extra)
if minutos == 60:
    minutos = 0
    time += 1  # Se os minutos chegaram a 60, somamos 1 hora

print(f"O JOGO DUROU {time} HORA(S) E {minutos} MINUTO(S)")
