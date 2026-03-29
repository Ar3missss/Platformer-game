import sys
import pygame 
from scripts.utils import load_image , load_images 
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
      
    def __init__(self):
        pygame.init()

        self.caption = pygame.display.set_caption("NINJA GAME")
        
        self.screen = pygame.display.set_mode((640,480))

        # We use .Surface to get a Blank Image here we get a blank image of dimension 320,240
        # The Idea of creating 2nd display is that we can render on smaller display that is on self.display and then scale it up to the self.screen
        # We do this create a pixel Art Effect

        self.display = pygame.Surface((320,240))
        
        self.clock = pygame.time.Clock()

        self.movement = [False,False]

        self.assets = {
            'decor' : load_images('tiles/decor'),  # ('tiles/decor') this is our path
            'grass' : load_images('tiles/grass'), 
            'large_decor' : load_images('tiles/large_decor'), 
            'spawners' : load_images('tiles/spawners'),
            'stone' : load_images('tiles/stone'), 
            'player' : load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50,50),(8,15)) # Calling PhyscisEntity Class (self, game, e_type, pos, size)

        self.tilemap = Tilemap(self)

    def run(self):             
        while True:
            self.display.fill((14,219,248))

            self.tilemap.render(self.display)

            self.player.update((self.movement[1]-self.movement[0],0)) # (x,y)

            self.player.render(self.display) # self.player is a physicsEntity object so this object has access to render() and update() methods
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0))   
            self.clock.tick(60)
            pygame.display.update()

if __name__ == "__main__":
    Game().run()