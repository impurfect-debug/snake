import random 
import pygame as pg


def snake():
    
    pg.init()
    
    mode = (400,600)
    screen = pg.display.set_mode(mode)
    pg.display.set_caption("Snake")
    red = (255,0,0)
    green = (0,255,0)
    black = (0,0,0)
    snake_x = 200
    snake_y = 300
    dx,dy = 0,0
    apple_x = random.randint(0,19)*20
    apple_y = random.randint(0,29)*20
    clock = pg.time.Clock()
    snake = [(snake_x,snake_y)]
    score = 0
    start = True
    
    while start:
        
        screen.fill(black)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                start = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    dx,dy = 0,-20
                if event.key == pg.K_DOWN:
                    dx,dy = 0,20
                if event.key == pg.K_RIGHT:
                    dx,dy = 20,0
                if event.key == pg.K_LEFT:
                    dx,dy = -20,0
                    
        snake_x += dx
        snake_y += dy
        
        snake.append((snake_x,snake_y))
        
        if snake_x == apple_x and snake_y == apple_y:
            apple_x = random.randint(0,19)*20
            apple_y = random.randint(0,29)*20
            score += 1
            print(f"Current score : {score}")
        # delete the tail because the snake keeps growing with the loop    
        else: 
            snake.pop(0)
        if snake_x < 0 or snake_x >= 400 or snake_y < 0 or snake_y >= 600:
            print(f"Oops! Game Over\nFinal score : {score}")
            break
        
        for body in snake:
            pg.draw.rect(screen,green,(body[0],body[1],20,20))
        pg.draw.rect(screen,red,(apple_x,apple_y,20,20))
        
        pg.display.flip()
        clock.tick(5)
                 
    pg.quit()

snake()