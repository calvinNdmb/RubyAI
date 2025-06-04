from constants import U_FACE, L_FACE, F_FACE, R_FACE, B_FACE, D_FACE

# Variable globale pour les données du cube
cube_data = []

def init_cube_data():
    """Initialise la structure de données cube_data avec un cube résolu."""
    global cube_data
    # La logique de mouvement opère sur les indices (0-5), 
    # la visualisation utilise COLORS_URSINA[indice]
    temp_data_indices = [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  # U_FACE
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],  # L_FACE (VIOLET)
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],  # F_FACE
        [[4, 4, 4], [4, 4, 4], [4, 4, 4]],  # R_FACE
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # B_FACE
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # D_FACE
    ]
    cube_data = temp_data_indices

def deep_copy_face(face_array):
    """Crée une copie profonde d'une face (liste de listes)."""
    return [row[:] for row in face_array]

def rotate_face_array_clockwise(face_array):
    """Fait pivoter une matrice 3x3 représentant une face dans le sens horaire."""
    N = 3
    new_face = [[None for _ in range(N)] for _ in range(N)]
    for r_idx in range(N):
        for c_idx in range(N):
            new_face[c_idx][N - 1 - r_idx] = face_array[r_idx][c_idx]
    return new_face

def rotate_face_array_counter_clockwise(face_array):
    """Fait pivoter une matrice 3x3 représentant une face dans le sens anti-horaire."""
    N = 3
    new_face = [[None for _ in range(N)] for _ in range(N)]
    for r_idx in range(N):
        for c_idx in range(N):
            new_face[N - 1 - c_idx][r_idx] = face_array[r_idx][c_idx]
    return new_face

# --- Fonctions de Logique de Mouvement (modifient cube_data) ---
def move_F_logic():
    global cube_data
    cube_data[F_FACE] = rotate_face_array_clockwise(cube_data[F_FACE])
    temp_strip = [cube_data[U_FACE][2][0], cube_data[U_FACE][2][1], cube_data[U_FACE][2][2]]
    for i in range(3): cube_data[U_FACE][2][i] = cube_data[L_FACE][2-i][2]
    for i in range(3): cube_data[L_FACE][i][2] = cube_data[D_FACE][0][i]
    for i in range(3): cube_data[D_FACE][0][i] = cube_data[R_FACE][2-i][0]
    for i in range(3): cube_data[R_FACE][i][0] = temp_strip[i]

def move_F_prime_logic():
    global cube_data
    cube_data[F_FACE] = rotate_face_array_counter_clockwise(cube_data[F_FACE])
    temp_strip = [cube_data[U_FACE][2][0], cube_data[U_FACE][2][1], cube_data[U_FACE][2][2]]
    for i in range(3): cube_data[U_FACE][2][i] = cube_data[R_FACE][i][0]
    for i in range(3): cube_data[R_FACE][i][0] = cube_data[D_FACE][0][2-i]
    for i in range(3): cube_data[D_FACE][0][i] = cube_data[L_FACE][i][2]
    for i in range(3): cube_data[L_FACE][2-i][2] = temp_strip[i]

def move_U_logic():
    global cube_data
    cube_data[U_FACE] = rotate_face_array_clockwise(cube_data[U_FACE])
    temp_strip = deep_copy_face(cube_data[F_FACE])[0]
    for i in range(3): cube_data[F_FACE][0][i] = cube_data[R_FACE][0][i]
    for i in range(3): cube_data[R_FACE][0][i] = cube_data[B_FACE][0][i]
    for i in range(3): cube_data[B_FACE][0][i] = cube_data[L_FACE][0][i]
    for i in range(3): cube_data[L_FACE][0][i] = temp_strip[i]

def move_U_prime_logic():
    global cube_data
    cube_data[U_FACE] = rotate_face_array_counter_clockwise(cube_data[U_FACE])
    temp_strip = deep_copy_face(cube_data[F_FACE])[0]
    for i in range(3): cube_data[F_FACE][0][i] = cube_data[L_FACE][0][i]
    for i in range(3): cube_data[L_FACE][0][i] = cube_data[B_FACE][0][i]
    for i in range(3): cube_data[B_FACE][0][i] = cube_data[R_FACE][0][i]
    for i in range(3): cube_data[R_FACE][0][i] = temp_strip[i]

def move_D_logic():
    global cube_data
    cube_data[D_FACE] = rotate_face_array_clockwise(cube_data[D_FACE])
    temp_strip = deep_copy_face(cube_data[F_FACE])[2]
    for i in range(3): cube_data[F_FACE][2][i] = cube_data[L_FACE][2][i]
    for i in range(3): cube_data[L_FACE][2][i] = cube_data[B_FACE][2][i]
    for i in range(3): cube_data[B_FACE][2][i] = cube_data[R_FACE][2][i]
    for i in range(3): cube_data[R_FACE][2][i] = temp_strip[i]

def move_D_prime_logic():
    global cube_data
    cube_data[D_FACE] = rotate_face_array_counter_clockwise(cube_data[D_FACE])
    temp_strip = deep_copy_face(cube_data[F_FACE])[2]
    for i in range(3): cube_data[F_FACE][2][i] = cube_data[R_FACE][2][i]
    for i in range(3): cube_data[R_FACE][2][i] = cube_data[B_FACE][2][i]
    for i in range(3): cube_data[B_FACE][2][i] = cube_data[L_FACE][2][i]
    for i in range(3): cube_data[L_FACE][2][i] = temp_strip[i]

def move_L_logic():
    global cube_data
    cube_data[L_FACE] = rotate_face_array_clockwise(cube_data[L_FACE])
    temp_strip = [cube_data[U_FACE][0][0], cube_data[U_FACE][1][0], cube_data[U_FACE][2][0]]
    for i in range(3): cube_data[U_FACE][i][0] = cube_data[B_FACE][2-i][2]
    for i in range(3): cube_data[B_FACE][i][2] = cube_data[D_FACE][2-i][0]
    for i in range(3): cube_data[D_FACE][i][0] = cube_data[F_FACE][i][0]
    for i in range(3): cube_data[F_FACE][i][0] = temp_strip[i]

def move_L_prime_logic():
    global cube_data
    cube_data[L_FACE] = rotate_face_array_counter_clockwise(cube_data[L_FACE])
    temp_strip = [cube_data[U_FACE][0][0], cube_data[U_FACE][1][0], cube_data[U_FACE][2][0]]
    for i in range(3): cube_data[U_FACE][i][0] = cube_data[F_FACE][i][0]
    for i in range(3): cube_data[F_FACE][i][0] = cube_data[D_FACE][i][0]
    for i in range(3): cube_data[D_FACE][i][0] = cube_data[B_FACE][2-i][2]
    for i in range(3): cube_data[B_FACE][2-i][2] = temp_strip[i]

def move_R_logic():
    global cube_data
    cube_data[R_FACE] = rotate_face_array_clockwise(cube_data[R_FACE])
    temp_strip = [cube_data[U_FACE][0][2], cube_data[U_FACE][1][2], cube_data[U_FACE][2][2]]
    for i in range(3): cube_data[U_FACE][i][2] = cube_data[F_FACE][i][2]
    for i in range(3): cube_data[F_FACE][i][2] = cube_data[D_FACE][i][2]
    for i in range(3): cube_data[D_FACE][i][2] = cube_data[B_FACE][2-i][0]
    for i in range(3): cube_data[B_FACE][2-i][0] = temp_strip[i]

def move_R_prime_logic():
    global cube_data
    cube_data[R_FACE] = rotate_face_array_counter_clockwise(cube_data[R_FACE])
    temp_strip = [cube_data[U_FACE][0][2], cube_data[U_FACE][1][2], cube_data[U_FACE][2][2]]
    for i in range(3): cube_data[U_FACE][i][2] = cube_data[B_FACE][2-i][0]
    for i in range(3): cube_data[B_FACE][2-i][0] = cube_data[D_FACE][i][2]
    for i in range(3): cube_data[D_FACE][i][2] = cube_data[F_FACE][i][2]
    for i in range(3): cube_data[F_FACE][i][2] = temp_strip[i]

def move_B_logic():
    global cube_data
    cube_data[B_FACE] = rotate_face_array_clockwise(cube_data[B_FACE])
    temp_strip = [cube_data[U_FACE][0][0], cube_data[U_FACE][0][1], cube_data[U_FACE][0][2]]
    for i in range(3): cube_data[U_FACE][0][i] = cube_data[R_FACE][i][2]
    for i in range(3): cube_data[R_FACE][i][2] = cube_data[D_FACE][2][2-i]
    for i in range(3): cube_data[D_FACE][2][i] = cube_data[L_FACE][i][0]
    for i in range(3): cube_data[L_FACE][2-i][0] = temp_strip[i]

def move_B_prime_logic():
    global cube_data
    cube_data[B_FACE] = rotate_face_array_counter_clockwise(cube_data[B_FACE])
    temp_strip = [cube_data[U_FACE][0][0], cube_data[U_FACE][0][1], cube_data[U_FACE][0][2]]
    for i in range(3): cube_data[U_FACE][0][i] = cube_data[L_FACE][2-i][0]
    for i in range(3): cube_data[L_FACE][2-i][0] = cube_data[D_FACE][2][i]
    for i in range(3): cube_data[D_FACE][2][i] = cube_data[R_FACE][2-i][2]
    for i in range(3): cube_data[R_FACE][i][2] = temp_strip[2-i]

# Dictionnaire des fonctions de mouvement
MOVE_FUNCTIONS = {
    "F": move_F_logic, "F_PRIME": move_F_prime_logic,
    "U": move_U_logic, "U_PRIME": move_U_prime_logic,
    "D": move_D_logic, "D_PRIME": move_D_prime_logic,
    "L": move_L_logic, "L_PRIME": move_L_prime_logic,
    "R": move_R_logic, "R_PRIME": move_R_prime_logic,
    "B": move_B_logic, "B_PRIME": move_B_prime_logic,
}

def execute_move(move_name):
    """Exécute un mouvement donné."""
    if move_name in MOVE_FUNCTIONS:
        MOVE_FUNCTIONS[move_name]()
        return True
    return False

def get_cube_data():
    """Retourne les données actuelles du cube."""
    return cube_data 