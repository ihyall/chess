import pygame as pg
import os
import abc

pg.init()

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



WIDTH = 800
HEIGHT = 800
FPS = 10

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

board = pg.image.load(os.path.join(img_folder, 'board_1.png'))
board_rect = board.get_rect()
# pawn_w = pg.image.load(os.path.join(img_folder, 'pawn_exp.png'))

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('CHESS')
clock = pg.time.Clock()
# all_sprites = pg.sprite.Group()
# pieces = Pieces()
# all_sprites.add(pieces)

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(board, board_rect)
    # all_sprites.update()
    # all_sprites.draw(screen)
    pg.display.flip()

pg.quit()

