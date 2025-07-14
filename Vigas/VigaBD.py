# VigaBD.py

from Vigas.viga import Viga 

# La segunda viga: Viga BD, se analiza como viga con voladizo en b, con 
# rodillo en C y fija en D:

class VigaBD(Viga):
    def __init__(self, lt2: float, w2: float):
        super().__init__(lt2, w2)

    def calcular_EI(self, E: float, Id: float):
        self.EI = super().calcular_EI(E, Id)

        return self.EI
        
    def sumatoria_de_M(self, w2: float, l2: float, l3: float):
        # Primero se calcula la longitud total de los dos tramos, con los 
        # datos dados:
        lt2 = l2 + l3

        # Se calculan las reacciones, siguiendo los sentidos del DCL, 
        # haciendo sumatoria de momentos en d, para calcular C:

        self.C = (w2 * lt2 * lt2 / 2) / 3

        return self.C

    # Como ya se tiene C, es posible hacer la sumatoria de fuerzas en y, 
    # nuevamente con sentido positivo hacia arriba:
    def sumatoria_de_Fy(self, w2: float):
        self.D = self.C - (w2 * 5)

        return self.D
    
    def calcular_yb(self, z2, yd, theta_d, w2, p_c, p_w2):
        # p_a, p_Ma y p_w1 son los puntos de aplicación de las fuerzas
    # y el inicio de w1:
        EI = self.EI
        C = self.C
        yb2 = super().calcular_yb(EI, yd, theta_d, z2, 0, C, 0, p_c, p_w2, w2)

        return yb2
