import argparse
import random
import time
from typing import List

import neat
import numpy as np
import pygame
import matplotlib.pyplot as plt

from rubiks_cube import RubiksCube

# Solved cube state for reference
_SOLVED_STATE = RubiksCube().cube.copy()

# Color mapping for Pygame visualization
COLORS = {
    0: (255, 0, 0),      # red
    1: (0, 255, 0),      # green
    2: (0, 0, 255),      # blue
    3: (255, 255, 0),    # yellow
    4: (255, 165, 0),    # orange
    5: (255, 255, 255),  # white
}


class DashboardReporter(neat.reporting.BaseReporter):
    """Reporter that stores best fitness and prints every 20 generations."""

    def __init__(self, storage: List[float]):
        self.storage = storage
        self.generation = 0

    def post_evaluate(self, config, population, species, best_genome):
        self.storage.append(best_genome.fitness)
        self.generation += 1
        if self.generation % 20 == 0:
            print(f"Generation {self.generation}: best fitness {best_genome.fitness:.2f}")


def scramble_cube(cube: RubiksCube, moves: int = 2) -> None:
    for _ in range(moves):
        cube.move(random.randint(0, 1))


def evaluate_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        cube = RubiksCube()
        scramble_cube(cube, moves=2)
        for _ in range(2):
            inputs = cube.cube.flatten() / 5.0
            output = net.activate(inputs)
            action = int(np.argmax(output))
            cube.move(action)
        diff = np.sum(cube.cube != _SOLVED_STATE)
        genome.fitness = -float(diff)


def draw_cube(screen, cube: RubiksCube, size: int = 30) -> None:
    offset = {
        RubiksCube.UP: (3 * size, 0),
        RubiksCube.LEFT: (0, 3 * size),
        RubiksCube.FRONT: (3 * size, 3 * size),
        RubiksCube.RIGHT: (6 * size, 3 * size),
        RubiksCube.BACK: (9 * size, 3 * size),
        RubiksCube.DOWN: (3 * size, 6 * size),
    }
    for face, (ox, oy) in offset.items():
        face_data = cube.cube[face]
        for i in range(3):
            for j in range(3):
                rect = pygame.Rect(ox + j * size, oy + i * size, size, size)
                color = COLORS[int(face_data[i, j])]
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)


def run_visual(config_file: str, generations: int = 10) -> None:
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_file,
    )
    pop = neat.Population(config)
    history: List[float] = []
    pop.add_reporter(DashboardReporter(history))
    winner = pop.run(evaluate_genomes, generations)

    # Visualize the winning genome solving a cube
    pygame.init()
    screen = pygame.display.set_mode((12 * 30, 9 * 30))
    pygame.display.set_caption("Rubik's Cube NEAT Visualization")
    net = neat.nn.FeedForwardNetwork.create(winner, config)
    cube = RubiksCube()
    scramble_cube(cube, moves=2)
    clock = pygame.time.Clock()
    running = True
    steps = 0
    while running and steps < 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((50, 50, 50))
        draw_cube(screen, cube)
        pygame.display.flip()
        inputs = cube.cube.flatten() / 5.0
        output = net.activate(inputs)
        action = int(np.argmax(output))
        cube.move(action)
        steps += 1
        clock.tick(2)
    pygame.quit()


def run_training(config_file: str, generations: int = 50) -> None:
    history: List[float] = []
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_file,
    )
    pop = neat.Population(config)
    pop.add_reporter(DashboardReporter(history))
    pop.add_reporter(neat.StdOutReporter(False))
    winner = pop.run(evaluate_genomes, generations)
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Training Progress")
    plt.show()
    print("Best genome:\n", winner)


def run_headless(config_file: str, generations: int = 50) -> None:
    history: List[float] = []
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_file,
    )
    pop = neat.Population(config)
    pop.add_reporter(DashboardReporter(history))
    winner = pop.run(evaluate_genomes, generations)
    print("Training complete. Best fitness:", max(history))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rubik's Cube NEAT solver")
    parser.add_argument(
        "--mode",
        choices=["visual", "train", "headless"],
        default="headless",
        help="Execution mode",
    )
    parser.add_argument(
        "--config",
        default="neat_config.ini",
        help="Path to NEAT configuration file",
    )
    parser.add_argument(
        "--generations",
        type=int,
        default=50,
        help="Number of generations",
    )
    args = parser.parse_args()

    if args.mode == "visual":
        run_visual(args.config, args.generations)
    elif args.mode == "train":
        run_training(args.config, args.generations)
    else:
        run_headless(args.config, args.generations)
