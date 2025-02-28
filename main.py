import cv2
import numpy as np
import time
import os
from puzzle import Puzzle
from node import Node

intro = r"""
 █████        ██████  ██    ██ ███████ ███████ ██      ███████     ███████  ██████  ██      ██    ██ ███████ ██████
██   ██       ██   ██ ██    ██    ███     ███  ██      ██          ██      ██    ██ ██      ██    ██ ██      ██   ██
 █████  █████ ██████  ██    ██   ███     ███   ██      █████       ███████ ██    ██ ██      ██    ██ █████   ██████
██   ██       ██      ██    ██  ███     ███    ██      ██               ██ ██    ██ ██       ██  ██  ██      ██   ██
 █████        ██       ██████  ███████ ███████ ███████ ███████     ███████  ██████  ███████   ████   ███████ ██   ██ """


def ask_choice():
    """Prompt the user to choose a puzzle solving mode."""
    print('Please choose one of the following options:')
    print('1. Solve a Numbered Sliding Puzzle')
    print('2. Solve a Sliding Puzzle from an Image')

    choice = int(input('Enter your choice: '))
    action(choice)


def action(choice):
    """Execute the appropriate action based on user's choice."""
    if choice == 1:
        puzzle = Puzzle(3, None)
        steps = puzzle.process()
        print('A* took {} steps to solve the puzzle!'.format(steps))

    elif choice == 2:
        path = input('Please enter the path of the image:\n')

        process_image(path)

    else:
        print('Invalid selection. Try again:')
        ask_choice()

def process_image(path):
    """Process an image to create and solve a sliding puzzle."""
    # Load and resize the image
    img = cv2.imread(r'{}'.format(path))
    img = cv2.resize(img, (450, 450))

    cv2.imshow('Original', img)

    # Create grid pieces from the image
    grid = []
    for j in range(0, 3):
        for i in range(0, 3):
            grid.append(img[i*150:(i+1)*150, j*150:(j+1)*150])

    # Create a blank slider image
    slider = np.ones((450, 450, 3), np.uint8) * 255

    # Prepare the image grid dictionary for the puzzle
    image_grid = {}
    for i in range(0, 3):
        for j in range(0, 3):
            if (j + i*3) != 8:
                bordered = cv2.copyMakeBorder(grid[j + i*3], 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=(0, 0, 0))
            else:
                # Create blank tile for the empty space
                white = np.ones((150, 150, 3), dtype=np.uint8) * 255
                bordered = cv2.copyMakeBorder(white, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=(0, 0, 0))

            bordered = cv2.resize(bordered, (150, 150))
            slider[j*150:(j+1)*150, i*150:(i+1)*150] = bordered
            image_grid['{}'.format(i + j*3 + 1)] = bordered

    cv2.imshow('Original', img)
    cv2.waitKey(0)
    cv2.imshow('Puzzle', slider)
    cv2.waitKey(0)

    # Create and solve the puzzle
    puzzle = Puzzle(3, image_grid)
    steps = puzzle.process()

    cv2.destroyAllWindows()
    print('\nA* took {} steps to solve the puzzle!'.format(steps))

if __name__ == "__main__":
    print(intro)
    print("\n✨ Welcome to the A* Sliding Puzzle Solver! ✨")
    time.sleep(1)
ask_choice()
           