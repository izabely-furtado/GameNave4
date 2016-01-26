from src.util.FabricaNaves import FabricaNave


class FabricaNaveInimiga(FabricaNave.FabricaNave):
    def __init__(self, nome, figura_nave, figura_explosao, som):
        super(FabricaNaveInimiga, self).__init__(nome, figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 0

    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.cria_area()
