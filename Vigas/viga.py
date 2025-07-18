# Viga.py

# Aquí van las vigas, en las que fue dividida la viga dada, para un mejor
# entendimiento.

import math

# viga

class Viga:
  def __init__(self, l: float, w: float):
    self.l = l
    self.w = w

  def sumatoria_de_Fy(self):
    raise NotImplementedError

  def sumatoria_de_M(self):
    raise NotImplementedError

  def calcular_yb(self):
    raise NotImplementedError

  def calcular_theta_b(self):
    raise NotImplementedError

  def calcular_EI(self, E: float, I: float):
    return E * I