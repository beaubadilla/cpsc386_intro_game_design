# Map is 51x47
import pygame
from imagerect import ImageRect


class Maze:
    BRICK_SIZE = 15

    def __init__(self, screen, mazefile, shieldfile, hportalfile, vportalfile, pillfile, powerpillfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()
            self.original = self.rows

        self.bricks = []
        self.shields = []
        self.hportals = []
        self.vportals = []
        self.pills = []
        self.powerpills = []
        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, "tile", sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.hportal = ImageRect(screen, hportalfile, sz, sz)
        self.vportal = ImageRect(screen, vportalfile, sz, sz)
        self.pill = ImageRect(screen, pillfile, sz, sz)
        self.powerpill = ImageRect(screen, powerpillfile, sz, sz)

        # Portals
        self.portal_counter = 0
        self.portals = []

        # Maze.BRICK_SIZE
        self.deltax = self.deltay = 15

        self.testing_pill = []

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height                # w = h = 15
        dx, dy = self.deltax, self.deltay       # dx = dy = 15

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'o':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'h':
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'v':
                    self.vportals.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'p':
                    self.testing_pill.append(list((pygame.Rect(ncol * dx, nrow * dy, w, h), nrow, ncol)))
                    self.pills.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'P':
                    self.powerpills.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def update(self):
        """Only updates pills and powerpills by reading in file"""
        with open(self.filename, 'r') as file:
            self.rows = file.readlines()
        sz = 15
        delta = 15
        self.pills.clear()
        self.powerpills.clear()
        self.bricks.clear()
        self.hportals.clear()
        self.vportals.clear()
        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'p':
                    self.pills.append(pygame.Rect(ncol * delta, nrow * delta, sz, sz))
                if col == 'P':
                    self.powerpills.append(pygame.Rect(ncol * delta, nrow * delta, sz, sz))
                if col == 'h':
                    self.hportals.append(pygame.Rect(ncol * delta, nrow * delta, sz, sz))
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * delta, nrow * delta, sz, sz))
                if col == 'v':
                    self.vportals.append(pygame.Rect(ncol * delta, nrow * delta, sz, sz))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.hportals:
            self.screen.blit(self.hportal.image, rect)
        for rect in self.vportals:
            self.screen.blit(self.vportal.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)
        for rect in self.powerpills:
            self.screen.blit(self.powerpill.image, rect)

    def reset_maze_file(self):
        with open(self.filename, 'w') as file:
            file.writelines(self.original)
