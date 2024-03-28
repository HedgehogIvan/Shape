from figure.circle import Circle
from figure.triangle import Triangle

c_test = Circle(5)
t_test = Triangle(9, 12, 15)

print(f"Площадь круга: {c_test.area()}", f"Площадь трегольника: {t_test.area()}", sep='\n')