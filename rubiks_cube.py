import numpy as np

class RubiksCube:
    """Simple Rubik's Cube representation using numpy arrays."""

    # Face indices
    FRONT = 0
    BACK = 1
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5

    def __init__(self):
        # Initialize each face with its own color index 0..5
        self.cube = np.array([np.full((3, 3), i, dtype=int) for i in range(6)])

    def rotate_face_cw(self, idx):
        self.cube[idx] = np.rot90(self.cube[idx], -1)

    def rotate_face_ccw(self, idx):
        self.cube[idx] = np.rot90(self.cube[idx], 1)

    def front_cw(self):
        """Front face clockwise"""
        self.rotate_face_cw(self.FRONT)
        u, d, l, r = self.UP, self.DOWN, self.LEFT, self.RIGHT

        temp = self.cube[u, 2].copy()
        self.cube[u, 2] = self.cube[l, :, 2][::-1]
        self.cube[l, :, 2] = self.cube[d, 0]
        self.cube[d, 0] = self.cube[r, :, 0][::-1]
        self.cube[r, :, 0] = temp

    def front_ccw(self):
        """Front face counterclockwise"""
        for _ in range(3):
            self.front_cw()

    def move(self, code):
        if code == 0:
            self.front_cw()
        elif code == 1:
            self.front_ccw()
        else:
            raise ValueError("Unknown move code")

    def __str__(self):
        return np.array2string(self.cube)


def main():
    cube = RubiksCube()
    print("Initial cube:")
    print(cube)
    cube.move(0)  # Front clockwise
    print("\nAfter F move:")
    print(cube)
    for _ in range(3):
        cube.move(1)
    print("\nAfter reversing the move:")
    print(cube)

if __name__ == "__main__":
    main()
