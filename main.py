# main.py

from Vigas.viga import Viga
from Vigas.VigaAB import VigaAB
from Vigas.VigaBD import VigaBD

from Tablas_Graficas.graficas import exportar_graficas_delta1
from Tablas_Graficas.graficas import exportar_graficas_delta2
from Tablas_Graficas.graficas import exportar_graficas_delta3

import math
import json


from Tablas_Graficas.tablas import generar_tabla
from Tablas_Graficas.tablas_puntos_criticos import generar_tabla_delta1
from Tablas_Graficas.tablas_puntos_criticos import generar_tabla_delta2
from Tablas_Graficas.tablas_puntos_criticos import generar_tabla_delta3

def main():
    print("Bienvenido, este código le permitirá desarrollar la viga combinada \
    presentada en el Proyecto 3.")

    delta_a = input("Por favor, ingrese el valor de delta a a probar: ")
    l1 = 4
    l2 = 2
    l3 = 3
    E = 80e9
    Ii = 1.33e-3
    Id = 2.28e-3
    w1 = 44750
    w2 = 179000

    vigaAB = VigaAB(l1, w1)
    vigaAB.calcular_EI(E, Ii)
    vigaAB.Análisis_Estático()
    yb1, theta_b1 = vigaAB.calcular_yb_thetab()

    vigaBD = VigaBD(l2, l3, w2)
    vigaBD.calcular_EI(E, Id)
    vigaBD.Análisis_Estático()
    yb2, theta_b2 = vigaBD.calcular_yb_thetab()

    resultados = {"yb1": yb1, "theta_b1": theta_b1, "yb2": yb2, "theta_b2": theta_b2}

        # Check for non-finite values before saving
    if all(math.isfinite(val) for val in resultados.values()):
        with open("resultados.json", "w") as f:
            json.dump(resultados, f)
    else:
        print("Error: Some calculated values are not finite and cannot be saved to JSON.")
        print(resultados)


    print(
            f"\nPor lo tanto, los resultados iniciales (presentados en las tablas) son:\n"
            f"  - Viga izquierda -> deflexión en b: {yb1:.5f} mm, inclinación: {theta_b1:.5f}°\n"
            f"  - Viga derecha  -> deflexión en b: {yb2:.5f} mm, inclinación: {theta_b2: .5f}°."
        )

    generar_tabla()
    if delta_a == "0":
        exportar_graficas_delta1()
        generar_tabla_delta1()
    elif delta_a == "10":
        exportar_graficas_delta2()
        generar_tabla_delta2()
    elif delta_a == "-10":
        exportar_graficas_delta3()
        generar_tabla_delta3()
    else:
        print("Error: Las gráficas solo serán generadas para los datos por defecto. Ingrese un valor válido (0, 10, -10). ")

if __name__ == '__main__':
    main()