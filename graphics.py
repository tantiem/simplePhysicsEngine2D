#Helpful for starting a new pygame project.
from distutils.log import debug
from xml.dom.minidom import Entity
import pygame
import pygame.locals as locs
import os.path

#Physics engine:
import PhysicsEngine
from EntityJS import PhysicsEntity
from EntityJS import EntityBodyType, EntityResolutionType

class EntityTrackingVisual:
    def __init__(self,entity:PhysicsEntity) -> None:
        self.entity = entity
        self.rect = pygame.rect.Rect(entity.getLeft(),entity.getTop(),entity.width,entity.height)
    def update(self):
        self.rect = pygame.rect.Rect(self.entity.getLeft(),self.entity.getTop(),self.entity.width,self.entity.height)
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,self.rect)

pygame.init()

scrX = 1080
scrY = 720

screen = pygame.display.set_mode((scrX, scrY))

FPS = 60
FPSclock = pygame.time.Clock()

physicsEngine = PhysicsEngine.PhysicsEngine()

entity1 = PhysicsEntity(0,20,40,EntityResolutionType["ELASTIC"],EntityBodyType["DYNAMIC"])
entity1.x = 100
entity1graphic = EntityTrackingVisual(entity1)

entity2 = PhysicsEntity(1,500,40,EntityResolutionType["ELASTIC"],EntityBodyType["KINEMATIC"])
entity2.y = 500
entity2graphic = EntityTrackingVisual(entity2)

entity3 = PhysicsEntity(2,30,30,EntityResolutionType["ELASTIC"],EntityBodyType["DYNAMIC"])
entity3.x = 300
entity3graphic = EntityTrackingVisual(entity3)

entity4 = PhysicsEntity(0,20,40,EntityResolutionType["ELASTIC"],EntityBodyType["DYNAMIC"])
entity4.x = 150
entity4graphic = EntityTrackingVisual(entity4)

physicsEngine.addEntity(entity1)
physicsEngine.addEntity(entity2)
physicsEngine.addEntity(entity3)
physicsEngine.addEntity(entity4)

#Create physics entities and respective objects



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
        entity1.x -= 3
    if held_keys[pygame.K_RIGHT]:
        entity1.x += 3

    '''Start input'''
    for event in pygame.event.get():
        if event.type == locs.QUIT:
            running = False
        if event.type == locs.KEYDOWN:
            '''Key Presses'''
            if event.key == locs.K_SPACE:
                entity1.vy = -10
        
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
    entity2graphic.update()
    entity2graphic.draw(screen,pygame.color.Color(10,10,10))
    entity3graphic.update()
    entity3graphic.draw(screen,pygame.color.Color(140,20,50))
    entity4graphic.update()
    entity4graphic.draw(screen,pygame.color.Color(50,60,40))
    
    '''Updating done'''
    pygame.display.flip()
    FPSclock.tick(FPS)
else:
    pygame.quit()