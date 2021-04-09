import pygame as pg
import os
import numpy as np

pg.init()

class Pieces(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (pos)
        self.image.set_colorkey((255, 0, 0))

        # def update(self, pos):
        #     pass

class Pawn_W(Pieces):
    def __init__(self, image, pos):
        super(Pawn_W, self).__init__(image, pos)

    def update(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            for click in pg.event.get():
                if click.type == pg.MOUSEBUTTONDOWN:
                    coord = pg.mouse.get_pos()
                    self.rect.center = get_coord(coord)


# class King_W(Pieces):
#     def __init__(self, image, pos):
#         super(Pawn_W, self).__init__(image, pos)
#
# class Queen_W(Pieces):
#     def __init__(self, image, pos):
#         super(Pawn_W, self).__init__(image, pos)
#
# class Knight_W(Pieces):
#     def __init__(self, image, pos):
#         super(Pawn_W, self).__init__(image, pos)
#
# class Bishop_W(Pieces):
#     def __init__(self, image, pos):
#         super(Pawn_W, self).__init__(image, pos)
#
# class Rook_W(Pieces):
#     def __init__(self, image, pos):
#         super(Pawn_W, self).__init__(image, pos)
# class Pieces(pg.sprite.Sprite):
#     def __init__(self):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pawn_w
#         self.rect = self.image.get_rect()
#         self.rect.bottomleft = ((0, HEIGHT))
#         self.image.set_colorkey((255, 0, 0))
#
#     def update(self):
#         motion = 5
#         self.rect.x += motion
#         self.rect.y -= motion
#         if self.rect.right > WIDTH or self.rect.left < 0:
#             self.rect.x = 400

def get_coord(pos):
    return (pos[0] % 100 * 100 + 50, pos[0] % 100 * 100 + 50)

# def motion():
#     if event.type == pg.MOUSEBUTTONDOWN:
#         where = get_coord(event.pos)


WIDTH = 800
HEIGHT = 800
FPS = 10
struct = np.arange(64)
struct = struct.reshape(8, 8)


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

board = pg.image.load(os.path.join(img_folder, 'board_1.png'))
board_rect = board.get_rect()
pawn_w = pg.image.load(os.path.join(img_folder, 'pawn_white.png'))
# pawn_w = pg.image.load(os.path.join(img_folder, 'pawn_exp.png'))

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('CHESS')
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()
white_pawns = pg.sprite.Group()
# pieces = Pieces()
# all_sprites.add(pieces)
for i in range(8):
    pawns_w = Pawn_W(pawn_w, (50 + 100 * i, 650))
    all_sprites.add(pawns_w)
    white_pawns.add(pawns_w)

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:


    screen.fill((255, 255, 255))
    screen.blit(board, board_rect)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()

