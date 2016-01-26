from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNave


class FabricaNaveJogador(FabricaNave.FabricaNave):
    def __init__(self, nome, figura_nave, figura_explosao, som):
        super().__init__(nome, figura_nave, figura_explosao, som)
        self.tempoMissel = 0
        self.municao = self.cria_municao()

    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.cria_area()

    @staticmethod
    def cria_velocidade():
        return {"x": 2, "y": 2}

    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(10, 2)
