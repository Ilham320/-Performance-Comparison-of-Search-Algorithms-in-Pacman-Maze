# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1un9QNSYtutkOK9ruvNcM25HCnqDSUKV2

#DFS
"""

def dfs(maze, start, goal):
    stack = [(start, [])]  # Stack holds tuples of (current state, path taken)
    visited = set()  # To avoid revisiting states

    while stack:
        current_state, path = stack.pop()

        if current_state == goal:
            return path  # Return the path to goal

        if current_state not in visited:
            visited.add(current_state)
            for neighbor in maze.get_neighbors(current_state):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None  # No path found

"""#BFS"""

from collections import deque

def bfs(maze, start, goal):
    queue = deque([(start, [])])  # Queue holds tuples of (current state, path taken)
    visited = set()  # To avoid revisiting states

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal:
            return path  # Return the path to goal

        if current_state not in visited:
            visited.add(current_state)
            for neighbor in maze.get_neighbors(current_state):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No path found

"""#UCS"""

import heapq

def ucs(maze, start, goal):
    frontier = [(0, start, [])]  # Priority queue holds tuples of (cost, current state, path taken)
    visited = set()  # To avoid revisiting states

    while frontier:
        cost, current_state, path = heapq.heappop(frontier)

        if current_state == goal:
            return path  # Return the path to goal

        if current_state not in visited:
            visited.add(current_state)
            for neighbor, move_cost in maze.get_neighbors_with_cost(current_state):
                if neighbor not in visited:
                    heapq.heappush(frontier, (cost + move_cost, neighbor, path + [neighbor]))

    return None  # No path found

"""#Comparing Performance for Different Mazes"""

import time

def compare_algorithms(maze, start, goal):
    print(f"Running on {maze.name}")

    # Run DFS
    start_time = time.time()
    path_dfs = dfs(maze, start, goal)
    dfs_time = time.time() - start_time
    print(f"DFS time: {dfs_time:.4f} seconds")

    # Run BFS
    start_time = time.time()
    path_bfs = bfs(maze, start, goal)
    bfs_time = time.time() - start_time
    print(f"BFS time: {bfs_time:.4f} seconds")

    # Run UCS
    start_time = time.time()
    path_ucs = ucs(maze, start, goal)
    ucs_time = time.time() - start_time
    print(f"UCS time: {ucs_time:.4f} seconds")

    # Output the results
    print(f"DFS path length: {len(path_dfs)}")
    print(f"BFS path length: {len(path_bfs)}")
    print(f"UCS path length: {len(path_ucs)}")
    print("-" * 40)

"""# Maze Sizes"""

class Maze:
    def __init__(self, grid, start, goal):
        """
        Initialize the maze with a grid, starting point, and goal.

        grid: 2D list representing the maze (0 = wall, 1 = free space).
        start: Tuple (x, y) representing the starting position.
        goal: Tuple (x, y) representing the goal position.
        """
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, x, y):
        """
        Check if the coordinates (x, y) are within bounds and not a wall.
        """
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 1

    def get_neighbors(self, x, y):
        """
        Get the valid neighbors (up, down, left, right) for the given position (x, y).
        """
        neighbors = []

        # Up
        if self.is_valid(x - 1, y):
            neighbors.append((x - 1, y))
        # Down
        if self.is_valid(x + 1, y):
            neighbors.append((x + 1, y))
        # Left
        if self.is_valid(x, y - 1):
            neighbors.append((x, y - 1))
        # Right
        if self.is_valid(x, y + 1):
            neighbors.append((x, y + 1))

        return neighbors

    def get_neighbors_with_cost(self, x, y):
        """
        Get the valid neighbors along with their movement cost (assumed cost of 1 for simplicity).
        """
        neighbors = []

        # Up
        if self.is_valid(x - 1, y):
            neighbors.append(((x - 1, y), 1))
        # Down
        if self.is_valid(x + 1, y):
            neighbors.append(((x + 1, y), 1))
        # Left
        if self.is_valid(x, y - 1):
            neighbors.append(((x, y - 1), 1))
        # Right
        if self.is_valid(x, y + 1):
            neighbors.append(((x, y + 1), 1))

        return neighbors

"""Tiny Maze (5x5)"""

tinyMaze = Maze(
    grid=[
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1]
    ],
    start=(0, 0),  # Starting position at top-left corner
    goal=(4, 4)    # Goal at bottom-right corner
)

"""Medium Maze (10x10)"""

mediumMaze = Maze(
    grid=[
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
    ],
    start=(0, 0),  # Starting position at top-left corner
    goal=(9, 9)    # Goal at bottom-right corner
)

"""Big Maze (20x20)"""

bigMaze = Maze(
    grid=[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    start=(0, 0),  # Starting position at top-left corner
    goal=(19, 19)   # Goal at bottom-right corner
)

"""#Compare"""

def compare_algorithms(maze, start, goal):
    """
    Compares the performance of different pathfinding algorithms.

    Args:
        maze: The maze object.
        start: The starting position (tuple).
        goal: The goal position (tuple).
    """


# prompt: compare performance
compare_algorithms(tinyMaze, tinyMaze.start, tinyMaze.goal)
compare_algorithms(mediumMaze, mediumMaze.start, mediumMaze.goal)
compare_algorithms(bigMaze, bigMaze.start, bigMaze.goal)

display(compare_algorithms)

print(compare_algorithms)