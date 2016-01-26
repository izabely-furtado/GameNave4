#!/usr/local/bin/python
import random
import pygame
import sys
from pygame.rect import Rect
from src.cci.Metricas import Metricas
from src.cgd import Path
# -------------------------------------------------------------------------------
# Name:        Nave Maluca 2.1
# Author:      Gislaine e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine  e Izabely'

pygame.init()


class Municao(object):
    def __init__(self, pos):
        self.figura = self.cria_figura()
        self.posicao = self.cria_posicao(pos)
        self.velocidade = self.cria_velocidade()
        self.colisao = False
        self.ativo = True
        self.area = self.start_area()

    @staticmethod
    def cria_figura():
        aleatorio = random.randint(0, 10)

        if 0 <= aleatorio <= 3:
            figura = pygame.image.load(Path.get_path() + "/Imagem/Tiro/tiro1.png").convert_alpha()
        elif 4 <= aleatorio <= 6:
            figura = pygame.image.load(Path.get_path() + "/Imagem/Tiro/tiro2.png").convert_alpha()
        else:
            figura = pygame.image.load(Path.get_path() + "/Imagem/Tiro/tiro3.png").convert_alpha()

        return figura

    @staticmethod
    def cria_posicao(pos):
        posicao = {'x':0, 'y':0}
        print("cria posicao", pos)
        if (pos['x'] < Metricas.lim_largura ) and (pos['y'] < Metricas.lim_altura ):
            posicao = {'x': pos['x'] + 30, "y": pos['y'] + 15}
        else:
            print("Posição invalida", sys.exc_info()[0])

        return posicao

    @staticmethod
    def cria_velocidade():
        return {"x": 0, "y": 20}

    def start_area(self):
        self.area = Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())

        return self.area

    def get_area(self):
        return self.area

    def atira(self):
        self.posicao["x"] -= self.velocidade["x"]
        self.posicao["y"] -= self.velocidade["y"]
        self.start_area()

    def get_posicao_y(self):
        return self.posicao["y"]

    def get_posicao_x(self):
        return self.posicao["x"]

    def set_posicao_y(self, valor):
        self.posicao["y"] = valor

    def set_posicao_x(self, valor):
        self.posicao["x"] = valor