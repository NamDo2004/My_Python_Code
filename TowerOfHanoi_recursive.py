
import pygame
import sys
# game constants
delay_ms = 1200
WIDTH = 1000
HEIGHT = 800
H_SPACING = WIDTH/4     
V_SPACING = 12          
V_GAP = 2               


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)


NUM_DISCS = 0
while NUM_DISCS == 0:
    temp = input("Enter desired number of discs (1-20): ")
    try:
        NUM_DISCS = int(temp)
    except:
        pass


FPS = 0
while FPS == 0:
    temp = input("Enter simulation speed(0.1-100000): ")
    try:
        FPS = float(temp)
    except:
        pass

print(NUM_DISCS,"chosen")


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("py towers of hanoi")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()


for i in range(1,4):
    width = 0.98*H_SPACING
    hpos = i*H_SPACING-width/2
    
    stack = pygame.sprite.Sprite()
    stack.image = pygame.Surface((width, 5))
    stack.image.fill(YELLOW)
    stack.rect = stack.image.get_rect()
    stack.rect.x = hpos
    stack.rect.y = HEIGHT-V_SPACING*3
    all_sprites.add(stack)



discs = []  
stack = []  
            


for i in range(NUM_DISCS):
    width = H_SPACING - i*H_SPACING/(1.6*NUM_DISCS)
    vpos = HEIGHT-V_SPACING*(i+4)
    
    disc_sprite = pygame.sprite.Sprite()
    disc_sprite.image = pygame.Surface((width,V_SPACING-V_GAP))
    disc_sprite.image.fill(GREEN)
    disc_sprite.rect = disc_sprite.image.get_rect()
    disc_sprite.rect.x = H_SPACING-width/2
    disc_sprite.rect.y = vpos
    
    discs.append(disc_sprite)
    stack.append(1)
    all_sprites.add(disc_sprite)


def blocking_id(disc_id, destination):
    
    for i in range(disc_id+1, NUM_DISCS):
        if stack[i] == destination:
            return i
    return None


def new_destination(disc_id, destination):
    
    if stack[disc_id]!=1 and destination!=1:
        return 1
    if stack[disc_id]!=2 and destination!=2:
        return 2
    if stack[disc_id]!=3 and destination!=3:
        return 3
    

def moveable(disc_id):
    
    for i in range((disc_id+1), NUM_DISCS):
        if stack[i] == stack[disc_id]:
            return False
    return True


def move_disc(disc_id, destination):
    width = H_SPACING - disc_id*H_SPACING/(1.6*NUM_DISCS)
    hpos = destination*H_SPACING-width/2
    
    discs[disc_id].rect.x = hpos

    
    j = 0
    for i in range(0, disc_id):
        if stack[i] == destination:
            j += 1
    vpos = HEIGHT-V_SPACING*(j+4)
    discs[disc_id].rect.y = vpos

    stack[disc_id] = destination
    
    

def move(disc_id, destination):

    
    if stack[disc_id] == destination:
        return move(disc_id+1,destination)
    
    
    if(moveable(disc_id)):
        
        blocker = blocking_id(disc_id, destination)
        if(blocker==None):
            move_disc(disc_id, destination)
            return disc_id
        else:
        
            return move(blocker, new_destination(disc_id, destination))
        
    
    else:
        return move(disc_id+1, new_destination(disc_id, destination))




cur_disc = 0                
while cur_disc < NUM_DISCS:
    
    
    clock.tick(FPS)
     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    all_sprites.update()
    
    
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

   
    disc_id = move(cur_disc,3)
    
    if disc_id == cur_disc:         
        print("Moved disc",disc_id)
        cur_disc += 1               
        pygame.time.delay(delay_ms)


all_sprites.update()

screen.fill(BLACK)
all_sprites.draw(screen)
pygame.display.update()

input("Simulation complete (press enter):")
pygame.quit()
quit()