# Viga.py

# Aquí van las vigas, en las que fue dividida la viga dada, para un mejor
# entendimiento.

class Viga:
    def __init__(self, l: float, w: float):
        self.l = l
        self.w = w

    def sumatoria_de_Fy(self):
        raise NotImplementedError
    
    def sumatoria_de_M(self):
        raise NotImplementedError
    
    def calcular_yb(self, EI, y0, theta_0, z, Mi, Pi, ai, bi, ci, qi):
        sum_Mi = (Mi * ((z - ai) ** 2)) / 2
        sum_Pi = (Pi * ((z - bi) ** 3)) / 6
        sum_qi = (qi * ((z - ci) ** 4)) / 24

    # Se escribe la ecuación universal de la curva elástica, con Mi y w 
    # negativos porque en análisis previos se determinó su dirección, 
    # entonces se escriben así desde la ecuación para facilitar el código
    # y las entradas de los datos.
        yb = (1 / EI) * ((EI * y0) + (EI * theta_0 * z) - sum_Mi + sum_Pi - sum_qi)
    
        return yb
    
    def calcular_EI(self, E: float, I: float):
        return E * I
    
