import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)  # (x,y)  We use list(pos) bcz to make position mutable for eg --> if our Player pos is  Player((100,200))it is immutable it becomes [100,200] now its list and mutable then self.pos[0] += 5
        self.size = size
        self.velocity = [0,0]  # Velocity = speed + direction so intially our velocity is [0,0] by speed it means left and right and by direction it means up and down
        
    def rect(self):
        return pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])    
    
    def update(self,tilemap,movement = (0,0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1]) # so here we are giving frame movement its (x,y)


        self.pos[0] += frame_movement[0]*2 # updating x position the of entity
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0]>0:
                    entity_rect.right =rect.left
                if frame_movement [0]<0: 
                    entity_rect.left = rect.right
                self.pos[0] =entity_rect.x
                

        self.pos[1] += frame_movement[1]*2 # updating y postiton of the entity
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1]>0:
                    entity_rect.bottom =rect.top
                if frame_movement [1]<0:
                    entity_rect.top = rect.bottom
                self.pos[1] =entity_rect.y

        self.velocity[1] = min(5,self.velocity[1] +0.1) # Created a limit of 5 for smooth falling

    def render(self,surf):
        surf.blit(self.game.assets['player'],self.pos)  # (img/source,position)