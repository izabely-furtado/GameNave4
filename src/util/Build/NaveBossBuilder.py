from src.cgd import Path
from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNaveBoss


class NaveBossBuilder(NaveBuilder.NaveBuilder):
    def __init__(self):
        super(NaveBossBuilder, self).__init__()
        self.build_dano()
        self.build_imagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()

    def build_dano(self):
        self.nave_product.dano = 0

    def build_imagem_nave(self):
        self.nave_product.imagem_nave = Path.get_path() + 'Imagem/Nave/NaveBoss.png'

    def build_imagem_explosao(self):
        self.nave_product.imagem_explosao = Path.get_path() + 'Imagem/Nave/NaveExplode.png'

    def build_som(self):
        self.nave_product.som = Path.get_path() + 'Som/MusicNave.wav'

    def build_nave(self):
        self.nave_product.nave_fabrica = FabricaNaveBoss.FabricaNaveBoss(self.nave_product.imagem_nave,
                                                                         self.nave_product.imagem_explosao,
                                                                         self.nave_product.som)
