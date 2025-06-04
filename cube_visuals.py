from ursina import Entity, Vec3
from constants import COLORS_URSINA, BLACK_STICKER, U_FACE, L_FACE, F_FACE, R_FACE, B_FACE, D_FACE
from cube_logic import get_cube_data

# Variable globale pour les entités des cubies
all_cubies_entities = []

class Cubie(Entity):
    """Représente un petit cube individuel (un 'cubie') du Rubik's Cube."""
    def __init__(self, position=(0,0,0)):
        super().__init__(model=None, position=position) # Parent invisible pour les facelets
        self.logical_coords = (int(round(position[0])), int(round(position[1])), int(round(position[2])))
        
        facelet_size = 0.96 # Légèrement inférieur à 1 pour créer des interstices
        facelet_thickness = 0.05 # Épaisseur des facelets pour qu'ils soient visibles

        # Création des 6 facelets (petits cubes fins) pour ce cubie.
        # Initialement noirs, ils seront colorés par update_3d_visuals.
        # Les positions et rotations sont relatives au centre du Cubie parent.
        self.facelets = {
            'F': Entity(parent=self, model='cube', scale=(facelet_size, facelet_size, facelet_thickness), position=(0,0,0.5 - facelet_thickness/2), color=BLACK_STICKER, name=f'F_{self.logical_coords}'), # Avant (+Z)
            'B': Entity(parent=self, model='cube', scale=(facelet_size, facelet_size, facelet_thickness), position=(0,0,-(0.5 - facelet_thickness/2)), rotation_y=180, color=BLACK_STICKER, name=f'B_{self.logical_coords}'),# Arrière (-Z)
            'U': Entity(parent=self, model='cube', scale=(facelet_size, facelet_size, facelet_thickness), position=(0,0.5 - facelet_thickness/2,0), rotation_x=-90, color=BLACK_STICKER, name=f'U_{self.logical_coords}'), # Haut (+Y)
            'D': Entity(parent=self, model='cube', scale=(facelet_size, facelet_size, facelet_thickness), position=(0,-(0.5 - facelet_thickness/2),0), rotation_x=90, color=BLACK_STICKER, name=f'D_{self.logical_coords}'),  # Bas (-Y)
            'R': Entity(parent=self, model='cube', scale=(facelet_size, facelet_size, facelet_thickness), position=(0.5 - facelet_thickness/2,0,0), rotation_y=90, color=BLACK_STICKER, name=f'R_{self.logical_coords}'),  # Droite (+X)
            'L': Entity(parent=self, model='cube', scale=(facelet_size, facelet_size, facelet_thickness), position=(-(0.5 - facelet_thickness/2),0,0), rotation_y=-90, color=BLACK_STICKER, name=f'L_{self.logical_coords}')  # Gauche (-X)
        }

def create_rubiks_cube_entities():
    """Crée les 26 Entités Cubie visibles et les stocke dans all_cubies_entities."""
    global all_cubies_entities
    all_cubies_entities = []
    for x_coord in range(-1, 2):
        for y_coord in range(-1, 2):
            for z_coord in range(-1, 2):
                if x_coord == 0 and y_coord == 0 and z_coord == 0:
                    all_cubies_entities.append(None) # Placeholder pour le cubie central invisible
                    continue
                cubie_entity = Cubie(position=(x_coord, y_coord, z_coord))
                all_cubies_entities.append(cubie_entity)

def update_3d_visuals():
    """Met à jour les couleurs des facelets 3D en fonction de cube_data."""
    cube_data = get_cube_data()
    if not cube_data or not all_cubies_entities:
        print("Erreur: cube_data ou all_cubies_entities non initialisé.")
        return

    for cubie_entity in all_cubies_entities:
        if not cubie_entity: continue # Ignorer le placeholder du centre

        ix, iy, iz = cubie_entity.logical_coords

        # Réinitialiser tous les facelets en noir et cachés
        for facelet_key, facelet_obj in cubie_entity.facelets.items():
            facelet_obj.color = BLACK_STICKER
            facelet_obj.visible = False

        # Appliquer les couleurs de cube_data aux facelets visibles
        # Le mappage est crucial et doit correspondre à la définition des faces et à l'orientation des cubies.
        # ix, iy, iz vont de -1 à 1. Les indices de cube_data[FACE][row][col] vont de 0 à 2.
        
        # Face HAUT (+Y) du cubie: correspond à U_FACE de cube_data
        if iy == 1: 
            color_idx = cube_data[U_FACE][iz+1][ix+1] # row: map z, col: map x
            cubie_entity.facelets['U'].color = COLORS_URSINA[color_idx]
            cubie_entity.facelets['U'].visible = True
        # Face BAS (-Y) du cubie: correspond à D_FACE de cube_data
        if iy == -1:
            color_idx = cube_data[D_FACE][-iz+1][ix+1] # row: map -z, col: map x
            cubie_entity.facelets['D'].color = COLORS_URSINA[color_idx]
            cubie_entity.facelets['D'].visible = True
        # Face GAUCHE (-X) du cubie: correspond à L_FACE de cube_data
        if ix == -1:
            color_idx = cube_data[L_FACE][-iy+1][iz+1] # row: map -y, col: map z
            cubie_entity.facelets['L'].color = COLORS_URSINA[color_idx]
            cubie_entity.facelets['L'].visible = True
        # Face DROITE (+X) du cubie: correspond à R_FACE de cube_data
        if ix == 1:
            color_idx = cube_data[R_FACE][-iy+1][-iz+1] # row: map -y, col: map -z
            cubie_entity.facelets['R'].color = COLORS_URSINA[color_idx]
            cubie_entity.facelets['R'].visible = True
        # Face AVANT (+Z) du cubie: correspond à F_FACE de cube_data
        if iz == 1:
            color_idx = cube_data[F_FACE][-iy+1][ix+1] # row: map -y, col: map x
            cubie_entity.facelets['F'].color = COLORS_URSINA[color_idx]
            cubie_entity.facelets['F'].visible = True
        # Face ARRIÈRE (-Z) du cubie: correspond à B_FACE de cube_data
        if iz == -1:
            color_idx = cube_data[B_FACE][-iy+1][-ix+1] # row: map -y, col: map -x
            cubie_entity.facelets['B'].color = COLORS_URSINA[color_idx]
            cubie_entity.facelets['B'].visible = True 