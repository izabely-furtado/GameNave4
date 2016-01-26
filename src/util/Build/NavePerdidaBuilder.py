from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNavePerdida
from src.cgd import Path


class NavePerdidaBuilder(NaveBuilder.NaveBuilder):
    def __init__(self):
        super(NavePerdidaBuilder, self).__init__()
        self.build_dano()
        self.build_imagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()

    def build_dano(self):
        self.nave_product.set_dano(0)

    def build_imagem_nave(self):
        self.nave_product.imagem_nave = Path.get_path() + "/Imagem/Nave/Perdida.png"

    def build_imagem_explosao(self):
        self.nave_product.imagem_explosao = Path.get_path() + "/Imagem/Nave/Boss.png"

    def build_som(self):
        self.nave_product.som = Path.get_path() + "/Som/MusicNave.wav"

    def build_nave(self):
        self.nave_product.nave_fabrica = FabricaNavePerdida.FabricaNavePerdida(self.nave_product.imagem_nave,
                                                                               self.nave_product.imagem_explosao,
                                                                               self.nave_product.som)
