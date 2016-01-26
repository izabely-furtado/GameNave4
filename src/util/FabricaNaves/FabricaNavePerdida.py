import random
from src.cci.Metricas import Metricas
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga


class FabricaNavePerdida(FabricaNaveInimiga.FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super().__init__('Nave Perdida', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 20
        self.municao = self.cria_municao()

    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < Metricas.lim_largura) and (self.posicao["x"] > 0):
            if aleatorio > 5:
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == Metricas.lim_largura:
            self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == 0:
            self.posicao["x"] += self.velocidade["x"]
        
        self.posicao["y"] += self.velocidade["y"]    
        self.cria_area()

    @staticmethod
    def cria_velocidade():
        return {"x": 1, "y": 1}

    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(2, 2)
