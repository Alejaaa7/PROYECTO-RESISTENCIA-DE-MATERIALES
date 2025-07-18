# VigaAB.py

from Vigas.viga import Viga
import math

# La primera viga: viga AB, se analiza como viga empotrada en a y con 
# voladizo en b:

class VigaAB(Viga):
  def __init__(self, l1: float, w1: float):
    self.l1 = l1
    self.w1 = w1

  def calcular_EI(self, E: float, Ii: float):
    self.EI = super().calcular_EI(E, Ii)
    return self.EI

  def Análisis_Estático(self):
    l1 = self.l1
    w1 = self.w1

    self.A = w1 * l1
    self.Ma = (w1 * l1 ** 2) / 2

    return self.A, self.Ma

  def calcular_yb_thetab(self):
    EI = self.EI
    w1 = self.w1
    A = self.A
    Ma = self.Ma
    l1 = self.l1

    sum_Pi = (A * l1 ** 3) / 6
    sum_Mi = (Ma* l1 ** 2) / 2
    sum_qi = (w1 * l1 ** 4) / 24

    yb_1 = (1 / EI) * (sum_Pi - sum_Mi - sum_qi)
    yb1 = yb_1 * 1000
    thetab1 = (1 / EI) * (sum_Pi - sum_Mi + sum_qi)
    theta_b1 = (thetab1 * 180) / math.pi

    return yb1, theta_b1