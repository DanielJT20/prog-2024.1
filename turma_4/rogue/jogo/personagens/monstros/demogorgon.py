import random

from .monstro import Monstro

class Demogorgon(Monstro):
    def __init__(self, dificuldade):
        self.nome = "Demogorgon"
        self.vida = int(dificuldade * random.randint(80, 120))
        self.forca = int(dificuldade * random.randint(5, 25))
        print("Um Demogorgon apareceu!")
