import pygame, random
from time import sleep

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Next-Fit Decreasing Algorithm")

WHITE = (255, 255, 255)
BLUE  = (0,255,0)
RED = (255, 0, 0)
TXT = (190,189,150)


# def display_plot(value):
#     for i in range(0,kk):
#         pygame.draw.line(screen, WHITE, (int(i*(800/kk)) , 600), (int(i*(800/kk)), 600 - value[i]), 3)


# value = []
value = [74,90,29,19,62,53,14,82,10,41,47,67,38,26,30]
value.sort(reverse=True)
rspace = []
bins = 15
capacity = 100
# for i in range(0, bins):
    # value.append(random.randint(1, capacity))
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

    tmp = 1
    for i in value:
        pygame.draw.rect(screen, RED, pygame.Rect(sp, 20, round(w - 10), i))
        font = pygame.font.SysFont(None, 20)
        img = font.render(str(tmp), True, BLUE)
        # screen.blit(img, (sp+w/2, 20))
        sp = sp + w
        tmp+=1

    sp = 0
    cbin = 0
    color = RED
    for i in value:
        pygame.display.update()
        sleep(0.1)
        if rspace[cbin] >= i:
            pygame.draw.rect(screen, color,
                             pygame.Rect(sp, round(600 - h + ((rspace[cbin] - i) )), w-10, i))
            rspace[cbin] -= i
        else:
            cbin += 1
            sp += w
            pygame.draw.rect(screen, color, pygame.Rect(sp, round(600 - (i)) , w - 10, i))
            rspace[cbin] -= i
        print(cbin)
        if color == RED:
            color = BLUE
        else:
            color = RED
    running = False
    count = 0
    for k in rspace:
        if k!=capacity:
            count+=1
        else:
            break
    font = pygame.font.SysFont(None, 50)
    img = font.render(str(count)+ " Bins Used To Store " + str(bins) + " Items", True, WHITE)
    screen.blit(img, (200,300))
    pygame.display.update()

print(rspace)
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
