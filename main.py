# main.py

from Vigas.viga import Viga
from Vigas.VigaAB import VigaAB
from Vigas.VigaBD import VigaBD

import json

from Definición.clasificacion import clasificacion
#from Definición.analisis import AnalisisViga

# OJO PONERLE INPUTS A ESTO

# def main():

#     try:

#         eleccion = input("¿Desea ingresar sus propios datos? Si no, \
# trabajaremos con los datos por defecto de nuestro grupo: ")
#         eleccion = eleccion.lower().strip()
#         if eleccion == "sí" or eleccion == "si":
#             l1 = input("Ingrese la longitud del vano 1, 2 y 3 separados por (m): ")
#             l2 = input("Ingrese la longitud del vano 2 (m): ")
#             l3 = input("Ingrese la longitud del vano 3 (m): ")
#             E = input("Ingrese el valor del módulo elástico equivalente de la viga (Pa): ")
#             Ii = input("Ingrese el momento de inercia de la viga izquierda (m^4): ")
#             Id = input("Ingrese el momento de inercia de la viga derecha (m^4): ")
#             w1, w2 = input("Ingrese el valor de la carga uniformemente distribuida aplicada en la viga izquierda (kN/m) : ").split(',')
#             w2 = input("Ingrese el valor de la carga concentrada en el tramo 2 (kN/m): ")

#             ya = input("Asentamiento diferencial en los apoyos (desplazamiento vertical del empotramiento A) (m): ")
#             theta_a = input("thetha a")
#             z1 = l1 # z para primer uso de la ecuación
#             p_a = input("app a") # punto de aplicación de A
#             p_Ma = input("app ma") # punto de aplicación de Ma
#             p_w1 = input("inicio w") # punto de inicio de la carga concentrada w1

#             # yd = input("yd")
#             # theta_d = input("thatad")
#             # z2 = input("z2") # para el segundo uso de la ecuación, OJO, donde se invierte el origen
#             # p_c = input("app c") # punto de aplicación de C
#             # p_w2 = input("app w2") # punto de inicio de la carfa concentrada w2

#             # delta_i = input("5")
#             # delta_s = input("4")
#         else:
#             l1 = 4
#             l2 = 2
#             l3 = 3
#             E = 80e9
#             Ii = 1.33e-3
#             Id = 2.28e-3
#             w1 = 44750
#             w2 = 179000

#             ya = 0
#             theta_a = 0
#             z1 = 4 # z para primer uso de la ecuación
#             p_a = 0 # punto de aplicación de A
#             p_Ma = 0 # punto de aplicación de Ma
#             p_w1 = 0 # punto de inicio de la carga concentrada w1

#             yd = 0
#             theta_d = 0
#             z2 = 5 # para el segundo uso de la ecuación, OJO, donde se invierte el origen
#             p_c = 3 # punto de aplicación de C
#             p_w2 = 0 # punto de inicio de la carfa concentrada w2

#             delta_i = 5e-3
#             delta_s = 4e-3


#         viga_AB = VigaAB(l1, w1)
#         viga_AB.calcular_EI(E, Ii)
#         viga_AB.sumatoria_de_M(w1, l1) 
#         viga_AB.sumatoria_de_Fy(w1, l1)
#         yb1 = viga_AB.calcular_yb(z1, ya, theta_a, w1, p_a, p_Ma, p_w1)

#         print(f"El resultado es {yb1: .5f}")

#         # viga_CD = VigaBD(5, 179000)
#         # viga_CD.calcular_EI(E, Id)
#         # viga_CD.sumatoria_de_M(w2, l2, l3)
#         # viga_CD.sumatoria_de_Fy(w2)

#         # yb2 = viga_CD.calcular_yb(z2, yd, theta_d, w2, p_c, p_w2)

#         # print(f"El resultado es {yb2: .5f}")


#         # Para guardar los resultados y poder usarlos luego:
#         with open("resultados.json", "w") as f:
#             json.dump({"yb1": yb1, "yb2": yb2}, f)

#         # Para decidir si la viga es o no continua
#         c = clasificacion()
#         if c.clasificar_viga(delta_i, delta_s):
#             print("La viga es continua, debemos rehacer los cálculos para una viga continua: ") ##### METER AQUÍ PARA REHACER LOS CÁLCULOS
#             #analisis = AnalisisViga()
#             #analisis.calcular_como_viga_continua()
#         else:
#             print("La viga no es continua, son dos vigas separadas, los resultados son ...") #### METER AQUÍ PARA MOSTRAR LOS RESULTADOS









#     except TypeError:
#         print("Error: Se espera que todos los datos sean numéricos.")



# def main():


#     eleccion = input("¿Desea ingresar sus propios datos? Si no, \
# trabajaremos con los datos por defecto de nuestro grupo: ")
#     eleccion = eleccion.lower().strip()
#     if eleccion == "sí" or eleccion == "si":
#         l1 = input("Ingrese la longitud del vano 1, 2 y 3 separados por (m): ")
#         l2 = input("Ingrese la longitud del vano 2 (m): ")
#         l3 = input("Ingrese la longitud del vano 3 (m): ")
#         E = input("Ingrese el valor del módulo elástico equivalente de la viga (Pa): ")
#         Ii = input("Ingrese el momento de inercia de la viga izquierda (m^4): ")
#         Id = input("Ingrese el momento de inercia de la viga derecha (m^4): ")
#         w1, w2 = input("Ingrese el valor de la carga uniformemente distribuida aplicada en la viga izquierda (kN/m) : ").split(',')
#  #       w2 = input("Ingrese el valor de la carga concentrada en el tramo 2 (kN/m): ")

#         ya = input("Asentamiento diferencial en los apoyos (desplazamiento vertical del empotramiento A) (m): ")
#         theta_a = input("thetha a")
#         z1 = l1 # z para primer uso de la ecuación
#         p_a = input("app a") # punto de aplicación de A
#         p_Ma = input("app ma") # punto de aplicación de Ma
#         p_w1 = input("inicio w") # punto de inicio de la carga concentrada w1

#             # yd = input("yd")
#             # theta_d = input("thatad")
#             # z2 = input("z2") # para el segundo uso de la ecuación, OJO, donde se invierte el origen
#             # p_c = input("app c") # punto de aplicación de C
#             # p_w2 = input("app w2") # punto de inicio de la carfa concentrada w2

#             # delta_i = input("5")
#             # delta_s = input("4")
#     else:
#         l1 = 4
#         l2 = 2
#         l3 = 3
#         E = 80e9
#         Ii = 1.33e-3
#         Id = 2.28e-3
#         w1 = 44750
#         w2 = 179000

#         ya = 0
#         theta_a = 0
#         z1 = 4 # z para primer uso de la ecuación
#         p_a = 0 # punto de aplicación de A
#         p_Ma = 0 # punto de aplicación de Ma
#         p_w1 = 0 # punto de inicio de la carga concentrada w1

#         yd = 0
#         theta_d = 0
#         z2 = 5 # para el segundo uso de la ecuación, OJO, donde se invierte el origen
#         p_c = 3 # punto de aplicación de C
#         p_w2 = 0 # punto de inicio de la carfa concentrada w2

#         delta_i = 5e-3
#         delta_s = 4e-3


#     viga_AB = VigaAB(l1, w1)
#     viga_AB.calcular_EI(E, Ii)
#     viga_AB.sumatoria_de_M(w1, l1) 
#     viga_AB.sumatoria_de_Fy(w1, l1)
#     yb1 = viga_AB.calcular_yb(z1, ya, theta_a, w1, p_a, p_Ma, p_w1)

#     print(f"El resultado es {yb1: .5f}")

        # viga_CD = VigaBD(5, 179000)
        # viga_CD.calcular_EI(E, Id)
        # viga_CD.sumatoria_de_M(w2, l2, l3)
        # viga_CD.sumatoria_de_Fy(w2)

        # yb2 = viga_CD.calcular_yb(z2, yd, theta_d, w2, p_c, p_w2)

        # print(f"El resultado es {yb2: .5f}")


        # Para guardar los resultados y poder usarlos luego:
        # with open("resultados.json", "w") as f:
        #     json.dump({"yb1": yb1, "yb2": yb2}, f)

        # # Para decidir si la viga es o no continua
    #    # c = clasificacion()
    #     if c.clasificar_viga(delta_i, delta_s):
    #         print("La viga es continua, debemos rehacer los cálculos para una viga continua: ") ##### METER AQUÍ PARA REHACER LOS CÁLCULOS
    #         #analisis = AnalisisViga()
    #         #analisis.calcular_como_viga_continua()
    #     else:
    #         print("La viga no es continua, son dos vigas separadas, los resultados son ...") #### METER AQUÍ PARA MOSTRAR LOS RESULTADOS









    # except TypeError:
    #     print("Error: Se espera que todos los datos sean numéricos.")



# if __name__ == "__main__":
#     main()

def main():
    l1 = 4
    l2 = 2
    l3 = 3
    E = 80e9
    Ii = 1.33e-3
    Id = 2.28e-3
    w1 = 44750
    w2 = 179000

    ya = 0
    theta_a = 0
    z1 = 4 # z para primer uso de la ecuación
    p_a = 0 # punto de aplicación de A
    p_Ma = 0 # punto de aplicación de Ma
    p_w1 = 0 # punto de inicio de la carga concentrada w1

    yd = 0
    theta_d = 0
    z2 = 5 # para el segundo uso de la ecuación, OJO, donde se invierte el origen
    p_c = 3 # punto de aplicación de C
    p_w2 = 0 # punto de inicio de la carfa concentrada w2

    delta_i = 5e-3
    delta_s = 4e-3


    viga_AB = VigaAB(l1, w1)
    viga_AB.calcular_EI(E, Ii)
    viga_AB.sumatoria_de_M(w1, l1) 
    viga_AB.sumatoria_de_Fy(w1, l1)

    yb1 = viga_AB.calcular_yb(z1, ya, theta_a, w1, p_a, p_Ma, p_w1)
    theta_b1 = viga_AB.calcular_theta_b(ya, theta_a, z1, p_Ma, p_a, p_w1, w1)
    
    print(f"El resultado es {yb1: .5f}, el ángulo es {theta_b1: .3f}°.")

    viga_CD = VigaBD(5, 179000)
    viga_CD.calcular_EI(E, Id)
    viga_CD.sumatoria_de_M(w2, l2, l3)
    viga_CD.sumatoria_de_Fy(w2)

    yb2 = viga_CD.calcular_yb(z2, yd, theta_d, w2, p_c, p_w2)
    theta_b2 = viga_CD.calcular_theta_b(yd, theta_d, z2, p_c, p_w2, w2)

    print(f"El resultado es {yb2: .5f} y el ángulo es {theta_b2: .3f}°.")


    # Para guardar los resultados y poder usarlos luego:
    with open("resultados.json", "w") as f:
        json.dump({"yb1": yb1, "yb2": yb2, "theta_b1": theta_b1, "theta_b2": theta_b2}, f)

            # Para decidir si la viga es o no continua
    c = clasificacion()
    if c.clasificar_viga(delta_i, delta_s):
        print("La viga es continua, debemos rehacer los cálculos para una viga continua: ") ##### METER AQUÍ PARA REHACER LOS CÁLCULOS
                #analisis = AnalisisViga()
                #analisis.calcular_como_viga_continua()
    else:
        print("La viga no es continua, son dos vigas separadas, los resultados son ...") #### METER AQUÍ PARA MOSTRAR LOS RESULTADOS




if __name__ == "__main__":
    main()