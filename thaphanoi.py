import pygame, sys, time

pygame.init()
pygame.display.set_caption("Thap Ha Noi")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 60

# game vars:
steps = 0
n_disks = 3
disks = []
towers_midx = [120, 320, 520]

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold = (239, 229, 51)
blue = (78,162,196) 
grey = (170, 170, 170)
green = (77, 206, 145)

def blit_text(screen, text, midtop, aa=True, font=None, font_name=None, size=None, color=(255,0,0)):
    if font is None:
        font = pygame.font.SysFont(font_name, size)
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)

def menu_screen():
    global screen, n_disks, game_done
    menu_done = False
    while not menu_done:
        screen.fill(white)
        blit_text(screen, 'Thap Ha Noi', (323,122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Thap Ha Noi', (320,120), font_name='sans serif', size=90, color=gold)
        blit_text(screen, 'Use arrow keys to select difficulty:', (320, 220), font_name='sans serif', size=30, color=black)
        blit_text(screen, str(n_disks), (320, 260), font_name='sans serif', size=40, color=blue)
        blit_text(screen, 'Press ENTER to continue', (320, 320), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    n_disks += 1
                    if n_disks > 6:
                        n_disks = 6
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    n_disks -= 1
                    if n_disks < 1:
                        n_disks = 1
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)

def game_over():
    global screen, steps
    screen.fill(white)
    min_steps = 2**n_disks - 1
    blit_text(screen, 'You Won!', (320, 200), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'You Won!', (322, 202), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'Your Steps: ' + str(steps), (320, 360), font_name='mono', size=30, color=black)
    blit_text(screen, 'Minimum Steps: ' + str(min_steps), (320, 390), font_name='mono', size=30, color=red)
    if min_steps == steps:
        blit_text(screen, 'You finished in minimum steps!', (320, 300), font_name='mono', size=26, color=green)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def draw_towers():
    global screen
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160, 20))
        pygame.draw.rect(screen, grey, pygame.Rect(xpos+75, 200, 10, 200))
    blit_text(screen, 'Start', (towers_midx[0], 403), font_name='mono', size=14, color=black)
    blit_text(screen, 'Finish', (towers_midx[2], 403), font_name='mono', size=14, color=black)

def make_disks():
    global n_disks, disks
    disks = []
    cao = 20
    ypos = 397 - cao
    width = n_disks * 23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(0, 0, width, cao)
        disk['rect'].midtop = (120, ypos)
        disk['val'] = n_disks - i
        disk['tower'] = 0
        disks.append(disk)
        ypos -= cao + 3
        width -= 23

def draw_disks():
    global screen, disks
    for disk in disks:
        pygame.draw.rect(screen, blue, disk['rect'])
    return

def check_won():
    global disks
    over = True
    for disk in disks:
        if disk['tower'] != 2:
            over = False
    if over:
        time.sleep(0.2)
        game_over()

def reset():
    global steps, pointing_at, floating, floater
    steps = 0
    pointing_at = 0
    floating = False
    floater = 0
    menu_screen()
    make_disks()

menu_screen()
make_disks()

# Auto-solving Towers of Hanoi
def abc(n, source, target, auxiliary):
    global steps  # Declare 'steps' as a global variable
    if n > 0:
        # Move n - 1 disks from source to auxiliary peg
        abc(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        for disk in disks:
            if disk['val'] == n and disk['tower'] == source:
                disk['tower'] = target
                disk['rect'].midtop = (towers_midx[target], 400 - (len([d for d in disks if d['tower'] == target]) * 23))
                time.sleep(0.5)  # Delay to visualize the move
                steps += 1
                screen.fill(white)
                draw_towers()
                draw_disks()
                blit_text(screen, 'Steps: ' + str(steps), (320, 20), font_name='mono', size=30, color=black)
                pygame.display.flip()

        # Move n-1 disks from auxiliary to target peg
        abc(n - 1, auxiliary, target, source)

if not game_done:
    abc(n_disks, 0, 2, 1)

game_over()
