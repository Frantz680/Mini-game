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
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # Dessiner le groupe de calques
        self.groupCalque = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        # On rajoute un calque avec le joueur
        self.groupCalque.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up
        elif pressed[pygame.K_DOWN]:
            self.player.move_down
        elif pressed[pygame.K_LEFT]:
            self.player.move_left
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right

    def game_lauch(self):
        """
        game launch
        """

        clock = pygame.time.Clock()

        loop_reception = 1

        # Loop reception
        while loop_reception:  

            self.handle_input()
            self.groupCalque.update()
            self.groupCalque.center(self.player.rect.center)
            self.groupCalque.draw(self.screen)

            # Screen refresh
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    loop_reception = 0

            clock.tick(60)
