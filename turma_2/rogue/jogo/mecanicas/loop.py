from . import mecanicas
from .inputbox import ler_texto

from ..gui.tela import Tela

from ..personagens.aventureiro import Aventureiro
from ..personagens.tesouro import Tesouro
from ..personagens.npc import NPC
from ..personagens.inimigos.boss import Boss

import pygame

def determinar_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

def executar():
    nome = ler_texto()
    aventureiro = Aventureiro(nome)
    tesouro = Tesouro()
    npc = NPC(tesouro)
    tela = Tela()

    jogo_rodando = True
    while jogo_rodando:
        # Análise dos eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False

            if evento.type == pygame.KEYUP:
                # Processamento do jogo
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False

                if teclas[pygame.K_SPACE]:
                    mecanicas.conversar(aventureiro, npc)
                else:
                    if not mecanicas.movimentar(aventureiro, determinar_direcao(teclas), npc):
                        jogo_rodando = False

                    if aventureiro.posicao == tesouro.posicao:
                        boss = Boss()
                        if mecanicas.iniciar_combate(aventureiro, boss):
                            aventureiro.status = f"Parabéns! Você derrotou {boss.nome} e encontrou o tesouro!"
                        else:
                            aventureiro.status = f"Você foi derrotado por {boss.nome}! Game over..."
                        jogo_rodando = False

        # Renderização na tela
        tela.renderizar(aventureiro, tesouro, npc)
        pygame.time.Clock().tick(60)
