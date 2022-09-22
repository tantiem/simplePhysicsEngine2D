#Helpful for starting a new pygame project.
from distutils.log import debug
import pygame
import pygame.locals as locs
import os.path

#Physics engine:
import PhysicsEngine
from EntityJS import PhysicsEntity
from EntityJS import EnitityBodyType, EntityResolutionType

class EntityTrackingVisual:
    def __init__(self,entity:PhysicsEntity) -> None:
        self.entity = entity
        self.rect = pygame.rect.Rect(entity.getLeft(),entity.getTop(),entity.width,entity.height)
    def update(self):
        self.rect = pygame.rect.Rect(self.entity.getLeft(),self.entity.getTop(),self.entity.width,self.entity.height)
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,self.rect)

pygame.init()

FPS = 60
FPSclock = pygame.time.Clock()

physicsEngine = PhysicsEngine.PhysicsEngine()

entity1 = PhysicsEntity(0,20,40,EntityResolutionType["ELASTIC"],EnitityBodyType["DYNAMIC"])
entity1graphic = EntityTrackingVisual(entity1)

physicsEngine.addEntity(entity1)

#Create physics entities and respective objects

scrX = 1080
scrY = 720

screen = pygame.display.set_mode((scrX, scrY))

#A basic camera operated with arrow keys/wasd

obj_count = 0

running = True
while running:
    '''Held down key input
    ALSO we are doing some neat camera movement right here specifically, acceleration and stuff so far.'''
    held_keys = pygame.key.get_pressed()


    if held_keys[pygame.K_UP]:
        pass
    if held_keys[pygame.K_DOWN]:
        pass
    if held_keys[pygame.K_LEFT]:
        pass
    if held_keys[pygame.K_RIGHT]:
        pass

    '''Start input'''
    for event in pygame.event.get():
        if event.type == locs.QUIT:
            running = False
        if event.type == locs.KEYDOWN:
            '''Key Presses'''
            pass
        if event.type == locs.MOUSEBUTTONDOWN:
            '''Mouse Cliques'''
            pass
        if event.type == locs.MOUSEMOTION:
            pass
            '''Mouse Movement'''
    '''While loop updates'''
    screen.fill((255, 255, 255))
    '''DrawStuff'''
    physicsEngine.step(FPSclock.get_fps()/60)
    entity1graphic.update()
    entity1graphic.draw(screen,pygame.color.Color(100,100,50))
    
    '''Updating done'''
    pygame.display.flip()
    FPSclock.tick(FPS)
else:
    pygame.quit()