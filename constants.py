from ursina import color

# --- Définitions des Couleurs (avec codes RGB explicites) ---
COLORS_URSINA = {
    0: color.rgb(255, 255, 255), # WHITE
    1: color.rgb(255, 255, 0),   # YELLOW
    2: color.rgb(0, 0, 255),     # BLUE
    3: color.rgb(0, 255, 0),     # GREEN (équivalent à lime)
    4: color.rgb(255, 0, 0),     # RED
    5: color.rgb(128, 0, 128)  # PURPLE (était ORANGE)
}
BLACK_STICKER = color.dark_gray # Pour les faces internes/non visibles des cubies

# --- Index des Faces (cohérent avec les versions précédentes) ---
U_FACE = 0 # Haut (Blanc par défaut)
L_FACE = 1 # Gauche (Violet par défaut)
F_FACE = 2 # Avant (Vert par défaut)
R_FACE = 3 # Droite (Rouge par défaut)
B_FACE = 4 # Arrière (Bleu par défaut)
D_FACE = 5 # Bas (Jaune par défaut)

# Configuration de l'interface utilisateur
BUTTON_SCALE = (.18, .04)
BUTTON_COLOR = color.azure.tint(-0.2)
TEXT_COLOR = color.black
BUTTON_COLUMN_X = -0.85
BUTTON_START_Y = 0.45
GROUP_SPACING_Y = 0.15
BUTTON_IN_GROUP_SPACING_Y = 0.05

# Configuration des mouvements pour l'UI
MOVE_GROUPS_CONFIG = [
    ("Avant (F)", ["F", "F_PRIME"]), 
    ("Haut (U)", ["U", "U_PRIME"]),
    ("Droite (R)", ["R", "R_PRIME"]), 
    ("Gauche (L)", ["L", "L_PRIME"]),
    ("Arrière (B)", ["B", "B_PRIME"]), 
    ("Bas (D)", ["D", "D_PRIME"]),
]

# Configuration de l'application
APP_TITLE = "Rubik's Cube 3D Python (Ursina)"
APP_SIZE = (1000, 700)
CAMERA_INITIAL_POSITION = (7, 7, -20)
SCRAMBLE_MOVES_COUNT = 25 