# VigaAB.py

from Vigas.viga import Viga

# La primera viga: viga AB, se analiza como viga empotrada en a y con 
# voladizo en b:

class VigaAB(Viga):
    def __init__(self, l1: float, w1: float):
        super().__init__(l1, w1)
        
    def calcular_EI(self, E: float, Ii: float):
        self.EI = super().calcular_EI(E, Ii)
        return self.EI

    # Ahora, respetando los sentidos dibujados en el DCL, se hace una 
    # sumatoria de fuerzas en y, con sentido positivo hacia arriba:
    def sumatoria_de_Fy(self, w1: float, l1: float): # para calcular el valor de A
        self.A = w1 * l1 
        return self.A
    
    # para calcular del valor del momento en A, se hace sumatoria de 
    # momentos en a (positivo en sentido antihorario): 
    def sumatoria_de_M(self, w1, l1): 
        lw = l1 / 2 # se calcula el punto de aplicación de w
        self.Ma = w1 * l1 * lw 
        return self.Ma
    
    def calcular_yb(self, z1, ya, theta_a, w1, p_a, p_Ma, p_w1):
    # p_a, p_Ma y p_w1 son los puntos de aplicación de las fuerzas
    # y el inicio de w1:
        EI = self.EI
        A = self.A
        Ma = self.Ma
        yb1 = super().calcular_yb(EI, ya, theta_a, z1, Ma, A, p_Ma, p_a, p_w1, w1)

        return yb1
