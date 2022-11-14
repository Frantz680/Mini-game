import pygame
import pytmx
import pyscroll

from pygame.locals import RESIZABLE, QUIT, KEYDOWN, K_F1, K_F2, K_F3, \
    K_DOWN, K_UP, K_LEFT, K_RIGHT

from constants import WINDOW_H, WINDOW_L
from player import Player
from map import MapManager

class Game:

    def __init__(self):

        pygame.init()

        # Opening the pygame and Title window
        self.screen = pygame.display.set_mode((WINDOW_L, WINDOW_H), RESIZABLE)

        # Title
        pygame.display.set_caption("Sauvez le monde")

        # # Charger la carte (tmx)
        # tmx_data = pytmx.util_pygame.load_pygame('map/map.tmx')
        # map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # map_layer.zoom = 2
        # self.map = "world"

        # Generer un joueur
        # player_position = tmx_data.get_object_by_name("player")
        self.player = Player(0,0)
        self.map_manager = MapManager(self.screen, self.player)
        # # Définir une liste pour les collision
        # self.walls = []

        # for object in tmx_data.objects:
        #     if object.name == 'collision':
        #         self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))

        # # Dessiner le groupe de calques
        # self.groupCalque = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        # # On rajoute un calque avec le joueur
        # self.groupCalque.add(self.player)

        # # Definir entrer maison
        # enter_house = tmx_data.get_object_by_name("enter_house")
        # self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.position[1] -= self.player.speed
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.position[1] += self.player.speed
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.position[0] -= self.player.speed
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.position[0] += self.player.speed
            self.player.change_animation('right')

    # def switch_house(self):
    #     # Charger la carte (tmx)
    #     tmx_data = pytmx.util_pygame.load_pygame('map/my_house.tmx')
    #     map_data = pyscroll.data.TiledMapData(tmx_data)
    #     map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
    #     map_layer.zoom = 2

    #     # Generer un joueur
    #     player_position = tmx_data.get_object_by_name("spawn_house")
    #     self.player = Player(player_position.x, player_position.y - 20)

    #     # Définir une liste pour les collision
    #     self.walls = []

    #     for object in tmx_data.objects:
    #         if object.name == 'collision':
    #             self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))

    #     # Dessiner le groupe de calques
    #     self.groupCalque = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
    #     # On rajoute un calque avec le joueur
    #     self.groupCalque.add(self.player)

    #     # Definir la sortie de la maison
    #     enter_house = tmx_data.get_object_by_name("exit_house")
    #     self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    # def exit_house(self):
    #     # Charger la carte (tmx)
    #     tmx_data = pytmx.util_pygame.load_pygame('map/map.tmx')
    #     map_data = pyscroll.data.TiledMapData(tmx_data)
    #     map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
    #     map_layer.zoom = 2

    #     # Generer un joueur
    #     player_position = tmx_data.get_object_by_name("enter_house_exit")
    #     self.player = Player(player_position.x, player_position.y )

    #     # Définir une liste pour les collision
    #     self.walls = []

    #     for object in tmx_data.objects:
    #         if object.name == 'collision':
    #             self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))

    #     # Dessiner le groupe de calques
    #     self.groupCalque = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
    #     # On rajoute un calque avec le joueur
    #     self.groupCalque.add(self.player)

    #     # Definir l'entrer de la maison
    #     enter_house = tmx_data.get_object_by_name("enter_house")
    #     self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    def update_position(self):
        self.map_manager.update()

        # On vérifier l'entrer dans la maison
        # if self.map == "world" and self.player.feet.colliderect(self.enter_house_rect):
        #     self.switch_house()
        #     self.map = 'my_house'

        # # On vérifie la sortir de la maison
        # if self.map == "my_house" and self.player.feet.colliderect(self.enter_house_rect):
        #     self.exit_house()
        #     self.map = "world"

        # # On vérifier si le joueur rentre en colision
        # for sprite in self.groupCalque.sprites():
        #     if sprite.feet.collidelist(self.walls) > -1:
        #         sprite.move_back()

    def game_lauch(self):
        """
        game launch
        """

        clock = pygame.time.Clock()

        loop_reception = 1

        # Loop reception
        while loop_reception:  

            self.player.location()
            self.handle_input()
            self.update_position()
            self.map_manager.draw()

            # Screen refresh
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    loop_reception = 0

            # 60 image par seconde
            clock.tick(60)
