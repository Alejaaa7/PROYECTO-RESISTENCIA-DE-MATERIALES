# Se crea la carpeta definición porque se va a usar para definir si la 
# viga es o no continua, y así poder llegar a las respuestas esperadas.

# Y el archivo clasificación porque en este se clasifica si es o no continua:

# clasificacion.py

import json

with open("resultados.json", "r") as f:
    datos = json.load(f)

yb1 = datos["yb1"]
yb2 = datos["yb2"]

diferencia = yb2 - yb1 # comparar el descenso entre vigas

class clasificacion:
    def __init__(self):
        self.viga_continua = None
        pass

    def clasificar_viga(self, delta_i: float, delta_s: float):
        if -delta_i < diferencia < delta_s:
            self.viga_continua = False
        else:
            self.viga_continua = True
        
        return self.viga_continua


    