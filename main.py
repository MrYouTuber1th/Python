import pygame
import numpy as np
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 600, 600
size = (width, height)

# Создание окна
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Клеточные автоматы")

# Размер клетки
cell_size = 10

# Размеры поля
rows = height // cell_size
cols = width // cell_size

# Создание случайного начального состояния и цветов
grid = np.random.choice([0, 1], size=(rows, cols))
colors = [((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (0, 0, 0)) for _ in range(2)]

# Создание объекта Clock для отслеживания FPS
clock = pygame.time.Clock()

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Создание нового пустого поля
    new_grid = np.zeros((rows, cols), dtype=int)

    # Обновление состояния клеток
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            neighbors = np.sum(grid[row - 1:row + 2, col - 1:col + 2]) - grid[row, col]
            if grid[row, col] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[row, col] = 0
            elif grid[row, col] == 0 and neighbors == 3:
                new_grid[row, col] = 1
            else:
                new_grid[row, col] = grid[row, col]

    # Обновление поля
    grid = new_grid.copy()

    # Отрисовка клеток с рандомными цветами
    screen.fill((0, 0, 0))
    for row in range(rows):
        for col in range(cols):
            color = colors[grid[row, col]][0]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    # Отображение FPS
    fps = int(clock.get_fps())
    font = pygame.font.Font(None, 36)
    text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(2000)  # Ограничение на 2000 FPS

pygame.quit()
