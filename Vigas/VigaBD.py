# VigaBD.py

from Vigas.viga import Viga 
import math

# La segunda viga: Viga BD, se analiza como viga con voladizo en b, con 
# rodillo en c y fija en d:

class VigaBD(Viga):
  def __init__(self, l2: float, l3: float, w2: float):
    self.l2 = l2
    self.l3 = l3
    self.w2 = w2

  def calcular_EI(self, E: float, Id: float):
    self.EI = super().calcular_EI(E, Id)
    return self.EI

  def Análisis_Estático(self):
    w2 = self.w2
    l4 = self.l2 + self.l3
    l3 = self.l3

    self.C = (w2 * (l4 ** 2)) / (2 * l3)
    self.D = (w2 * l4) - self.C

    return self.C, self.D

  def calcular_yb_thetab(self):
    EI = self.EI
    w2 = self.w2
    C = self.C
    D = self.D
    l3 = self.l3
    l2 = self.l2
    l4 = l3 + l2

    theta_d = (1 / EI) * (((w2 * (l3 ** 4)) / 24) + ((D * (l3 ** 3)) / 6))

    yb_2 = (1 / EI) * ((EI * theta_d * l4) + ((C * ((l4 - l3) ** 3)) / 6) - \
     ((w2 * (l4 ** 4)) / 24) + ((D * (l4 ** 3)) / 6))

    yb2 = yb_2 * 1000

    thetab2 = (1 / EI) * ((EI * theta_d) + ((C * ((l4 - l3) ** 2)) / 2) + \
     ((D * (l4 ** 2)) / 2) - ((w2 * (l4 ** 3)) / 6))

    theta_b2 = (thetab2 * 180) / math.pi

    return yb2, theta_b2
