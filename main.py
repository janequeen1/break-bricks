import pygame
import random

# 초기화
pygame.init()

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 화면 크기 설정
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기")

# 공 설정
ball_width = 20
ball_height = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 3
ball_dy = 3

# 패들 설정
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_dx = 0
paddle_speed = 6

# 벽돌 설정
brick_width = 75
brick_height = 20
bricks = []

for i in range(7):
    for j in range(5):
        bricks.append(pygame.Rect(i * (brick_width + 10) + 35, j * (brick_height + 10) + 50, brick_width, brick_height))

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_dx = -paddle_speed
            elif event.key == pygame.K_RIGHT:
                paddle_dx = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_dx = 0

    # 패들 이동
    paddle_x += paddle_dx
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > WIDTH - paddle_width:
        paddle_x = WIDTH - paddle_width

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 벽과 충돌
    if ball_x <= 0 or ball_x >= WIDTH - ball_width:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1
    if ball_y >= HEIGHT:
        running = False  # 게임 오버

    # 패들과 충돌
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y < paddle_y + paddle_height:
        ball_dy *= -1

    # 벽돌과 충돌
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy *= -1
            break

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_width, ball_height))

    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()