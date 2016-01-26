import random
from src.cci.Metricas import Metricas
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga


class FabricaNaveBoss(FabricaNaveInimiga.FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super(FabricaNaveBoss, self).__init__('BOSS!!', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 200
        self.municao = self.cria_municao()

    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < Metricas.lim_largura - aleatorio) and (self.posicao["x"] > 0 + aleatorio):
            if aleatorio < 5:
                self.posicao["x"] += self.velocidade["x"] + aleatorio
            else:
                self.posicao["x"] -= self.velocidade["x"] - aleatorio
        elif self.posicao["x"] == Metricas.lim_largura:
            self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == 0:
            self.posicao["x"] += self.velocidade["x"]
        
        if (self.posicao["y"] < Metricas.lim_altura - aleatorio) and (self.posicao["y"] > 0 + aleatorio):
            if aleatorio < 5:
                if self.posicao["direcao"] != "ABAIXO":
                    self.posicao["y"] += self.velocidade["y"] + aleatorio
                    self.posicao["direcao"] = "ABAIXO"
                else:
                    self.posicao["y"] -= self.velocidade["y"] - aleatorio
                    self.posicao["direcao"] = "ACIMA"

        self.cria_area()

    @staticmethod
    def cria_velocidade():
        return {"x": 1, "y": 1}

    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(10, 4)
