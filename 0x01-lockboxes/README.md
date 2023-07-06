# 0x01. Lockboxes
This project is focused on solving the "Lockboxes" problem, which involves determining if all the lockboxes in a given collection can be opened. Each box can contain keys that correspond to other boxes in the collection.

The goal is to create a Python function canUnlockAll(boxes) that checks if it's possible to unlock all the boxes in the collection.



## Tasks
### [Lockboxes](0-lockboxes.py) 
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
	- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

