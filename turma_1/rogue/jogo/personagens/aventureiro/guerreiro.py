import random

from .aventureiro import Aventureiro
from .aventureiro import XP_POR_NIVEL 


class Guerreiro(Aventureiro):
    def __init__(self):
        super().__init__()
        self.xp = self.xp
        self.xp = self.nivel
        self.xp_max = self.xp_max
        self.vida = random.randint(90, 110)
        self.defesa = random.randint(9, 17)
        self.forca = random.randint(15, 25)
        self.vida_max = self.vida
