"""
// Rect collision tests the edges of each rect to
// test whether the objects are overlapping the other
CollisionDetector.prototype.collideRect =
    function(collider, collidee) {

    // Store the collider and collidee edges
    var l1 = collider.getLeft();
    var t1 = collider.getTop();
    var r1 = collider.getRight();
    var b1 = collider.getBottom();

    var l2 = collidee.getLeft();
    var t2 = collidee.getTop();
    var r2 = collidee.getRight();
    var b2 = collidee.getBottom();

    // If the any of the edges are beyond any of the
    // others, then we know that the box cannot be
    // colliding
    if (b1 < t2 || t1 > b2 || r1 < l2 || l1 > r2) {
        return false;
    }

    // If the algorithm made it here, it had to collide
    return true;
};
"""

import EntityJS;

class CollisionDetector:
    def __init__(self) -> None:
        pass
    @staticmethod
    def collideRect(collider:EntityJS.PhysicsEntity,collidee:EntityJS.PhysicsEntity):
        #Store collider and collidee edges
        l1 = collider.getLeft()
        t1 = collider.getTop()
        r1 = collider.getRight()
        b1 = collider.getBottom()

        l2 = collidee.getLeft()
        t2 = collidee.getTop()
        r2 = collidee.getRight()
        b2 = collidee.getBottom()

        # If the any of the edges are beyond any of the
        # others, then we know that the box cannot be
        # colliding
        if (b1 < t2 or t1 > b2 or r1 < l2 or l1 > r2):
            return False
        
        #if the algorithm made it here, it had to have collided
        return True
    @staticmethod
    def getCollisions(entities:list[EntityJS.PhysicsEntity]):
        #Here we will need to find all unique collisions between all entities.
        collisionDict = {}
        for entity in entities:
            #Check if the body type is dynamic or kinematic; based on the resolution code,
            #we only want dynamic bodies on the left and kinematic on the right (or slight chance
            # of another dynamic on the right.)
            if entity.bodyType == EntityJS.EntityBodyType["KINEMATIC"]:
                continue
            for other in entities:
                if entity == other:
                    continue
                #Check if a collision occured
                if CollisionDetector.collideRect(entity,other):
                    #skip if this collision is already recorded
                    try:
                        if collisionDict[(entity,other)] or collisionDict[(other,entity)]:
                            continue
                    except KeyError:
                        #Record this collision, store a collision object
                        collisionDict[(entity,other)] = EntityJS.Collision(entity,other)
        return collisionDict





                