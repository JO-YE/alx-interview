#!/usr/bin/python3
'''A function that determines if all boxes in a colection can be opened
   returns True if it is posible to unlock all the boxes, false otherwise
'''


def canUnlockAll(boxes):
    '''This method takes list of lists as input'''
    # Each sublist represent a box
    boxes_num = len(boxes)
    box_visited = {0: True}  # first box as been unlocked and visited already
    storage = [0]  # this container stores box indices that can be visited
    # or rather boxes that need to be visited
    # `0` represent index 0, the first box as been unloced

    while storage:  # while storage is not empty
        recent_box = storage.pop()  # LIFO principle
        # this returns the last element that was added to the storage

        for key in boxes[recent_box]:  # boxes is a list of lists
            if key < boxes_num and key not in box_visited:
                box_visited[key] = True
                storage.append(key)

    return len(box_visited) == boxes_num
    # checking that the num of boxes visted equals the total num of boxes
    # this will return  true if all boxes have been `visited` otherwise false
