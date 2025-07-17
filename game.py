import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Pac-Man properties
PACMAN_RADIUS = 20
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Walls
walls = [
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 200, 20, 400),
    pygame.Rect(700, 200, 20, 400),
    pygame.Rect(100, 580, 620, 20)
]

# Game clock
clock = pygame.time.Clock()

def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), PACMAN_RADIUS)

def main():
    global pacman_x, pacman_y
    running = True

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        new_x, new_y = pacman_x, pacman_y
        if keys[pygame.K_UP]:
            new_y -= pacman_speed
        if keys[pygame.K_DOWN]:
            new_y += pacman_speed
        if keys[pygame.K_LEFT]:
            new_x -= pacman_speed
        if keys[pygame.K_RIGHT]:
            new_x += pacman_speed

        # Collision detection
        pacman_rect = pygame.Rect(new_x - PACMAN_RADIUS, new_y - PACMAN_RADIUS, PACMAN_RADIUS * 2, PACMAN_RADIUS * 2)
        if not any(pacman_rect.colliderect(wall) for wall in walls):
            pacman_x, pacman_y = new_x, new_y

        # Draw walls
        for wall in walls:
            pygame.draw.rect(screen, GREEN, wall)

        # Draw Pac-Man
        draw_pacman(pacman_x, pacman_y)

        # Update display
        pygame.display.flip()

        # Frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()