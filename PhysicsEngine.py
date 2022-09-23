from CollisionDetector import CollisionDetector
from CollisionResolver import CollisionResolver
import EntityJS

GRAVITY_X = 0
GRAVITY_Y = 1

class PhysicsEngine:
    def __init__(self,entities: list[EntityJS.PhysicsEntity] = []) -> None:
        self.entities = entities
        self.entityCount = len(entities)

    def addEntity(self,entity):
        self.entityCount = self.entityCount + 1
        entity.id = self.entityCount
        print(f"entity id added: {entity.id}")
        self.entities.append(entity)

    def step(self,elapsed):
        gx = GRAVITY_X * elapsed
        gy = GRAVITY_Y * elapsed
        #Time passes, objects move. (or dont)
        for entity in self.entities:
            if entity.bodyType == EntityJS.EntityBodyType["DYNAMIC"]:
                entity.vx += entity.ax * elapsed + gx
                entity.vy += entity.ay * elapsed + gy
                entity.x  += entity.vx * elapsed
                entity.y  += entity.vy * elapsed
                continue
            elif entity.bodyType == EntityJS.EntityBodyType["KINEMATIC"]:
                entity.vx += entity.ax * elapsed
                entity.vy += entity.ay * elapsed
                entity.x  += entity.vx * elapsed
                entity.y  += entity.vy * elapsed
                continue

        collisions = CollisionDetector.getCollisions(self.entities)
        #At this point, we now have gone through collision detection for all entities

        if (len(collisions) > 0):
            #if there are any collisions:
            for key in collisions:
                col:EntityJS.Collision = collisions[key]
                #resolve, where the left hand will be affected.
                CollisionResolver.resolve(col.entity1,col.entity2)
    
