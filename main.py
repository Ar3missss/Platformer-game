import sys
import pygame 
pygame.init()

WIDTH=640
HEIGHT=480

class main:

    def __init__(self):
        self.caption = pygame.display.set_caption("NINJA GAME")
        
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        
        self.clock = pygame.time.Clock()
        
        self.image = pygame.image.load("/Users/macbookair/Python/Marioo/data/images/clouds/cloud_1.png")

        self.image_pos = [160,260]

    def run(self):             
        while True: 
            self.screen.blit(self.image,self.image_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.clock.tick(60)
            pygame.display.update()


main().run()

if __name__ == "__main__":
    main()