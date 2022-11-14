from dataclasses import dataclass
import pygame, pytmx, pyscroll

@dataclass
class Map:
    name: str
    walls: list()
    groupCalque: pyscroll.PyscrollGroup


class MapManager:

    def __init__(self, screen, player):
        self.maps = dict() # "my_house" -> Map("my_house", walls, groups)
        self.screen = screen
        self.player = player
        self.current_map = "map"

        self.register_map("map")
        self.register_map("my_house")

    def register_map(self, name):
        # Charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Generer un joueur
        # player_position = tmx_data.get_object_by_name("spawn_house")
        # self.player = Player(player_position.x, player_position.y - 20)

        # Définir une liste pour les collision
        walls = []

        for object in tmx_data.objects:
            if object.name == 'collision':
                walls.append(pygame.Rect(object.x, object.y, object.width, object.height))

        # Dessiner le groupe de calques
        groupCalque = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        # On rajoute un calque avec le joueur
        groupCalque.add(self.player)

        #Créer un objet Map
        self.maps[name] = Map(name, walls, groupCalque)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().groupCalque

    def get_walls(self):
        return self.get_map().walls

    def draw(self):
        # Elle dessine et centre
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()