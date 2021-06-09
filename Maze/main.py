# Importing the library
import pygame
import sys
import time

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing Color
color = (255, 255, 255)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

W, H = 20, 20
X, Y = 0, 0

m = []
start = 1, 1
end = 2, 5

for i in range(len(maze)):
    m.append([])
    for j in range(len(maze[i])):
        m[-1].append(0)
i, j = start
m[i][j] = 1


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i - 1][j] == 0 and maze[i - 1][j] == 0:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and maze[i][j - 1] == 0:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and maze[i + 1][j] == 0:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and maze[i][j + 1] == 0:
                    m[i][j + 1] = k + 1


k = 0

# Drawing Rectangle
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            x = 21 * (j + 1)
            y = 21 * (i + 1)
            pygame.draw.rect(surface, color, pygame.Rect(x, y, W, H))


# draw end maze
i, j = end
x = 21 * (j + 1)
y = 21 * (i + 1)

pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(x, y, W, H))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k)
        # Drawing Rectangle
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] > 0:
                    x = 21 * (j + 1)
                    y = 21 * (i + 1)
                    pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(x, y, W, H))
                    pygame.display.update()

        pygame.time.wait(500)
    pygame.display.flip()
