import cv2
from numpy.lib.function_base import append
from node import *
import numpy as np
import os

class Puzzle:
    def __init__(self,size,image_grid,save):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.write = save
        self.open = []
        self.closed = []
        self.img_dict = image_grid

    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        

    def process(self):
        #If working on Image::
        if self.img_dict is not None:
            print('fkjb',self.write)
            if self.write:
                folders = os.listdir(r'saves')
                if not folders:
                    os.mkdir(r'saves\0')
                    folder = 0
                else:
                    folder = int(folders[-1]) + 1
                    os.mkdir(r'saves\{}'.format(folder))
            print('Enter the Random Sequence of Grid:')
            start = self.accept()

            goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        else:
            print("Enter the start state matrix:")
            start = self.accept()
            print("Enter the goal state matrix:")        
            goal = self.accept()

        start = Node(start,0,0)
        start.fval = self.f(start,goal)

        """ Put the start node in the open list"""
        self.open.append(start)
        step = 0

        print('_____________\nStarting:')
        print('Step: ',step)
        while True:
            cur = self.open[0]
            
            #flattening
            indexes = []
            for myList in cur.data:
                for item in myList:
                    indexes.append(item)
            #print(indexes)

            print('\n')

            #For numbers::
            if self.img_dict is None:
                for i in cur.data:
                    for j in i:
                        print(j,end=" ")
                    print("")
                print('\n')

            #for Images::
            else:
                print('Solving for image...\nCheck Image...')
                image_grid = self.img_dict
                slider = np.ones((450,450,3),np.uint8)
                
                #print(image_grid.keys())

                for i in range(0,3):
                    for j in range(0,3):
                        idx = indexes[j + i*3]
                        if idx == '_':
                            idx = 9
                        slider[i*150:(i+1)*150,j*150:(j+1)*150] = image_grid[str(idx)]
                
                cv2.imshow('Slider',slider) 
                if self.write:
                    cv2.imwrite('saves\{}\{}.jpg'.format(folder,step),slider)     
                cv2.waitKey(0)
            
            
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            step = step + 1 
            print('Step: ',step)

            """ sort the opne list based on f value """
            self.open.sort(key = lambda x:x.fval,reverse=False)

            if step>2500:
                print('Puzzle is in Insolvable Instance!!')
                exit()

        return step