from pygame import *
from random import randrange

font.init()

'''create the display'''
size = 800
res = 50

size_amount = (size, size)

win = display.set_mode(size_amount)
display.set_caption('Snake')

# load the background
bg = transform.scale(image.load('background.png'), size_amount)

run = True
finish = False

clock = time.Clock()
fps = 60

'''Settings'''

dirs = {'W': True, 'S': True, 'A': True, 'D': True}

sx, sy = 0, 0
x, y = randrange(res, size-res, res), randrange(res, size-res, res)

lenght = 1
snake = [(x, y)]

apple = randrange(res, size-res, res), randrange(res, size-res, res)


green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

score_numbers = list()

score = 0

speed_count, snake_speed = 0, 10

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    win.blit(bg, (0,0))

    if finish != True:

        # score
        score_label = font.SysFont("Arial", 50).render('Score:', True, blue)
        win.blit(score_label, (0, 0))

        score_text = font.SysFont("Arial", 50).render(str(score), True, blue)
        win.blit(score_text, (170, 0))

        # snake
        [(draw.rect(win, green, (i, j, res - 1, res - 1))) for i, j in snake]
        draw.rect(win, red, (*apple, res, res))

        speed_count += 1

        # eat apples
        if snake[-1] == apple:
            apple = randrange(res, size-res, res), randrange(res, size-res, res)
            lenght += 1
            score += 1
            fps += 0.4
            score_numbers.append(score)

            print('Yummy!!!')

        if not speed_count % snake_speed:
            snake = snake[-lenght:]
            x += sx*50
            y += sy*50
            snake.append((x,y))

        for i in score_numbers:
            if i % 5 == 0:
                fps += 0.05

        # snake's keys management

        keys = key.get_pressed()

        if keys[K_w] and dirs['W']:
            sx, sy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True,}
        
        if keys[K_s] and dirs['S']:
            sx, sy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True,}

        if keys[K_a] and dirs['A']:
            sx, sy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False,}

        if keys[K_d] and dirs['D']:
            sx, sy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True,}

    # game over
    if x < 0 or x > size - res or y < 0 or y > size - res:
        img = font.SysFont("Arial", 100).render('Game over', True, red)
        win.blit(img, (200, 300))
        finish = True


    display.update()
    clock.tick(fps)

