import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Mapping of face indices used by rubiks_cube.py
FRONT, BACK, UP, DOWN, LEFT, RIGHT = range(6)

# Default color mapping for the six faces
COLORS = {
    0: "white",
    1: "yellow",
    2: "blue",
    3: "green",
    4: "orange",
    5: "red",
}

# Orientation vectors for each face. Each entry contains
# (normal, axis_u, axis_v) describing a local coordinate system for that face.
ORIENTATIONS = {
    FRONT: (np.array([0, 0, 1]), np.array([1, 0, 0]), np.array([0, 1, 0])),
    BACK:  (np.array([0, 0, -1]), np.array([-1, 0, 0]), np.array([0, 1, 0])),
    UP:    (np.array([0, 1, 0]), np.array([1, 0, 0]), np.array([0, 0, -1])),
    DOWN:  (np.array([0, -1, 0]), np.array([1, 0, 0]), np.array([0, 0, 1])),
    LEFT:  (np.array([-1, 0, 0]), np.array([0, 0, -1]), np.array([0, 1, 0])),
    RIGHT: (np.array([1, 0, 0]), np.array([0, 0, 1]), np.array([0, 1, 0])),
}


def _square_vertices(face: int, row: int, col: int) -> list:
    """Return the 4 vertices for a sticker located on a given face."""
    normal, axis_u, axis_v = ORIENTATIONS[face]
    base = normal * 1.5

    u0 = -1.5 + col
    u1 = u0 + 1
    v1 = 1.5 - row
    v0 = v1 - 1

    p1 = base + axis_u * u0 + axis_v * v0
    p2 = base + axis_u * u1 + axis_v * v0
    p3 = base + axis_u * u1 + axis_v * v1
    p4 = base + axis_u * u0 + axis_v * v1
    return [p1, p2, p3, p4]


def view_cube(cube: np.ndarray) -> None:
    """Display a Rubik's cube from a 6x3x3 numpy array."""
    if cube.shape != (6, 3, 3):
        raise ValueError("Cube array must have shape (6, 3, 3)")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.axis("off")

    polys = []
    colors = []

    for face in range(6):
        for r in range(3):
            for c in range(3):
                polys.append(_square_vertices(face, r, c))
                colors.append(COLORS.get(int(cube[face, r, c]), "gray"))

    pc = Poly3DCollection(polys, facecolors=colors, edgecolors="black")
    ax.add_collection3d(pc)
    plt.show()


def main() -> None:
    sample = np.array(
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[2, 2, 2], [2, 2, 2], [3, 3, 3]],
            [[2, 2, 2], [3, 3, 3], [3, 3, 3]],
            [[4, 4, 5], [4, 4, 5], [4, 4, 5]],
            [[4, 5, 5], [4, 5, 5], [4, 5, 5]],
        ],
        dtype=int,
    )
    view_cube(sample)


if __name__ == "__main__":
    main()
