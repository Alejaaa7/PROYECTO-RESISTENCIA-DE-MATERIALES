# tablas.py

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.backends.backend_pdf import PdfPages


# Se crea una función que en main nos permita crear las tablas
def generar_tabla_delta1():
    # Los datos que van en la tabla
    data = {
        "Valor": ["Valor máximo", "Valor mínimo"],
        "V (kN)": ["270", "-1000"],
        "Mf (kNm)": ["-900", "-3500"],
        "Ubicación V critico(m)": ["0", "6"],
        "Ubicación M critico(m)": ["0", "4"]
    }

    # Se crea el DataFrame
    df = pd.DataFrame(data)

    # Se ponen colores bonitos
    color_arriba = "#7e8bff"
    color_filas = ["#ffffff", "#b9b9f8"] #si el usuario desea, puede cambiar los colores
    color_titulo = "#2e2a59"

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
    nombre = input("¿Cómo quiere guardar su tabla resumen de valores críticos? (sin extensión): ").strip()

    # Asegurarse de que termine en ".pdf"
    if not nombre.lower().endswith(".pdf"):
        nombre += ".pdf"

    plt.savefig(nombre, bbox_inches="tight", pad_inches=0.5)
    plt.close()

    print(f"✅ PDF exportado exitosamente como '{nombre}'\
    (encuéntrelo en la carpeta donde ejecutó este archivo).")


# tabla_puntos_criticos.py

# Se crea una función que en main nos permita crear las tablas
def generar_tabla_delta2():
    # Los datos que van en la tabla
    data = {
        "Valor": ["Valor máximo", "Valor mínimo"],
        "V (kN)": ["400", "-110"],
        "Mf (kNm)": ["750", "-1000"],
        "Ubicación V critico(m)": ["9", "6"],
        "Ubicación M critico(m)": ["4", "0"]
    }

    # Se crea el DataFrame
    df = pd.DataFrame(data)

    # Se ponen colores bonitos
    color_arriba = "#7e8bff"
    color_filas = ["#ffffff", "#b9b9f8"] #si el usuario desea, puede cambiar los colores
    color_titulo = "#2e2a59"

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
    nombre = input("¿Cómo quiere guardar su tabla resumen de valores críticos? (sin extensión): ").strip()

    # Asegurarse de que termine en ".pdf"
    if not nombre.lower().endswith(".pdf"):
        nombre += ".pdf"

    plt.savefig(nombre, bbox_inches="tight", pad_inches=0.5)
    plt.close()

    print(f"✅ PDF exportado exitosamente como '{nombre}'\
    (encuéntrelo en la carpeta donde ejecutó este archivo).")

# tablas.py

# Se crea una función que en main nos permita crear las tablas
def generar_tabla_delta3():
    # Los datos que van en la tabla
    data = {
        "Valor": ["Valor máximo", "Valor mínimo"],
        "V (kN)": ["220", "-1000"],
        "Mf (kNm)": ["-700", "-3300"],
        "Ubicación V critico(m)": ["0", "6"],
        "Ubicación M critico(m)": ["0", "4"]
    }

    # Se crea el DataFrame
    df = pd.DataFrame(data)

    # Se ponen colores bonitos
    color_arriba = "#7e8bff"
    color_filas = ["#ffffff", "#b9b9f8"] #si el usuario desea, puede cambiar los colores
    color_titulo = "#2e2a59"

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
    nombre = input("¿Cómo quiere guardar su tabla resumen de valores críticos? (sin extensión): ").strip()

    # Asegurarse de que termine en ".pdf"
    if not nombre.lower().endswith(".pdf"):
        nombre += ".pdf"

    plt.savefig(nombre, bbox_inches="tight", pad_inches=0.5)
    plt.close()

    print(f"✅ PDF exportado exitosamente como '{nombre}'\
    (encuéntrelo en la carpeta donde ejecutó este archivo).")
