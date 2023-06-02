import pygame
import random
screen = pygame.display.set_mode((700,500))
clock = pygame.time.Clock()
enemy_x1 = 0
enemy_y1 = 0
enemy_x2 = 0
enemy_y2 = 0
enemy_x3 = 0
enemy_y3 = 0
score = 0
enemy_velocity_y = 1
x = 350 
y = 400

def checkCollision():
    enemies_y = [enemy_y1,enemy_y2,enemy_y3]
    enemies_x = [enemy_x1,enemy_x2,enemy_x3]
    for enemy_y in enemies_y:
        if enemy_y >= y and enemy_y <= y + 50:
            for enemy_x in enemies_x:
                if enemy_x >= x and enemy_x <= x + 100:
                    print("GAME OVER")
                    print("Score: ",score)
                    exit()
                if enemy_x + 100 > x and enemy_x + 100 < x+100:
                    print("GAME OVER")
                    print("Score: ",score)
                    exit()
        if enemy_y+50 >= y and enemy_y +50 < y+50:
            for enemy_x in enemies_x:
                if enemy_x >= x and enemy_x <= x + 100:
                    print("GAME OVER")
                    print("Score: ",score)
                    exit()
                if enemy_x + 100 > x and enemy_x + 100 < x+100:
                    print("GAME OVER")
                    print("Score: ",score)
                    exit()

def moveEnemy():
    global enemy_x1,enemy_y1,score,enemy_velocity_y
    enemy_y1 += enemy_velocity_y
    if enemy_y1 > 500:
        score += 1
        enemy_y1 = -60
        enemy_x1 = random.randint(1,600)
        enemy_velocity_y += 1
    global enemy_x2,enemy_y2
    enemy_y2 += enemy_velocity_y
    if enemy_y2 > 500:
        score += 1
        enemy_y2 = -60
        enemy_x2= random.randint(1,600)
    global enemy_x3,enemy_y3
    enemy_y3 += enemy_velocity_y
    if enemy_y3 > 500:
        score += 1
        enemy_y3 = -60
        enemy_x3= random.randint(1,600)
    



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill("Yellow")

    checkCollision()
    moveEnemy()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x>0: x -= 5
    if keys[pygame.K_d] and x<600: x += 5

    pygame.draw.rect(screen,"red",(enemy_x1,enemy_y1,100,50))
    pygame.draw.rect(screen,"red",(enemy_x2,enemy_y2,100,50))
    pygame.draw.rect(screen,"red",(enemy_x3,enemy_y3,100,50))
    pygame.draw.rect(screen,"black",(x,y,100,50))
    pygame.display.flip()

    clock.tick(120)
aa