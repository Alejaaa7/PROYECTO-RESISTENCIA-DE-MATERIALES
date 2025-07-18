# tablas.py

# por ahora, se crea tablas.py para crear las tablas resumen, luego se 
# encontrará la manera de incorporarlo al main.py :)

import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Se vuelven a usar los datos guardados:
import json

# tablas.py

# Se vuelven a usar los datos guardados:

with open("resultados.json", "r") as f:
    datos = json.load(f)

yb1 = round(datos["yb1"], 5)
yb2 = round(datos["yb2"], 5)
theta_b1 = round(datos["theta_b1"], 5)
theta_b2 = round(datos["theta_b2"], 5)

# Se crea una función que en main nos permita crear las tablas
def generar_tabla():
    # Los datos que van en la tabla
    data = {
        "VIGA": ["Viga Izquierda", "Viga Derecha"],
        "Deflexión (mm)": [f"{yb1: .5f}", f"{yb2: .5f}"],
        "Pendiente (°)": [f"{theta_b1: .5f}", f"{theta_b2: .5f}"]
    }

    # Se crea el DataFrame
    df = pd.DataFrame(data)

    # Se ponen colores bonitos
    color_arriba = "#ff7ed6"
    color_filas = ["#ffffff", "#e2b9f8"] #si el usuario desea, puede cambiar los colores
    color_titulo = "#442a59"

    # Figura tipo dashborad

    fig, ax = plt.subplots(figsize = (11, 8.5))
    ax.axis("off")

    # Crear el título principal
    plt.title("TABLA RESUMEN DE DEFLEXIÓN Y PENDIENTE", fontsize = 30, \
            fontweight = "bold", color = color_titulo, loc = "center", pad = 30)

    # Crear la tabla bonita
    tabla = ax.table(
        cellText = df.values,
        colLabels = df.columns,
        cellLoc = "center",
        loc = "center",
        colColours = [color_arriba] * len(df.columns)
    )

    # Estilizar tabla para que sea más bonita
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1.5, 2.5)

    # Poner estilo a las celdas
    for i in range(len(df)):
        fondo = color_filas[i % 2]
        for j in range(len(df.columns)):
            tabla[(i + 1, j)].set_facecolor(fondo)
            tabla[(i + 1, j)].set_text_props(color = "black", \
                                            fontname = "DejaVu Serif")

    # Parte de arriba con letra blanca y fondo color
    for j in range(len(df.columns)):
        tabla[(0, j)].set_text_props(weight = "bold", color = "white", \
                                            fontname = "DejaVu Serif" )

    # Pie de página pro
    diauso = datetime.datetime.now().strftime("%d/%m/%Y")
    fig.text(0.5, 0.05, f"Generado el {diauso}",
            ha = "center", fontsize = 8, color = "gray")

    # GUARDAR PDF!
    nombre = input("¿Cómo quiere guardar su tabla resumen de deflexión y pendiente?  (sin extensión): ").strip()

    # Asegurarse de que termine en ".pdf"
    if not nombre.lower().endswith(".pdf"):
        nombre += ".pdf"

    plt.savefig(nombre, bbox_inches="tight", pad_inches=0.5)
    plt.close()

    print(f"✅ PDF exportado exitosamente como '{nombre}'\
    (encuéntrelo en la carpeta donde ejecutó este archivo).")
