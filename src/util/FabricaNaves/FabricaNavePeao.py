from src.cci.Metricas import Metricas
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga

class FabricaNavePeao(FabricaNaveInimiga.FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super(FabricaNavePeao, self).__init__('Nave Peao', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 10

    def move(self):
        if self.posicao["direcao"] == "DIREITA":
            if self.posicao["x"] < Metricas.lim_largura:
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["direcao"] = "ESQUERDA"
                self.posicao["y"] += self.velocidade["y"] 
        elif self.posicao["direcao"] == "ESQUERDA":
            if self.posicao["x"] > 0:
                self.posicao["x"] -= self.velocidade["x"]
            else:
                self.posicao["direcao"] = "DIREITA"
                self.posicao["y"] += self.velocidade["y"] 
        
        self.cria_area()

    @staticmethod
    def cria_velocidade():
        return {"x": 1, "y": 1}

    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(1, 1)
