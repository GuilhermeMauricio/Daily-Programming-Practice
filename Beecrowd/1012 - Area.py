a,b,c=map(float,input().split(' '))



rectangled_triangle=((a*c)/2)
area_circle=(3.14159*(c**2))
area_trapezium= (((a+b)*c)/2)
area_square=(b*b)
area_rectangle=(a*b)

print(f"TRIANGULO: {rectangled_triangle:.3f}")
print(f"CIRCULO: {area_circle:.3f}")
print(f"TRAPEZIO: {area_trapezium:.3f}")
print(f"QUADRADO: {area_square:.3f}")
print(f"RETANGULO: {area_rectangle:.3f}")