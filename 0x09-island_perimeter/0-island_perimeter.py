#!/usr/bin/python3
"""
This is a module to calculate the perimeter of a single island in a grid
"""


def island_perimeter(grid):
    """
    This function calculates the perimeter of the island in a grid

    Args:
        grid (list): 2D array (horizontal x vertical) of integers.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for hor in range(len(grid)):
        for ver in range(len(grid[hor])):
            if grid[hor][ver] == 1:
                perimeter += 4
                if hor > 0 and grid[hor - 1][ver] == 1:
                    perimeter -= 2
                if ver > 0 and grid[hor][ver - 1] == 1:
                    perimeter -= 2
    return perimeter