#libraries
import pygame
import time
import random

pygame.init()


#Colors
snakeColor = (0, 129, 204)
backgroundColor = (16, 16, 16)
scoreColor = (79, 196, 79)
red = (255, 77, 0)
tgtsColor = (245,245,220)

#Game_Informations
game_display = pygame.display.set_mode((600,400))
font = pygame.font.SysFont("Verdana",10)
t = font.render("@ JaseerZoiydi", True,(245,245,245))
game_display.blit(t, [5,5])
pygame.display.set_caption("Jo Snake !")

clock = pygame.time.Clock()


#Snake_Informations
snake_size = 10
snake_speed = 10

message_font = pygame.font.SysFont("Verdana", 20)
score_font = pygame.font.SysFont("Verdana", 20)

#Functions
def print_score (score) :
    text = score_font.render("0"+ str(score), True, scoreColor)
    game_display.blit(text, [20,5])

def draw_snake (snake_size, snake_pixels) :
    for px in snake_pixels :
        pygame.draw.rect(game_display, snakeColor, [px[0], px[1], snake_size, snake_size])

def run_game() :
    game_over = False
    game_close = False

    x = 300
    y = 200

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    #targets_Positions
    tgt_x = round(random.randrange(0, 600-snake_size) / 10.0)* 10.0
    tgt_y = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    while tgt_x in [5,6,7,8] and tgt_y in[21,23,24] :
        tgt_x = round(random.randrange(0, 600-snake_size) / 10.0)* 10.0
        tgt_y = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_a = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_b = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    while tgt_a in [5,6,7,8] and tgt_b in[21,23,24] :
        tgt_a = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
        tgt_b = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_m = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_n = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    while tgt_m in [5,6,7,8] and tgt_n in[21,23,24] :
        tgt_m = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
        tgt_n = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_w = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_z = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    while tgt_w in [5,6,7,8] and tgt_z in[21,23,24] :
        tgt_w = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
        tgt_z = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_g = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    tgt_h = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
    while tgt_g in [5,6,7,8] and tgt_h in[21,23,24] :
        tgt_g = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
        tgt_h = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0

    while not game_over :

        #Game_Close
        while game_close :
            game_display.fill(backgroundColor)
            game_display.blit(t, [510,377])
            game_over_message = message_font.render("U LOST BRO :( ", True, red)
            game_display.blit(game_over_message, [200, 170])
            print_score(snake_length - 1)
            pygame.display.update()

            #Game_Start
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_1 :
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2 :
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
        
        #Game_Play
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT :
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP :
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN :
                    x_speed = 0
                    y_speed = snake_size
 
        #Game_Lost
        if x >= 600 or x < 0 or y >= 400 or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(backgroundColor)
        game_display.blit(t, [510,377])
        pygame.draw.rect(game_display, tgtsColor, [tgt_x, tgt_y, snake_size, snake_size])
        pygame.draw.rect(game_display, tgtsColor, [tgt_a, tgt_b, snake_size, snake_size])
        pygame.draw.rect(game_display, tgtsColor, [tgt_w, tgt_z, snake_size, snake_size])
        pygame.draw.rect(game_display, tgtsColor, [tgt_m, tgt_n, snake_size, snake_size])
        pygame.draw.rect(game_display, tgtsColor, [tgt_g, tgt_h, snake_size, snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length :
            del snake_pixels[0]
        
        for p in snake_pixels [:-1] :
            if p == [x, y]:
                game_close = True
        
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        #Remake_Targets_Positions
        if x == tgt_x and y == tgt_y :
            tgt_x = round(random.randrange(0, 600-snake_size) / 10.0)* 10.0
            tgt_y = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            while tgt_x in [5,6,7,8] and tgt_y in [21,23,24] :
                tgt_x = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
                tgt_y = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            snake_length +=1
        if x == tgt_a and y == tgt_b :
            tgt_a = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            tgt_b = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            while tgt_a in [5,6,7,8] and tgt_b in [21,23,24] :
                tgt_a = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
                tgt_b = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            snake_length +=1
        if x == tgt_m and y == tgt_n :
            tgt_m = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            tgt_n = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            while tgt_m in [5,6,7,8] and tgt_n in [21,23,24] :
                tgt_m = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
                tgt_n = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            snake_length +=1
        if x == tgt_g and y == tgt_h :
            tgt_g = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            tgt_h = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            while tgt_g in [5,6,7,8] and tgt_h in [21,23,24]:
                tgt_g = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
                tgt_h = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            snake_length +=1
        if x == tgt_w and y == tgt_z :
            tgt_w = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            tgt_z = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            while tgt_w in [5,6,7,8] and tgt_z in[21,23,24]:
                tgt_w = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
                tgt_z = round(random.randrange(0, 400-snake_size) / 10.0)* 10.0
            snake_length +=1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()
#Runing_Game
run_game()


