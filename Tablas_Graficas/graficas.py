# SE DIVIDEN EN LAS TRES OPCIONES PARA DELTA, PARA FACILITAR EL MANEJO DE
# DATOS

import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# GRÁFICAS DELTA_A = 0

def exportar_graficas_delta1():
  # Valores conocidos (ajústalos si son otros)
  l1 = 4  # m
  l2 = 2  # m
  l3 = 3  # m
  w1 = 44750  # N/m
  w2 = 179000  # N/m

  # Constantes dadas
  A = 312539.635538
  Ma = 892158.542152
  C = 523267.274103
  D = -433056.909641

  # Dominio
  x1 = np.linspace(0, l1, 300)
  x2 = np.linspace(l1, l1 + l2, 300)
  x3 = np.linspace(l1 + l2, l1 + l2 + l3, 300)

  # Variable y para segundo y tercer tramo
  y2 = l1 + l2 + l3 - x2
  y3 = l1 + l2 + l3 - x3

  # Cortante
  V1 = A - w1 * x1
  V2 = D + C - w2 * y2
  V3 = D - w2 * y3

  # Momento
  M1 = (A * x1) - Ma - (w1 * x1 ** 2) / 2
  M2 = (D * y2) + (C * (y2 - l3)) - (w2 * (y2 ** 2) / 2)
  M3 = (D * y3) - (w2 * (y3 ** 2) / 2)

  # Crear figuras y exportar
  with PdfPages("diagramas_cortante_momento(ya_0).pdf") as pdf:

      # --- Diagrama de Fuerza Cortante ---
      plt.figure(figsize=(10, 5))
      plt.plot(x1, V1, color="#E91E63", linewidth=2, label='V(x)')
      plt.plot(x2, V2, color="#E91E63", linewidth=2)
      plt.plot(x3, V3, color="#E91E63", linewidth=2)
      plt.fill_between(x1, V1, color="#F8BBD0", alpha=0.4)
      plt.fill_between(x2, V2, color="#F8BBD0", alpha=0.4)
      plt.fill_between(x3, V3, color="#F8BBD0", alpha=0.4)
      plt.axhline(0, color='black', linewidth=1)
      plt.title("DIAGRAMA DE FUERZA CORTANTE", fontsize=18, fontweight='bold')
      plt.xlabel("Longitud x (m)", fontsize=14)
      plt.ylabel("Cortante V(x) [N]", fontsize=14)
      plt.grid(True, linestyle='--', alpha=0.5)
      plt.legend()
      plt.tight_layout()
      plt.text(6, min(np.min(V1), np.min(V2), np.min(V3)) * 0.9, f"Generado el 18/07/2025", fontsize=8)
      pdf.savefig()
      plt.close()

      # --- Diagrama de Momento Flector ---
      plt.figure(figsize=(10, 5))
      plt.plot(x1, M1, color="#3F51B5", linewidth=2, label='M(x)')
      plt.plot(x2, M2, color="#3F51B5", linewidth=2)
      plt.plot(x3, M3, color="#3F51B5", linewidth=2)
      plt.fill_between(x1, M1, color="#C5CAE9", alpha=0.4)
      plt.fill_between(x2, M2, color="#C5CAE9", alpha=0.4)
      plt.fill_between(x3, M3, color="#C5CAE9", alpha=0.4)
      plt.axhline(0, color='black', linewidth=1)
      plt.title("DIAGRAMA DE MOMENTO FLECTOR", fontsize=18, fontweight='bold')
      plt.xlabel("Longitud x (m)", fontsize=14)
      plt.ylabel("Momento M(x) [N·m]", fontsize=14)
      plt.grid(True, linestyle='--', alpha=0.5)
      plt.legend()
      plt.tight_layout()
      plt.text(6, min(np.min(M1), np.min(M2), np.min(M3)) * 0.9, f"Generado el 18/07/2025", fontsize=8)
      pdf.savefig()
      plt.close()

  print("Listo. Diagramas exportados como 'diagramas_cortante_momento(ya_0).pdf'")

# ------------------------------------------------------------------------

# GRÁFICAS DELTA_A = 10

def exportar_graficas_delta2():
  # Valores conocidos (ajústalos si son otros)
  l1 = 4  # m
  l2 = 2  # m
  l3 = 3  # m
  w1 = 44750  # N/m
  w2 = 179000  # N/m

  # Constantes dadas
  A =350352.073840
  Ma = 1043408.295360
  C = 460246.543600
  D = 407848.617440

  # Dominio
  x1 = np.linspace(0, l1, 300)
  x2 = np.linspace(l1, l1 + l2, 300)
  x3 = np.linspace(l1 + l2, l1 + l2 + l3, 300)

  # Variable y para segundo y tercer tramo
  y2 = l1 + l2 + l3 - x2
  y3 = l1 + l2 + l3 - x3

  # Cortante
  V1 = A - w1 * x1
  V2 = D + C - w2 * y2
  V3 = D - w2 * y3

  # Momento
  M1 = (A * x1) - Ma - (w1 * x1 ** 2) / 2
  M2 = (D * y2) + (C * (y2 - l3)) - (w2 * (y2 ** 2) / 2)
  M3 = (D * y3) - (w2 * (y3 ** 2) / 2)

  # Crear figuras y exportar
  with PdfPages("diagramas_cortante_momento(ya_10).pdf") as pdf:

      # --- Diagrama de Fuerza Cortante ---
      plt.figure(figsize=(10, 5))
      plt.plot(x1, V1, color="#E91E63", linewidth=2, label='V(x)')
      plt.plot(x2, V2, color="#E91E63", linewidth=2)
      plt.plot(x3, V3, color="#E91E63", linewidth=2)
      plt.fill_between(x1, V1, color="#F8BBD0", alpha=0.4)
      plt.fill_between(x2, V2, color="#F8BBD0", alpha=0.4)
      plt.fill_between(x3, V3, color="#F8BBD0", alpha=0.4)
      plt.axhline(0, color='black', linewidth=1)
      plt.title("DIAGRAMA DE FUERZA CORTANTE", fontsize=18, fontweight='bold')
      plt.xlabel("Longitud x (m)", fontsize=14)
      plt.ylabel("Cortante V(x) [N]", fontsize=14)
      plt.grid(True, linestyle='--', alpha=0.5)
      plt.legend()
      plt.tight_layout()
      plt.text(6, min(np.min(V1), np.min(V2), np.min(V3)) * 0.9, f"Generado el 18/07/2025", fontsize=8)
      pdf.savefig()
      plt.close()

      # --- Diagrama de Momento Flector ---
      plt.figure(figsize=(10, 5))
      plt.plot(x1, M1, color="#3F51B5", linewidth=2, label='M(x)')
      plt.plot(x2, M2, color="#3F51B5", linewidth=2)
      plt.plot(x3, M3, color="#3F51B5", linewidth=2)
      plt.fill_between(x1, M1, color="#C5CAE9", alpha=0.4)
      plt.fill_between(x2, M2, color="#C5CAE9", alpha=0.4)
      plt.fill_between(x3, M3, color="#C5CAE9", alpha=0.4)
      plt.axhline(0, color='black', linewidth=1)
      plt.title("DIAGRAMA DE MOMENTO FLECTOR", fontsize=18, fontweight='bold')
      plt.xlabel("Longitud x (m)", fontsize=14)
      plt.ylabel("Momento M(x) [N·m]", fontsize=14)
      plt.grid(True, linestyle='--', alpha=0.5)
      plt.legend()
      plt.tight_layout()
      plt.text(6, min(np.min(M1), np.min(M2), np.min(M3)) * 0.9, f"Generado el 18/07/2025", fontsize=8)
      pdf.savefig()
      plt.close()

  print("Listo. Diagramas exportados como 'diagramas_cortante_momento(ya_10).pdf'")

# -----------------------------------------------------------------------------

# GRÁFICAS DELTA_A = 10

def exportar_graficas_delta3():
  # Valores conocidos (ajústalos si son otros)
  l1 = 4  # m
  l2 = 2  # m
  l3 = 3  # m
  w1 = 44750  # N/m
  w2 = 179000  # N/m

  # Constantes dadas
  A = 274727.197236
  Ma = 740908.788944
  C = 586288.004607
  D = -458265.201843

  # Dominio
  x1 = np.linspace(0, l1, 300)
  x2 = np.linspace(l1, l1 + l2, 300)
  x3 = np.linspace(l1 + l2, l1 + l2 + l3, 300)

  # Variable y para segundo y tercer tramo
  y2 = l1 + l2 + l3 - x2
  y3 = l1 + l2 + l3 - x3

  # Cortante
  V1 = A - w1 * x1
  V2 = D + C - w2 * y2
  V3 = D - w2 * y3

  # Momento
  M1 = (A * x1) - Ma - (w1 * x1 ** 2) / 2
  M2 = (D * y2) + (C * (y2 - l3)) - (w2 * (y2 ** 2) / 2)
  M3 = (D * y3) - (w2 * (y3 ** 2) / 2)

  # Crear figuras y exportar
  with PdfPages("diagramas_cortante_momento(ya_-10).pdf") as pdf:

      # --- Diagrama de Fuerza Cortante ---
      plt.figure(figsize=(10, 5))
      plt.plot(x1, V1, color="#E91E63", linewidth=2, label='V(x)')
      plt.plot(x2, V2, color="#E91E63", linewidth=2)
      plt.plot(x3, V3, color="#E91E63", linewidth=2)
      plt.fill_between(x1, V1, color="#F8BBD0", alpha=0.4)
      plt.fill_between(x2, V2, color="#F8BBD0", alpha=0.4)
      plt.fill_between(x3, V3, color="#F8BBD0", alpha=0.4)
      plt.axhline(0, color='black', linewidth=1)
      plt.title("DIAGRAMA DE FUERZA CORTANTE", fontsize=18, fontweight='bold')
      plt.xlabel("Longitud x (m)", fontsize=14)
      plt.ylabel("Cortante V(x) [N]", fontsize=14)
      plt.grid(True, linestyle='--', alpha=0.5)
      plt.legend()
      plt.tight_layout()
      plt.text(6, min(np.min(V1), np.min(V2), np.min(V3)) * 0.9, f"Generado el 18/07/2025", fontsize=8)
      pdf.savefig()
      plt.close()

      # --- Diagrama de Momento Flector ---
      plt.figure(figsize=(10, 5))
      plt.plot(x1, M1, color="#3F51B5", linewidth=2, label='M(x)')
      plt.plot(x2, M2, color="#3F51B5", linewidth=2)
      plt.plot(x3, M3, color="#3F51B5", linewidth=2)
      plt.fill_between(x1, M1, color="#C5CAE9", alpha=0.4)
      plt.fill_between(x2, M2, color="#C5CAE9", alpha=0.4)
      plt.fill_between(x3, M3, color="#C5CAE9", alpha=0.4)
      plt.axhline(0, color='black', linewidth=1)
      plt.title("DIAGRAMA DE MOMENTO FLECTOR", fontsize=18, fontweight='bold')
      plt.xlabel("Longitud x (m)", fontsize=14)
      plt.ylabel("Momento M(x) [N·m]", fontsize=14)
      plt.grid(True, linestyle='--', alpha=0.5)
      plt.legend()
      plt.tight_layout()
      plt.text(6, min(np.min(M1), np.min(M2), np.min(M3)) * 0.9, f"Generado el 18/07/2025", fontsize=8)
      pdf.savefig()
      plt.close()

  print("Listo. Diagramas exportados como 'diagramas_cortante_momento(ya_-10).pdf'")