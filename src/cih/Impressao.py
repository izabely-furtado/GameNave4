#!/usr/local/bin/python
import pygame
from src.cci.Metricas import Metricas
from src.cgd import Path

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 2.1
# Author:      Gislaine
# Created:     09/29/2015
# Copyright:   (c) Gislaine  e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine  e Izabely'

pygame.init()
pygame.font.init()


class Impressao(object):

    def __init__(self):
        self.telao = self.imprime_tela_inicial()
        self.figura = None

    @staticmethod
    def imprime_instrucao():
        titulo = " - Nave maluca -Instrução"

        tela = pygame.display.set_mode((Metricas.largura, Metricas.altura), 0, 32)
        pygame.display.set_caption(titulo)
        imagem = pygame.image.load(Path.get_path() + "/Imagem/Tela/tela_espaco5.jpg").convert_alpha()

        tela.blit(imagem, (0, 0))

        return tela

    @staticmethod
    def imprime_tela_inicial():

        titulo = " - Nave maluca - Let's Play"
        tela = pygame.display.set_mode((Metricas.largura, Metricas.altura), 0, 32)
        pygame.display.set_caption(titulo)
        caminho = Path.get_path() + "/Imagem/Tela/tela_espaco2.jpg"
        imagem = pygame.image.load(caminho).convert()

        tela.blit(imagem, (0, 0))

        font_name = pygame.font.get_default_font()
        game_font = pygame.font.SysFont(font_name, 25)
        text = game_font.render("Pontuação: "+"0000", True, (255, 100, 255))
        tela.blit(text, (20, 10))

        return tela

    @staticmethod
    def start_tela_menu():

        titulo = " - Nave maluca - Menu"

        tela = pygame.display.set_mode((Metricas.largura, Metricas.altura), 0, 32)
        pygame.display.set_caption(titulo)
        caminho = Path.get_path() + "/Imagem/Tela/tela_espaco2.jpg"
        imagem = pygame.image.load(caminho).convert()

        tela.blit(imagem, (0, 0))

        pygame.display.update()

        tela.blit(imagem, (10, 10))

        pygame.display.update()

        return tela

    @staticmethod
    def imprime_texto_fim():

        tela = pygame.display.set_mode((Metricas.largura, Metricas.altura), 0, 32)
        titulo = " - Nave  - Game over"
        pygame.display.set_caption(titulo)
        caminho = Path.get_path() + "/Imagem/Tela/tela_menu5.jpg"
        imagem = pygame.image.load(caminho).convert()
        tela.blit(imagem, (0, 0))
        font_name = pygame.font.get_default_font()
        game_font = pygame.font.SysFont(font_name, 70)

        text = game_font.render("GAME OVER", True, (255, 0, 0))
        tela.blit(text, (510, 175))

        return tela
