import numpy as np
import matplotlib.pyplot as plt

def f(x, x0, y0, x1, y1):
    """Ecuación de la recta que pasa por (x0, y0) (x1, y1)"""
    return (y1-y0)/(x1-x0)*(x-x0) + y0



a = 1.0
b = 10
x = np.linspace(a,b, num= 100)
length = 100
lista = [(a + x * (b - a)/length)**3 for x in range(length)]
print(lista)

plt.plot(x,lista, 'o', color="red")
plt.show()