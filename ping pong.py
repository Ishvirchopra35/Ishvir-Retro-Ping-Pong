# pingpong.py

import sys
import pygame


pygame.init()

WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 0
ball_speed_y = 0

paddle_width = 15
paddle_height = 60
left_paddle_x = 10
right_paddle_x = WIDTH - 25
left_paddle_y = HEIGHT // 2 - paddle_height // 2
right_paddle_y = HEIGHT // 2 - paddle_height // 2
paddle_speed = 7
score_left = 0
score_right = 0

font = pygame.font.Font(None, 36)

def reset_ball():
    return WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED

timer_started = False
start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not timer_started and pygame.time.get_ticks() - start_time >= 5000:
        timer_started = True
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - paddle_height:
        right_paddle_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if (
        left_paddle_x < ball_x < left_paddle_x + paddle_width
        and left_paddle_y < ball_y < left_paddle_y + paddle_height
    ) or (
        right_paddle_x < ball_x < right_paddle_x + paddle_width
        and right_paddle_y < ball_y < right_paddle_y + paddle_height
    ):
        ball_speed_x = -ball_speed_x

    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball_x <= 0:
        score_right += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()

    if ball_x >= WIDTH:
        score_left += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))
    score_display = font.render(f'{score_left} - {score_right}', True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 40, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)