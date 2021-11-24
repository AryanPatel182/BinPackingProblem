import pygame, random
from time import sleep

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("First-Fit Algorithm")

WHITE = (255, 255, 255)
BLUE  = (0,255,0)
RED = (255, 0, 0)
TXT = (190,189,150)


# def display_plot(value):
#     for i in range(0,kk):
#         pygame.draw.line(screen, WHITE, (int(i*(800/kk)) , 600), (int(i*(800/kk)), 600 - value[i]), 3)


value = [74,90,29,19,62,53,14,82,10,41,47,67,38,26,30]
rspace = []
bins = 15
capacity = 100
# for i in range(0, bins):
#     value.append(random.randint(1, capacity))
    # rspace.append(capacity)

print(value)

running = True
while running:
    sleep(0.01)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # display_plot(value)
    for i in range(0, bins):
        rspace.append(capacity)
    w = round(800 / bins)
    h = round(capacity)
    sp = 0

    for i in value:
        pygame.draw.rect(screen, RED, pygame.Rect(sp, 20, round(w - 10), i))
        sp = sp + w

    sp = 0
    color = RED
    ytxt = 300
    for i in value:
        pygame.display.update()
        sleep(0.1)
        ebin = 0
        for j in range(len(value)):
            if rspace[ebin] >= i:
                if(rspace[ebin] == capacity): ytxt = 300
                else: ytxt -= 25
                pygame.draw.rect(screen, color,
                                 pygame.Rect(sp + ebin*w, round(600 - h  +(rspace[ebin] - i )), w - 10, i-2))
                rspace[ebin] -= i
                break
            else:
                ebin += 1
            if color == RED:
                color = BLUE
            else:
                color = RED
    running = False
    count = 0
    for k in rspace:
        if k != capacity:
            count += 1
        else:
            break
    font = pygame.font.SysFont(None, 50)
    img = font.render(str(count) + " Bins Used To Store " + str(bins) + " Items", True, WHITE)
    screen.blit(img, (200, 300))
    pygame.display.update()

print(rspace)
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
