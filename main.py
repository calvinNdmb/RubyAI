from ursina import *
from constants import APP_TITLE, APP_SIZE, CAMERA_INITIAL_POSITION
from cube_logic import init_cube_data
from cube_visuals import create_rubiks_cube_entities, update_3d_visuals
from ui import create_ui

def setup_camera():
    """Configure la caméra pour une vue optimale du cube."""
    EditorCamera(rotation_speed=200, zoom_speed=1, pan_speed=(0.5,0.5))
    camera.position = CAMERA_INITIAL_POSITION
    camera.look_at(Vec3(0,0,0))

def setup_lighting():
    """Configure l'éclairage de la scène."""
    AmbientLight(color=color.rgba(150, 150, 150, 0.8))
    DirectionalLight(color=color.rgba(200,200,200,1), direction=(-1,1,1), shadows=False)
    DirectionalLight(color=color.rgba(100,100,100,1), direction=(1,-1,-1), shadows=False)

def main():
    """Point d'entrée principal de l'application."""
    # Initialisation de l'application Ursina
    app = Ursina(title=APP_TITLE, borderless=False, size=APP_SIZE)

    # Initialisation des données du cube
    init_cube_data()
    
    # Création des entités 3D
    create_rubiks_cube_entities()
    
    # Mise à jour initiale des visuels
    update_3d_visuals()

    # Configuration de la caméra et de l'éclairage
    setup_camera()
    setup_lighting()
    
    # Création de l'interface utilisateur
    create_ui()

    # Lancement de l'application
    app.run()

if __name__ == '__main__':
    main() 