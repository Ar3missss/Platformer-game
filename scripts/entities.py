import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)  # (x,y)  We use list(pos) bcz to make position mutable for eg --> if our Player pos is  Player((100,200))it is immutable it becomes [100,200] now its list and mutable then self.pos[0] += 5
        self.size = size
        self.velocity = [0,0]  # Velocity = speed + direction so intially our velocity is [0,0] by speed it means left and right and by direction it means up and down
        
    
    def update(self,movement = (0,0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1]) # so here we are giving frame movement its (x,y) 

        self.pos[0] += frame_movement[0]*5 # updating x position the of entity
        self.pos[1] += frame_movement[1] # updating y postiton of the entity

    def render(self,surf):
        surf.blit(self.game.assets['player'],self.pos)  # (img/source,position)