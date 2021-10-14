def display(board, coords, color, next_info, held_info, score, SPEED):
    # Generates the display
    
    border = np.uint8(127 - np.zeros([20, 1, 3]))
    border_ = np.uint8(127 - np.zeros([1, 34, 3]))
    
    dummy = board.copy()
    dummy[coords[:,0], coords[:,1]] = color
    
    right = np.uint8(np.zeros([20, 10, 3]))
    right[next_info[0][:,0] + 2, next_info[0][:,1]] = next_info[1]
    left = np.uint8(np.zeros([20, 10, 3]))
    left[held_info[0][:,0] + 2, held_info[0][:,1]] = held_info[1]
    
    dummy = np.concatenate((border, left, border, dummy, border, right, border), 1)
    dummy = np.concatenate((border_, dummy, border_), 0)
    dummy = dummy.repeat(20, 0).repeat(20, 1)
    dummy = cv2.putText(dummy, str(score), (520, 200), cv2.FONT_HERSHEY_DUPLEX, 1, [0, 0, 255], 2)
    
    # Instructions for the player
    
    dummy = cv2.putText(dummy, "A - move left", (45, 200), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    dummy = cv2.putText(dummy, "D - move right", (45, 225), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    dummy = cv2.putText(dummy, "S - move down", (45, 250), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    dummy = cv2.putText(dummy, "W - hard drop", (45, 275), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    dummy = cv2.putText(dummy, "J - rotate left", (45, 300), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    dummy = cv2.putText(dummy, "L - rotate right", (45, 325), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    dummy = cv2.putText(dummy, "I - hold", (45, 350), cv2.FONT_HERSHEY_DUPLEX, 0.6, [0, 0, 255])
    
    cv2.imshow("Tetris", dummy)
    key = cv2.waitKey(int(1000/SPEED))
    
    return key
