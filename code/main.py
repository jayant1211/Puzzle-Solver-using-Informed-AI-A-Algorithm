import cv2
from puzzle import *
from node import *
import numpy as np


def ask_choice():
    choice = int(input('\nHello!!\nOn what you want to try 8-Puzzle on:\n\n1.Numbers\n2.Image\n'))
    action(choice)

def action(choice):
    if choice == 1:
        puz = Puzzle(3,None,False)
        steps = puz.process()
        print('A * took {} Steps to Solve the Puzzle!'.format(steps))


    elif choice == 2:
        path = input('Please Enter the path of image:\n')
        
        save = input('Do you want to save the solution Images?(Y/N)\n')
        if (save == 'N') or (save == 'n'):
            save = 0
        elif (save == 'Y') or (save == 'y'):
            save = 1
        else:
            print('Invalid choice for save! Not saving by default.\n')
            save = 0

        process_image(path,save)
        
    else:
        print('INVALID CHOICE!!\nPlease Try Again.\n')
        ask_choice()

def process_image(path,save):
    #print(path)
    img = cv2.imread(r'{}'.format(path))
    img = cv2.resize(img,(450,450))

    cv2.imshow('Original',img)

    grid = []

    '''
    grid[0] = 1,grid[1] = 2.......
    '''
    for j in range(0,3):
        for i in range(0,3):
            grid.append(img[i*150:(i+1)*150,j*150:(j+1)*150])

    #print(len(grid))

    #make a window
    slider = np.ones((450,450,3),np.uint8)
    slider = 255*slider

    image_grid = {}

    for i in range(0,3):
        for j in range(0,3):
            if (j + i*3)!= 8:
                bordered = cv2.copyMakeBorder(grid[j + i*3],2,2,2,2,cv2.BORDER_CONSTANT,value=(0,0,0))

            else:
                white = np.ones((150,150,3),dtype=np.uint8)
                white = 255*white
                bordered = cv2.copyMakeBorder(white,2,2,2,2,cv2.BORDER_CONSTANT,value=(0,0,0))

            bordered = cv2.resize(bordered,(150,150))
            slider[j*150:(j+1)*150,i*150:(i+1)*150] = bordered
            image_grid['{}'.format(i + j*3 + 1)] = bordered

    #for i in range(0,9):
    #    cv2.imshow('{}'.format(i),grid[i])

    '''for i in range(0,3):
        cv2.line(img,)'''

    cv2.imshow('Original',img)
    cv2.waitKey(0)
    cv2.imshow('Slider_Representation',slider)
    cv2.waitKey(0)

    puz = Puzzle(3,image_grid,save)
    steps = puz.process()  

    cv2.destroyAllWindows()
    print('\nA * took {} Steps to Solve the Puzzle!'.format(steps))
ask_choice()