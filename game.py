import pygame
import pytmx
import pyscroll

from pygame.locals import RESIZABLE, QUIT, KEYDOWN, K_F1, K_F2, K_F3, \
    K_DOWN, K_UP, K_LEFT, K_RIGHT

from constants import WINDOW_H, WINDOW_L
from player import Player

class Game:

    def __init__(self):

        pygame.init()

        # Opening the pygame and Title window
        self.screen = pygame.display.set_mode((WINDOW_L, WINDOW_H), RESIZABLE)

        # Title
        pygame.display.set_caption("Sauvez le monde")

        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map/map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Generer un joueur
        self.player = Player()

        # Dessiner le groupe de calques
        self.groupCalque = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        # On rajoute un calque avec le joueur
        self.groupCalque.add(self.player)

    def game_lauch(self):
        """
        game launch
        """

        loop_reception = 1

        # Loop reception
        while loop_reception:  

            self.groupCalque.draw(self.screen)

            # Screen refresh
            pygame.display.flip()
            pygame.key.set_repeat(400, 30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    loop_reception = 0
