import numpy as np
import matplotlib.pyplot as plt

def f(x, x0, y0, x1, y1):
    """Ecuación de la recta que pasa por (x0, y0) (x1, y1)"""
    return (y1-y0)/(x1-x0)*(x-x0) + y0


def main():
    a = 1
    b = 10
    length = 100
    test_list = [(a + x * (b - a)/length)**3 for x in range(length)]
    print(test_list)

    #x=np.linspace(a[0],b[0], num= 100)

    plt.plot(a,test_list, 'o', color="red")

if __name__ == '__main__':
    main()