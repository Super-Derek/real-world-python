"""
Chapter 1 - Search and Rescue
Base implementation of the Bayesian search-and-rescue model
from 'Real World Python' by Lee Vaughan, Chapter 1.
"""

import sys
import random
import itertools
import numpy as np
import cv2 as cv

# Map image for the fictional Cape Python coastline
MAP_FILE = "cape_python.png"

# Search area rectangles on the map image
# Each tuple is: (UL-X, UL-Y, LR-X, LR-Y)
SA1_CORNERS = (130, 265, 180, 315)
SA2_CORNERS = (80, 255, 130, 305)
SA3_CORNERS = (105, 205, 155, 255)

class Search():
    """Bayesian Search & Rescue game with 3 search areas."""

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(MAP_FILE), file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0
        self.sailor_actual = (0, 0) # As 'local' coords within search area

        self.sa1 = self.img[SA1_CORNERS[1]:SA1_CORNERS[3],
                            SA1_CORNERS[0]:SA1_CORNERS[2]]

        self.sa2 = self.img[SA2_CORNERS[1]:SA2_CORNERS[3],
                            SA2_CORNERS[0]:SA2_CORNERS[2]]

        self.sa3 = self.img[SA3_CORNERS[1]:SA3_CORNERS[3],
                            SA3_CORNERS[0]:SA3_CORNERS[2]]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0


def main() -> None:
    """Entry point for the Chapter 1 Search and Rescue demo."""
    print("Search and Rescue simulation starting...")

    img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
    if img is None:
        print(f"ERROR: Could not load map file {MAP_FILE}", file=sys.stderr)
        sys.exit(1)

    height, width = img.shape[:2]
    print(f"Loaded map image '{MAP_FILE}' ({width}x{height} pixels).")

if __name__ == "__main__":
    main()
