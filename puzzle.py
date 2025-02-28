import cv2
import numpy as np
import os
from node import Node

class Puzzle:
    def __init__(self, size, image_grid):
        """
        Initialize the puzzle with specified size, image grid.
        
        Args:
            size: Size of the puzzle grid (e.g., 3 for a 3x3 puzzle)
            image_grid: Dictionary of image tiles for visual representation
        """
        self.n = size
        self.open = []
        self.closed = []
        self.img_dict = image_grid

    def accept(self):
        """
        Accept the puzzle configuration from the user input.
        
        Returns:
            2D list representing the puzzle state
        """
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        """
        Calculate the heuristic function value f(x) = h(x) + g(x)
        
        Args:
            start: Starting node
            goal: Goal state
            
        Returns:
            Total heuristic value
        """
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        """
        Calculate the heuristic value (misplaced tiles)
        
        Args:
            start: Current puzzle state
            goal: Goal puzzle state
            
        Returns:
            Number of misplaced tiles
        """
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        
    def process(self):
        """
        Process the puzzle using A* algorithm.
        
        Returns:
            Number of steps taken to solve the puzzle
        """
        # Setup for image-based puzzle
        if self.img_dict is not None:
            print('Enter sequence to jumble image grid:')
            start = self.accept()  # e.g. [['1','2','3'],['4','5','6'],['7','_','8']]
            goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        else:
            # Setup for number-based puzzle
            print("Enter the start state of puzzle (e.g.:\n1 2 3\n4 5 6\n7 _ 8)")
            start = self.accept()
            print("Enter the goal state of puzzle (e.g.:\n1 2 3\n4 5 6\n7 _ 8)")        
            goal = self.accept()

        # Initialize the starting node
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        # Add start node to open list
        self.open.append(start)
        step = 0

        print('\nSolving Puzzle:')
        print('Step No: ', step)
        while True:
            cur = self.open[0]
            if cur.direction:
                print("Shift blank space to {}".format(cur.direction))
            # Flatten current puzzle state for display
            indexes = []
            for myList in cur.data:
                for item in myList:
                    indexes.append(item)

            print('\n')

            # Display for number-based puzzle
            if self.img_dict is None:
                for i in cur.data:
                    for j in i:
                        print(j, end=" ")
                    print("")
                print('\n')
            # Display for image-based puzzle
            else:
                print('Check image...')
                image_grid = self.img_dict
                slider = np.ones((450, 450, 3), np.uint8)
                
                # Construct the visual representation
                for i in range(0, 3):
                    for j in range(0, 3):
                        idx = indexes[j + i*3]
                        if idx == '_':
                            idx = 9
                        slider[i*150:(i+1)*150, j*150:(j+1)*150] = image_grid[str(idx)]
                
                cv2.imshow('Slider', slider) # Display the current state of the puzzle
                cv2.waitKey(0)
            
            
            # Check if goal state is reached
            if self.h(cur.data, goal) == 0:
                break
                
            # Generate and evaluate child nodes
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            step = step + 1 
            print('Step No.: ', step)

            # Sort the open list based on f value
            self.open.sort(key=lambda x: x.fval, reverse=False)

            # Safety check for unsolvable puzzles
            #TODO - make this more efficient and less arbitrary; check for parity inversion
            if step > 2500:
                print('Puzzle is in an unsolvable state!')
                exit()

        return step
