# User Interface module for RubyAI
from ursina import Button, Text, Func
import random

from constants import (
    BUTTON_SCALE, BUTTON_COLOR, TEXT_COLOR, BUTTON_COLUMN_X, BUTTON_START_Y,
    GROUP_SPACING_Y, BUTTON_IN_GROUP_SPACING_Y, MOVE_GROUPS_CONFIG,
    SCRAMBLE_MOVES_COUNT
)
from cube_logic import execute_move, init_cube_data
from cube_visuals import update_3d_visuals


def _on_move_click(move_name: str):
    """Execute a cube move and refresh visuals."""
    if execute_move(move_name):
        update_3d_visuals()


def _scramble():
    """Scramble the cube with random moves."""
    moves = [m for _, group in MOVE_GROUPS_CONFIG for m in group]
    for _ in range(SCRAMBLE_MOVES_COUNT):
        execute_move(random.choice(moves))
    update_3d_visuals()


def _reset_cube():
    """Reset the cube to solved state."""
    init_cube_data()
    update_3d_visuals()


def create_ui():
    """Create all UI buttons used to interact with the cube."""
    y = BUTTON_START_Y
    for _, moves in MOVE_GROUPS_CONFIG:
        for move in moves:
            btn = Button(
                text=move,
                color=BUTTON_COLOR,
                scale=BUTTON_SCALE,
                text_color=TEXT_COLOR,
                position=(BUTTON_COLUMN_X, y)
            )
            btn.on_click = Func(_on_move_click, move)
            y -= BUTTON_IN_GROUP_SPACING_Y
        y -= GROUP_SPACING_Y

    # Scramble and reset buttons below move controls
    scramble_btn = Button(
        text='Scramble',
        color=BUTTON_COLOR,
        scale=BUTTON_SCALE,
        text_color=TEXT_COLOR,
        position=(BUTTON_COLUMN_X, y)
    )
    scramble_btn.on_click = Func(_scramble)
    y -= GROUP_SPACING_Y

    reset_btn = Button(
        text='Reset',
        color=BUTTON_COLOR,
        scale=BUTTON_SCALE,
        text_color=TEXT_COLOR,
        position=(BUTTON_COLUMN_X, y)
    )
    reset_btn.on_click = Func(_reset_cube)
