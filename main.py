import cv2
import numpy as np
from random import choice

SPEED = 1 # Controls the speed of the tetris pieces

# Make a board

board = np.uint8(np.zeros([20, 10, 3]))

# Initialize some variables

quit = False
place = False
drop = False
switch = False
held_piece = ""
flag = 0
score = 0

# All the tetris pieces
next_piece = choice(["O", "I", "S", "Z", "L", "J", "T"])

def get_info(piece):
    if piece == "I":
        coords = np.array([[0, 3], [0, 4], [0, 5], [0, 6]])
        color = [255, 155, 15]
    elif piece == "T":
        coords = np.array([[1, 3], [1, 4], [1, 5], [0, 4]])
        color = [138, 41, 175]
    elif piece == "L":
        coords = np.array([[1, 3], [1, 4], [1, 5], [0, 5]])
        color = [2, 91, 227]
    elif piece == "J":
        coords = np.array([[1, 3], [1, 4], [1, 5], [0, 3]])
        color = [198, 65, 33]
    elif piece == "S":
        coords = np.array([[1, 5], [1, 4], [0, 3], [0, 4]])
        color = [55, 15, 215]
    elif piece == "Z":
        coords = np.array([[1, 3], [1, 4], [0, 4], [0, 5]])
        color = [1, 177, 89]
    else:
        coords = np.array([[0, 4], [0, 5], [1, 4], [1, 5]])
        color = [2, 159, 227]
    
    return coords, color

