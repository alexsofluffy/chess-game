import pygame
from game import Chess
from piece import Pawn, Rook, Knight, Bishop, Queen, King
from board import Board


# Initializes all imported Pygame modules and the display window
pygame.init()
screen_width = 740
screen_height = 740
win = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
pygame.display.set_caption('Chess')
# Loads all images stored in 'root/assets' folder
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

# Initializes a new game of chess.
game = Chess()
# Initializes a grid for storing the images of all the chess pieces.
grid = [['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_']]
# Key used for mapping out the coordinates of each individual square on grid.
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
    """Represents an image of a chess piece."""
    def __init__(self, image):
        """Creates a new chess piece image.

        Keyword arguments:
        image -- the actual image file for the piece
        """
        self.image = image


# Creates and assigns images of the corresponding chess pieces on the game
# board, onto the game grid.
grid[1][0] = ChessImg(b_pawn)
grid[1][1] = ChessImg(b_pawn)
grid[1][2] = ChessImg(b_pawn)
grid[1][3] = ChessImg(b_pawn)
grid[1][4] = ChessImg(b_pawn)
grid[1][5] = ChessImg(b_pawn)
grid[1][6] = ChessImg(b_pawn)
grid[1][7] = ChessImg(b_pawn)
grid[0][0] = ChessImg(b_rook)
grid[0][7] = ChessImg(b_rook)
grid[0][1] = ChessImg(b_knight)
grid[0][6] = ChessImg(b_knight)
grid[0][2] = ChessImg(b_bishop)
grid[0][5] = ChessImg(b_bishop)
grid[0][3] = ChessImg(b_queen)
grid[0][4] = ChessImg(b_king)
grid[6][0] = ChessImg(w_pawn)
grid[6][1] = ChessImg(w_pawn)
grid[6][2] = ChessImg(w_pawn)
grid[6][3] = ChessImg(w_pawn)
grid[6][4] = ChessImg(w_pawn)
grid[6][5] = ChessImg(w_pawn)
grid[6][6] = ChessImg(w_pawn)
grid[6][7] = ChessImg(w_pawn)
grid[7][0] = ChessImg(w_rook)
grid[7][7] = ChessImg(w_rook)
grid[7][1] = ChessImg(w_knight)
grid[7][6] = ChessImg(w_knight)
grid[7][2] = ChessImg(w_bishop)
grid[7][5] = ChessImg(w_bishop)
grid[7][3] = ChessImg(w_queen)
grid[7][4] = ChessImg(w_king)

# Global variables live here.
indicate_square_from = False
indicate_square_to = False
pawn_selected = False
king_selected = False
promotion = False

# UI and display fonts live here.
my_font = pygame.font.SysFont("arial", 30)
quit_msg = my_font.render("Press q to quit", True, (255, 255, 255))
player_color = "white"
opponent_color = "black"
player_msg = my_font.render("You are {color}".format(color=player_color),
                            True, (255, 0, 0))


def redrawWindow(mouse_x=None, mouse_y=None, x_copy=None, y_copy=None,
                 x2_copy=None, y2_copy=None):
    """Updates/re-draws the client window with the chess board, UI elements and
    chess images at their most current positions.

    Keyword arguments:
    mouse_x -- x position of mouse when an image is selected
    mouse_y -- y position of mouse when an image is selected
    x_copy -- copy of x position of square that piece is moving from
    y_copy -- copy of y position of square that piece is moving from
    x2_copy -- copy of x position of square that piece is moving to
    y2_copy -- copy of y position of square that piece is moving to
    """
    win.fill((0, 0, 0))
    win.blit(quit_msg, (20, 20))
    win.blit(player_msg, (302, 50))
    # coor_msg used for testing purposes to locate current mouse coordinates.
    # coor_msg = my_font.render(str(mouse_x) + ", " + str(mouse_y), True,
    #                           (0, 255, 0))
    # win.blit(coor_msg, (600, 50))

    # Draws all the squares on the chess grid.
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

    # Draws indicators at the squares that the chess images are moving from/to.
    if indicate_square_from is True:
        pygame.draw.rect(win, (255, 255, 194),
                         (grid_key.get(mouse_y)[0] - 1,
                          grid_key.get(mouse_x)[0] - 1, 70, 70))
    if indicate_square_to is True:
        pygame.draw.rect(win, (255, 255, 194),
                         (grid_key.get(y_copy)[0] - 1,
                          grid_key.get(x_copy)[0] - 1, 70, 70))
        pygame.draw.rect(win, (255, 255, 194),
                         (grid_key.get(y2_copy)[0] - 1,
                          grid_key.get(x2_copy)[0] - 1, 70, 70))

    # Blits all the chess images at their most current positions on chess grid.
    for i in range(8):
        for j in range(8):
            if grid[i][j] != '_':
                win.blit(grid[i][j].image, (grid_key.get(j)[0] + 3,
                                            grid_key.get(i)[0] + 3))
    game_status = my_font.render(game.state, True, (255, 0, 0))
    win.blit(game_status, (500, 50))
    pygame.display.update(win)


def main():
    """Main function containing the core logic behind client."""
    # Variables that store the mouse coordinates, which are then passed into
    # the redrawWindow function.
    mouse_x = None
    mouse_y = None
    mouse_x2 = None
    mouse_y2 = None
    x_copy = None
    y_copy = None
    x2_copy = None
    y2_copy = None

    # References to global variables defined at the beginning of the file.
    global indicate_square_from
    global indicate_square_to
    global pawn_selected
    global king_selected
    global promotion

    # Main game loop that runs until user quits or closes client window. To
    # make it easier to follow the logic of this loop, steps are commented in
    # chronological order.
    while True:
        for event in pygame.event.get():
            # Ends program if user closes client window.
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # Ends program if user clicks 'q' key to quit.
                if event.key == pygame.K_q:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Step 4: If indicator is being displayed, that means a valid
                # piece to move has been selected. Afterwards, program stores
                # a second set of x and y coordinates when mouse clicks on a
                # different square. If user clicks outside of grid, all
                # variables reset and loop starts over at step 1.
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
                        if pawn_selected is True:
                            pawn_selected = False
                        if king_selected is True:
                            king_selected = False
                        continue
                else:
                    # Step 1: Updates x and y coordinates of mouse if a square
                    # on grid is clicked. Else, does nothing and display is
                    # refreshed.
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

        # Step 5: With a second set of mouse coordinates, program determines if
        # a move is valid. If so, piece is moved on chess board as well as the
        # corresponding piece image on the chess grid. If move invalid, resets
        # all variables and loop starts over at step 1.
        if mouse_x2 is not None and mouse_y2 is not None:
            if game.move(mouse_x, mouse_y, mouse_x2, mouse_y2) is True:

                # Special rules for en-passant capturing.
                if pawn_selected is True:
                    if game.turn == 'b':  # Meaning white pawn was moved.
                        if mouse_x2 == 0:
                            promotion = True
                        if mouse_x - mouse_x2 == 1:
                            if mouse_y > mouse_y2 and mouse_y - mouse_y2 == 1:
                                if game.board[mouse_x][mouse_y2] == '_':
                                    if grid[mouse_x][mouse_y2] != '_' and \
                                            grid[mouse_x][mouse_y2].image == b_pawn:
                                        grid[mouse_x][mouse_y2] = '_'
                            if mouse_y < mouse_y2 and mouse_y2 - mouse_y == 1:
                                if game.board[mouse_x][mouse_y2] == '_':
                                    if grid[mouse_x][mouse_y2] != '_' and \
                                            grid[mouse_x][mouse_y2].image == b_pawn:
                                        grid[mouse_x][mouse_y2] = '_'
                    if game.turn == 'w':  # Meaning black pawn was moved.
                        if mouse_x2 == 7:
                            promotion = True
                        if mouse_x2 - mouse_x == 1:
                            if mouse_y > mouse_y2 and mouse_y - mouse_y2 == 1:
                                if game.board[mouse_x][mouse_y2] == '_':
                                    if grid[mouse_x][mouse_y2] != '_' and \
                                            grid[mouse_x][mouse_y2].image == w_pawn:
                                        grid[mouse_x][mouse_y2] = '_'
                            if mouse_y < mouse_y2 and mouse_y2 - mouse_y == 1:
                                if game.board[mouse_x][mouse_y2] == '_':
                                    if grid[mouse_x][mouse_y2] != '_' and \
                                            grid[mouse_x][mouse_y2].image == w_pawn:
                                        grid[mouse_x][mouse_y2] = '_'
                    pawn_selected = False

                # Special rules for castling.
                if king_selected is True:
                    if game.turn == 'b':  # Meaning white king was moved.
                        if mouse_x2 == 7 and mouse_y2 == 2:
                            rook_image = grid[7][0]
                            grid[7][0] = '_'
                            grid[7][3] = rook_image
                        if mouse_x2 == 7 and mouse_y2 == 6:
                            rook_image = grid[7][7]
                            grid[7][7] = '_'
                            grid[7][5] = rook_image
                    if game.turn == 'w':  # Meaning black king was moved.
                        if mouse_x2 == 0 and mouse_y2 == 2:
                            rook_image = grid[0][0]
                            grid[0][0] = '_'
                            grid[0][3] = rook_image
                        if mouse_x2 == 0 and mouse_y2 == 6:
                            rook_image = grid[0][7]
                            grid[0][7] = '_'
                            grid[0][5] = rook_image
                    king_selected = False

                piece_image = grid[mouse_x][mouse_y]
                if promotion is True:
                    if game.turn == 'b':
                        piece_image.image = w_queen
                        promotion = False
                    else:
                        piece_image.image = b_queen
                        promotion = False
                grid[mouse_x][mouse_y] = '_'
                grid[mouse_x2][mouse_y2] = piece_image
                x_copy = mouse_x
                y_copy = mouse_y
                x2_copy = mouse_x2
                y2_copy = mouse_y2
                mouse_x = None
                mouse_y = None
                mouse_x2 = None
                mouse_y2 = None
                indicate_square_from = False
                indicate_square_to = True
                redrawWindow(mouse_x, mouse_y, x_copy, y_copy, x2_copy,
                             y2_copy)
                continue
            else:
                mouse_x = None
                mouse_y = None
                mouse_x2 = None
                mouse_y2 = None
                indicate_square_from = False
                if pawn_selected is True:
                    pawn_selected = False
                continue
        else:
            # Step 2: If square selected contains a chess piece of the same
            # color as the player whose turn it is, window is updated with
            # indicator appears showing the piece that is selected. If square
            # is empty or player attempts to select a piece of a different
            # color, no indicator appears.
            if mouse_x is not None and mouse_y is not None:
                if game.board[mouse_x][mouse_y] != '_':
                    if game.turn == 'w':
                        if game.board[mouse_x][mouse_y].color == 'w':
                            indicate_square_from = True
                            if isinstance(game.board[mouse_x][mouse_y], Pawn) \
                                    is True:
                                pawn_selected = True
                            if isinstance(game.board[mouse_x][mouse_y], King) \
                                    is True and \
                                    game.board[mouse_x][mouse_y].moved is False:
                                king_selected = True
                    if game.turn == 'b':
                        if game.board[mouse_x][mouse_y].color == 'b':
                            indicate_square_from = True
                            if isinstance(game.board[mouse_x][mouse_y], Pawn) \
                                    is True:
                                pawn_selected = True
                            if isinstance(game.board[mouse_x][mouse_y], King) \
                                    is True and \
                                    game.board[mouse_x][mouse_y].moved is False:
                                king_selected = True

            # Step 3: Client window is updated with or without indicator.
            if x_copy and y_copy and x2_copy and y2_copy is None:
                redrawWindow(mouse_x, mouse_y)
            else:
                # Step 6: Updates client window. Indicators signifying the
                # squares that the piece moved from/to will remain on board
                # until next move.
                redrawWindow(mouse_x, mouse_y, x_copy, y_copy, x2_copy,
                             y2_copy)


main()