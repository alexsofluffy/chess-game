import pygame
from game import Chess
from piece import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board

pygame.init()
screen_width = 740
screen_height = 740
win = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
pygame.display.set_caption('Chess')
b_pawn = pygame.image.load('assets/b_pawn.png')
b_rook = pygame.image.load('assets/b_rook.png')
b_knight = pygame.image.load('assets/b_knight.png')
b_bishop = pygame.image.load('assets/b_bishop.png')
b_queen = pygame.image.load('assets/b_queen.png')
b_king = pygame.image.load('assets/b_king.png')
w_pawn = pygame.image.load('assets/w_pawn.png')
w_rook = pygame.image.load('assets/w_rook.png')
w_knight = pygame.image.load('assets/w_knight.png')
w_bishop = pygame.image.load('assets/w_bishop.png')
w_queen = pygame.image.load('assets/w_queen.png')
w_king = pygame.image.load('assets/w_king.png')

clientNumber = 0

grid_key = {
    0: (91, 160),
    1: (161, 230),
    2: (231, 300),
    3: (301, 370),
    4: (371, 440),
    5: (441, 510),
    6: (511, 580),
    7: (581, 650)
}


class ChessImg:
    def __init__(self, row, col, image):
        self.row = row
        self.col = col
        self.image = image


game = Chess()

grid = [['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_']]

grid[1][0] = ChessImg(1, 0, b_pawn)
grid[1][1] = ChessImg(1, 1, b_pawn)
grid[1][2] = ChessImg(1, 2, b_pawn)
grid[1][3] = ChessImg(1, 3, b_pawn)
grid[1][4] = ChessImg(1, 4, b_pawn)
grid[1][5] = ChessImg(1, 5, b_pawn)
grid[1][6] = ChessImg(1, 6, b_pawn)
grid[1][7] = ChessImg(1, 7, b_pawn)
grid[0][0] = ChessImg(0, 0, b_rook)
grid[0][7] = ChessImg(0, 7, b_rook)
grid[0][1] = ChessImg(0, 1, b_knight)
grid[0][6] = ChessImg(0, 6, b_knight)
grid[0][2] = ChessImg(0, 2, b_bishop)
grid[0][5] = ChessImg(0, 5, b_bishop)
grid[0][3] = ChessImg(0, 3, b_queen)
grid[0][4] = ChessImg(0, 4, b_king)

grid[6][0] = ChessImg(6, 0, w_pawn)
grid[6][1] = ChessImg(6, 1, w_pawn)
grid[6][2] = ChessImg(6, 2, w_pawn)
grid[6][3] = ChessImg(6, 3, w_pawn)
grid[6][4] = ChessImg(6, 4, w_pawn)
grid[6][5] = ChessImg(6, 5, w_pawn)
grid[6][6] = ChessImg(6, 6, w_pawn)
grid[6][7] = ChessImg(6, 7, w_pawn)
grid[7][0] = ChessImg(7, 0, w_rook)
grid[7][7] = ChessImg(7, 7, w_rook)
grid[7][1] = ChessImg(7, 1, w_knight)
grid[7][6] = ChessImg(7, 6, w_knight)
grid[7][2] = ChessImg(7, 2, w_bishop)
grid[7][5] = ChessImg(7, 5, w_bishop)
grid[7][3] = ChessImg(7, 3, w_queen)
grid[7][4] = ChessImg(7, 4, w_king)


my_font = pygame.font.SysFont("arial", 30)
quit_msg = my_font.render("Press q to quit", True, (255, 255, 255))
player_color = "white"
opponent_color = "black"
player_msg = my_font.render("You are {color}".format(color=player_color),
                            True, (255, 0, 0))
indicate_square_from = False


def redrawWindow(mouse_x=None, mouse_y=None):
    win.fill((0, 0, 0))
    for i in range(8):
        y = 70 * i + 90
        for j in range(8):
            x = 70 * j + 90
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(win, (221, 219, 197), (x, y, 70, 70))
                else:
                    pygame.draw.rect(win, (79, 115, 69), (x, y, 70, 70))
            else:
                if j % 2 == 0:
                    pygame.draw.rect(win, (79, 115, 69), (x, y, 70, 70))
                else:
                    pygame.draw.rect(win, (221, 219, 197), (x, y, 70, 70))
    win.blit(quit_msg, (20, 20))
    win.blit(player_msg, (300, 50))
    coor_msg = my_font.render(str(mouse_x) + ", " + str(mouse_y), True, (0, 255, 0))
    win.blit(coor_msg, (600, 50))

    if indicate_square_from is True:
        pygame.draw.rect(win, (255, 255, 194),
                         (grid_key.get(mouse_y)[0] - 1,
                          grid_key.get(mouse_x)[0] - 1, 70, 70))

    for i in range(8):
        for j in range(8):
            if grid[i][j] != '_':
                win.blit(grid[i][j].image, (grid_key.get(j)[0] + 3,
                                            grid_key.get(i)[0] + 3))




    pygame.display.update(win)


def main():







    mouse_x = None
    mouse_y = None

    mouse_x2 = None
    mouse_y2 = None

    global indicate_square_from








    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if indicate_square_from is True:
                    mouse_pos2 = pygame.mouse.get_pos()
                    if 90 <= mouse_pos2[0] <= 650 and 90 <= mouse_pos2[1] <= 650:
                        for key, value in grid_key.items():
                            if value[0] <= mouse_pos2[1] <= value[1]:
                                mouse_x2 = key
                            if value[0] <= mouse_pos2[0] <= value[1]:
                                mouse_y2 = key
                    else:
                        mouse_x = None
                        mouse_y = None
                        indicate_square_from = False
                        continue
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    if 90 <= mouse_pos[0] <= 650 and 90 <= mouse_pos[1] <= 650:
                        for key, value in grid_key.items():
                            if value[0] <= mouse_pos[1] <= value[1]:
                                mouse_x = key
                            if value[0] <= mouse_pos[0] <= value[1]:
                                mouse_y = key
                    else:
                        mouse_x = None
                        mouse_y = None


        if mouse_x2 is not None and mouse_y2 is not None:
            if game.move(mouse_x, mouse_y, mouse_x2, mouse_y2) is True:
                piece_image = grid[mouse_x][mouse_y]
                grid[mouse_x][mouse_y] = '_'
                grid[mouse_x2][mouse_y2] = piece_image
                mouse_x = None
                mouse_y = None
                mouse_x2 = None
                mouse_y2 = None
                indicate_square_from = False
                continue
            else:
                mouse_x = None
                mouse_y = None
                mouse_x2 = None
                mouse_y2 = None
                indicate_square_from = False
                continue


        else:
            if mouse_x is not None and mouse_y is not None:
                if game.board[mouse_x][mouse_y] != '_':
                    if game.turn == 'w':
                        if game.board[mouse_x][mouse_y].color == 'w':
                            indicate_square_from = True
                    if game.turn == 'b':
                        if game.board[mouse_x][mouse_y].color == 'b':
                            indicate_square_from = True

            redrawWindow(mouse_x, mouse_y)


main()