from jogo.gui.tela import Tela

from . import movimento
from . import inputbox
from . import buttonbox

from jogo.personagens.monstros.boss import Boss
from jogo.personagens.aventureiro.aventureiro import Aventureiro
from jogo.personagens.aventureiro.guerreiro import Guerreiro
from jogo.personagens.aventureiro.tank import Tank
from jogo.personagens.tesouro import Tesouro

import pygame

def jogo():
    tesouro = Tesouro()

    nome = inputbox.ler_texto("Informe o seu nome:")
    classe = buttonbox.selecionar_classe("Clique na classe desejada:")

    match classe:
        case "Aventureiro":
            jogador = Aventureiro()
        case "Guerreiro":
            jogador = Guerreiro()
        case "Tank":
            jogador = Tank()

    jogador.nome = nome
    print(f"Saudações, {jogador.nome}! Boa sorte!")

    tela = Tela()

    mensagem_combate = ""
    jogo_acabou = False
    while not jogo_acabou:
        # Controlar os eventos
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    return

                if teclas[pygame.K_z]:
                    jogador.mudar_cor()
                elif teclas[pygame.K_x]:
                    jogador.mudar_char()
                elif teclas[pygame.K_KP_PLUS]:
                    jogador.aumentar_dificuldade()
                elif teclas[pygame.K_KP_MINUS]:
                    jogador.diminuir_dificuldade()
                else:
                    # Executar as ações do jogo
                    resultado, nome_monstro = movimento.movimentar(jogador, teclas)
                    if resultado == 0:
                        mensagem_combate = f"Você foi derrotado por {nome_monstro}..."
                        jogo_acabou = True
                    elif resultado == 1:
                        mensagem_combate = f"{nome_monstro} foi derrotado!"
                    else:
                        mensagem_combate = "Você não encontrou nada"

                    if jogador.posicao == tesouro.posicao:
                        boss = Boss(jogador.dificuldade)
                        if movimento.iniciar_combate(jogador, boss):
                            mensagem_combate = f"Parabéns, {jogador.nome}, você encontrou o tesouro!"
                        else:
                            mensagem_combate = f"Você foi derrotado pelo chefão... =("

                        jogo_acabou = True

        # Desenho na tela
        tela.renderizar(jogador, tesouro, mensagem_combate)

        # Chamar o relógio interno do jogo
        pygame.time.Clock().tick(60)
