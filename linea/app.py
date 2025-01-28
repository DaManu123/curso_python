import funciones
import argparse

def main(m:float, b:float):
    # m = 2.0
    # b = 3.0
    '''
    funcion principal que calcula las coordenadas de una linea recta recibimos m y b y regresa: nada
    :param m:
    :param b:
    :return:
    '''
    X = [x for x in range(1, 11)]
    Y = [funciones.Calcular_Y(x, m, b) for x in X]
    # print('Enteros:')
    # coordenadas_enteros = list(zip(X, Y))
    # # print(coordenadas_enteros)
    XF = [x/10.0 for x in range(10, 110, 5)]
    YF = [funciones.Calcular_Y(x, m, b) for x in XF]
    coordenadas_flotantes = list(zip(XF, YF))
    print('flotantes')
    print(coordenadas_flotantes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=float, help='pendiente de la linea',default=2.0)
    parser.add_argument('-b', type=float, help='ordenada al origen de la linea',default=3.0)
    args = parser.parse_args()
    main(args.m, args.b)