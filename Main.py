import pygame

def main():
    pygame.init()

    # Constants
    ROWS = 8
    COLS = 8
    BOARD_SIZE = 800
    SQUARE_SIZE = BOARD_SIZE // ROWS
    WIDTH, HEIGHT = BOARD_SIZE, BOARD_SIZE
    selected_square = False
    selected_piece, selected_row, selected_col = None, None, None

    # Colors
    LIGHT_COLOR = (220, 220, 220)
    DARK_COLOR = (0, 0, 0)
    HIGHLIGHT_COLOR = (186, 202, 43)

    # Board Grid
    BOARD_GRID = [[0 for col in range(COLS)] for row in range(ROWS)]

    # Turn Tracker
    turn = 0

    font = pygame.font.SysFont("Arial", 50)

    try:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Asher's Chess Game")
        clock = pygame.time.Clock()


        def draw_board():
            for row in range(ROWS):
                for col in range(COLS):
                    if (row + col) % 2 == 0:
                        color = LIGHT_COLOR
                    else:
                        color = DARK_COLOR

                    x = col * SQUARE_SIZE
                    y = row * SQUARE_SIZE

                    pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

        def start_piece_pos():
            for row in range(ROWS):
                for col in range(COLS):

                    # Light Pieces
                    if row == 7 and col == 0 or row == 7 and col == 7:
                        BOARD_GRID[row][col] = 5
                    elif row == 7 and col == 1 or row == 7 and col == 6:
                        BOARD_GRID[row][col] = 3
                    elif row == 7 and col == 2 or row == 7 and col == 5:
                        BOARD_GRID[row][col] = 4
                    elif row == 7 and col == 3:
                        BOARD_GRID[row][col] = 9
                    elif row == 7 and col == 4:
                        BOARD_GRID[row][col] = 10
                    elif row == 6:
                        BOARD_GRID[row][col] = 1

                    # Dark Pieces
                    if row == 0 and col == 0 or row == 0 and col == 7:
                        BOARD_GRID[row][col] = -5
                    elif row == 0 and col == 1 or row == 0 and col == 6:
                        BOARD_GRID[row][col] = -3
                    elif row == 0 and col == 2 or row == 0 and col == 5:
                        BOARD_GRID[row][col] = -4
                    elif row == 0 and col == 3:
                        BOARD_GRID[row][col] = -9
                    elif row == 0 and col == 4:
                        BOARD_GRID[row][col] = -10
                    elif row == 1:
                        BOARD_GRID[row][col] = -1

        def draw_pieces():
            for row in range(ROWS):
                for col in range(COLS):

                    # Light Pieces
                    if BOARD_GRID[row][col] == 1:
                        screen.blit(font.render("P", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == 3:
                        screen.blit(font.render("Kn", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == 4:
                        screen.blit(font.render("B", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == 5:
                        screen.blit(font.render("R", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == 9:
                        screen.blit(font.render("Q", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == 10:
                        screen.blit(font.render("K", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))

                    # Dark Pieces
                    if BOARD_GRID[row][col] == -1:
                        screen.blit(font.render("P", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == -3:
                        screen.blit(font.render("Kn", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == -4:
                        screen.blit(font.render("B", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == -5:
                        screen.blit(font.render("R", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == -9:
                        screen.blit(font.render("Q", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
                    elif BOARD_GRID[row][col] == -10:
                        screen.blit(font.render("K", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))

        def draw_highlighted_square():
            if selected_square:
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, (selected_col * SQUARE_SIZE, selected_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        def draw_game():
            draw_board()
            draw_highlighted_square()
            draw_pieces()

        def piece_selection(selected_square, selected_row, selected_col, selected_piece, row, col):
            selected_row = row
            selected_col = col
            selected_piece = BOARD_GRID[selected_row][selected_col]
            selected_square = True
            return selected_square, selected_piece, selected_row, selected_col

        def piece_move(selected_square, selected_row, selected_col, selected_piece, row, col):
            temp_row = selected_row
            temp_col = selected_col
            piece = selected_piece
            BOARD_GRID[temp_row][temp_col] = 0
            BOARD_GRID[row][col] = piece
            print("Current board:")
            for board_row in BOARD_GRID:
                print(" ".join(f"{square:>3}" for square in board_row))
            print()


        # Draw the game here.
        start_piece_pos()

        running = True
        while running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left Mouse Click
                    if selected_square == False:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_row = mouse_pos[1] // SQUARE_SIZE
                        mouse_column = mouse_pos[0] // SQUARE_SIZE
                        if turn == 0 and BOARD_GRID[mouse_row][mouse_column] > 0:
                            selected_square, selected_piece, selected_row, selected_col = piece_selection(selected_square, selected_piece, selected_row, selected_col, mouse_row, mouse_column)
                        elif turn == 1 and BOARD_GRID[mouse_row][mouse_column] < 0:
                            selected_square, selected_piece, selected_row, selected_col = piece_selection(selected_square, selected_piece, selected_row, selected_col, mouse_row, mouse_column)

                    elif selected_square == True:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_row = mouse_pos[1] // SQUARE_SIZE
                        mouse_column = mouse_pos[0] // SQUARE_SIZE

                        if selected_piece == 5: # Light Rook Movement
                            if selected_row == mouse_row:
                                piece_move(selected_square, selected_row, selected_col, selected_piece, selected_row, mouse_column)
                                selected_square = False
                                turn = 1
                            elif selected_col == mouse_column:
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, selected_col)
                                selected_square = False
                                turn = 1
                        elif selected_piece == -5: # Dark Rook Movement
                            if selected_row == mouse_row:
                                if BOARD_GRID[mouse_row][mouse_column] > 0:
                                    print("Capture!")
                                piece_move(selected_square, selected_row, selected_col, selected_piece, selected_row, mouse_column)
                                selected_square = False
                                turn = 1
                                print("White's Move!")
                            elif selected_col == mouse_column:
                                print(selected_piece, selected_row, selected_col, mouse_row, mouse_column)
                                if BOARD_GRID[mouse_row][mouse_column] > 0:
                                    print("Capture!")
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, selected_col)
                                selected_square = False
                                turn = 0
                                print("White's Move!")

                        if selected_piece == 1: # Light Pawn Movement
                            if (selected_col == mouse_column and (selected_row - 1) == mouse_row) or (selected_row == 6 and (selected_col == mouse_column and (selected_row - 1 == mouse_row or selected_row - 2 == mouse_row))):
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, selected_col)
                                selected_square = False
                                turn = 1
                            elif selected_row - 1 == mouse_row and (selected_col - 1 == mouse_column or selected_col + 1 == mouse_column) and BOARD_GRID[mouse_row][mouse_column] < 0:
                                if selected_row == 0:
                                    piece_move(selected_square, selected_row, selected_col, 9, selected_row, mouse_column)
                                    selected_square = False
                                    turn = 1
                                else:
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_column)
                                    selected_square = False
                                    turn = 1
                        elif selected_piece == -1: # Dark Pawn Movement
                            if (selected_col == mouse_column and (selected_row + 1) == mouse_row) or (selected_row == 1 and (selected_col == mouse_column and (selected_row + 1 == mouse_row or selected_row + 2 == mouse_row))):
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, selected_col)
                                selected_square = False
                                turn = 0
                            elif selected_row + 1 == mouse_row and (selected_col - 1 == mouse_column or selected_col + 1 == mouse_column) and BOARD_GRID[mouse_row][mouse_column] > 0:
                                if selected_row == 0:
                                    piece_move(selected_square, selected_row, selected_col, -9, selected_row, mouse_column)
                                    selected_square = False
                                    turn = 0
                                else:
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_column)
                                    selected_square = False
                                    turn = 0

                        if selected_piece == 3:
                            if (selected_col + 1 == mouse_column or selected_col - 1 == mouse_column) and selected_row + 2 == mouse_row and BOARD_GRID[mouse_row][mouse_column] <= 0:
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_column)






                        else:

                            if selected_piece >= 0 and BOARD_GRID[mouse_row][mouse_column] <= 0:
                                if BOARD_GRID[mouse_row][mouse_column] < 0:
                                    print("Capture!")
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_column)
                                selected_square = False
                                turn = 1
                            elif selected_piece <= 0 and BOARD_GRID[mouse_row][mouse_column] >= 0:
                                if BOARD_GRID[mouse_row][mouse_column] > 0:
                                    print("Capture!")
                                piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_column)
                                selected_square = False
                                turn = 0


                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3: # Right Mouse Click
                    if selected_square == True:
                        selected_square = False

            if not running:
                break


            draw_game()
            clock.tick(60)
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
