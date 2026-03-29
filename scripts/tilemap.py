class Tilemap:
    def __init__(self,game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3+i) + ';10'] = {'type' : 'grass', 'variant' : 0, 'pos' : (3+i,10)} # str(3+i) + ';10'] is our key and {'type' : 'grass', 'variant' : 1, 'pos' : (3+i,10)} is our value
            self.tilemap['10;'+str(5+i)] = {'type' : 'stone', 'variant' : 0, 'pos' : (10,5+i)}

    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']],tile['pos'])
        
        #  we multiply pos with tile size bcz we have to make a grid like :-
        #  (0,0)   (16,0)   (32,0)   (48,0)
        #  (0,16)  (16,16)  (32,16)  (48,16)
        #  if we dont multiply our tiles will overlap in oneplace
        
        for loc in self.tilemap: # This means everything that is inside self.tilemap put them into loc one by one (tilemap ke andar jo jo items hain, unhe ek ek karke loc me daalte jao)
            tile = self.tilemap[loc] # This means Put loc key data into tile 
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size)) #.blit(surface,position)
