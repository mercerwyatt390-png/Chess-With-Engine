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
    font = pygame.font.SysFont("Arial", 50)


    # Colors
    LIGHT_COLOR = (220, 220, 220)
    DARK_COLOR = (0, 0, 0)
    HIGHLIGHT_COLOR = (186, 202, 43)

    # Board Grid
    BOARD_GRID = [[0 for col in range(COLS)] for row in range(ROWS)]

    # Dynamic Variables
    turn = 0

    light_check = False
    dark_check = False

    light_king_row = 7
    light_king_col = 4

    dark_king_row = 0
    dark_king_col = 4


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
                        screen.blit(font.render("N", False, "Red"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
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
                        screen.blit(font.render("N", False, "Blue"), (col * SQUARE_SIZE + 35, row * SQUARE_SIZE + 20))
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

        def clear_path_orthogonal(selected_row, selected_col, row, col):
            if selected_row < row:
                for i in range(row - selected_row):
                    if i != 0:
                        if BOARD_GRID[selected_row + i][selected_col] != 0:
                            return False
            elif selected_row > row:
                for i in range(selected_row - row):
                    if i != 0:
                        if BOARD_GRID[selected_row - i][selected_col] != 0:
                            return False
            elif selected_col < col:
                for i in range(col - selected_col):
                    if i != 0:
                        if BOARD_GRID[selected_row][selected_col + i] != 0:
                            return False
            elif selected_col > col:
                for i in range(selected_col - col):
                    if i != 0:
                        if BOARD_GRID[selected_row][selected_col - i] != 0:
                            return False

            return True

        def clear_path_diagonal(selected_row, selected_col, row, col):
            if selected_row < row and selected_col < col:
                for i in range(row - selected_row):
                    if i != 0:
                        if BOARD_GRID[selected_row + i][selected_col + i] != 0:
                            return False
            elif selected_row < row and selected_col > col:
                for i in range(row - selected_row):
                    if i != 0:
                        if BOARD_GRID[selected_row + i][selected_col - i] != 0:
                            return False
            elif selected_row > row and selected_col > col:
                for i in range(selected_row - row):
                    if i != 0:
                        if BOARD_GRID[selected_row - i][selected_col - i] != 0:
                            return False
            elif selected_row > row and selected_col < col:
                for i in range(selected_row - row):
                    if i != 0:
                        if BOARD_GRID[selected_row - i][selected_col + i] != 0:
                            return False
            return True

        def check_checker(light_king_row, light_king_col, dark_king_row, dark_king_col):

            def is_king_attacked(k_row, k_col, is_light_king):

                if is_light_king:
                    enemy_pawn = -1
                    enemy_knight = -3
                    enemy_bishop = -4
                    enemy_rook = -5
                    enemy_queen = -9
                    enemy_king = -10
                else:
                    enemy_pawn = 1
                    enemy_knight = 3
                    enemy_bishop = 4
                    enemy_rook = 5
                    enemy_queen = 9
                    enemy_king = 10

                ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in ortho_dirs:
                    for step in range(1, 8):
                        r, c = k_row + (dr * step), k_col + (dc * step)
                        if 0 <= r < 8 and 0 <= c < 8:
                            piece = BOARD_GRID[r][c]
                            if piece == 0:
                                continue
                            elif piece == enemy_rook or piece == enemy_queen:
                                return True
                            else:
                                break
                        else:
                            break

                diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dr, dc in diag_dirs:
                    for step in range(1, 8):
                        r, c = k_row + (dr * step), k_col + (dc * step)
                        if 0 <= r < 8 and 0 <= c < 8:
                            piece = BOARD_GRID[r][c]
                            if piece == 0:
                                continue
                            elif piece == enemy_bishop or piece == enemy_queen:
                                return True
                            else:
                                break
                        else:
                            break

                knight_offsets = [
                    (-2, -1), (-2, 1), (2, -1), (2, 1),
                    (-1, -2), (1, -2), (-1, 2), (1, 2)
                ]
                for dr, dc in knight_offsets:
                    r, c = k_row + dr, k_col + dc
                    if 0 <= r < 8 and 0 <= c < 8:
                        if BOARD_GRID[r][c] == enemy_knight:
                            return True


                pawn_row_offset = -1 if is_light_king else 1
                pawn_attacks = [
                    (k_row + pawn_row_offset, k_col - 1),
                    (k_row + pawn_row_offset, k_col + 1)
                ]
                for r, c in pawn_attacks:
                    if 0 <= r < 8 and 0 <= c < 8:
                        if BOARD_GRID[r][c] == enemy_pawn:
                            return True

                king_offsets = [
                    (-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, 1), (-1, -1), (1, -1), (1, 1)
                ]

                for dr, dc in king_offsets:
                    r, c = k_row + dr, k_col + dc
                    if 0 <= r < 8 and 0 <= c < 8:
                        if BOARD_GRID[r][c] == enemy_king:
                            return True

                return False  # Safe!

            nonlocal light_check, dark_check
            light_check = is_king_attacked(light_king_row, light_king_col, is_light_king=True)
            dark_check = is_king_attacked(dark_king_row, dark_king_col, is_light_king=False)

            if light_check: print("Light King is in CHECK!")
            if dark_check: print("Dark King is in CHECK!")

        def is_move_legal(start_row, start_col, end_row, end_col, is_light_turn):
            original_start = BOARD_GRID[start_row][start_col]
            original_end = BOARD_GRID[end_row][end_col]

            nonlocal light_king_row, light_king_col, dark_king_row, dark_king_col
            old_lk_row, old_lk_col = light_king_row, light_king_col
            old_dk_row, old_dk_col = dark_king_row, dark_king_col

            BOARD_GRID[start_row][start_col] = 0
            BOARD_GRID[end_row][end_col] = original_start

            if original_start == 10:
                light_king_row, light_king_col = end_row, end_col
            elif original_start == -10:
                dark_king_row, dark_king_col = end_row, end_col

            move_causes_check = False

            check_checker(light_king_row, light_king_col, dark_king_row, dark_king_col)

            if is_light_turn == 0 and light_check:
                move_causes_check = True
            elif is_light_turn == 1 and dark_check:
                move_causes_check = True

            BOARD_GRID[start_row][start_col] = original_start
            BOARD_GRID[end_row][end_col] = original_end
            light_king_row, light_king_col = old_lk_row, old_lk_col
            dark_king_row, dark_king_col = old_dk_row, old_dk_col

            check_checker(light_king_row, light_king_col, dark_king_row, dark_king_col)

            return not move_causes_check



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
                        mouse_col = mouse_pos[0] // SQUARE_SIZE
                        if turn == 0 and BOARD_GRID[mouse_row][mouse_col] > 0:
                            selected_square, selected_piece, selected_row, selected_col = piece_selection(selected_square, selected_piece, selected_row, selected_col, mouse_row, mouse_col)
                        elif turn == 1 and BOARD_GRID[mouse_row][mouse_col] < 0:
                            selected_square, selected_piece, selected_row, selected_col = piece_selection(selected_square, selected_piece, selected_row, selected_col, mouse_row, mouse_col)

                    elif selected_square == True:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_row = mouse_pos[1] // SQUARE_SIZE
                        mouse_col = mouse_pos[0] // SQUARE_SIZE

                        if selected_piece == 5: # Light Rook Movement
                            if (selected_row == mouse_row or selected_col == mouse_col) and BOARD_GRID[mouse_row][mouse_col] <= 0 and clear_path_orthogonal(selected_row, selected_col, mouse_row, mouse_col):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 1
                        elif selected_piece == -5: # Dark Rook Movement
                            if (selected_row == mouse_row or selected_col == mouse_col) and BOARD_GRID[mouse_row][mouse_col] >= 0 and clear_path_orthogonal(selected_row, selected_col, mouse_row, mouse_col):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 0

                        elif selected_piece == 1: # Light Pawn Movement
                            if ((selected_col == mouse_col and (selected_row - 1) == mouse_row) or (selected_row == 6 and (selected_col == mouse_col and (selected_row - 1 == mouse_row or selected_row - 2 == mouse_row)))) and BOARD_GRID[mouse_row][mouse_col] == 0 and clear_path_orthogonal(selected_row, selected_col, mouse_row, mouse_col):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, selected_col)
                                    selected_square = False
                                    turn = 1
                            elif selected_row - 1 == mouse_row and (selected_col - 1 == mouse_col or selected_col + 1 == mouse_col) and BOARD_GRID[mouse_row][mouse_col] < 0:
                                if mouse_row == 0:
                                    if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                        piece_move(selected_square, selected_row, selected_col, 9, mouse_row, mouse_col)
                                        selected_square = False
                                        turn = 1
                                else:
                                    if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                        piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                        selected_square = False
                                        turn = 1
                        elif selected_piece == -1: # Dark Pawn Movement
                            if ((selected_col == mouse_col and (selected_row + 1) == mouse_row) or (selected_row == 1 and (selected_col == mouse_col and (selected_row + 1 == mouse_row or selected_row + 2 == mouse_row)))) and BOARD_GRID[mouse_row][mouse_col] == 0 and clear_path_orthogonal(selected_row, selected_col, mouse_row, mouse_col):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, selected_col)
                                    selected_square = False
                                    turn = 0
                            elif selected_row + 1 == mouse_row and (selected_col - 1 == mouse_col or selected_col + 1 == mouse_col) and BOARD_GRID[mouse_row][mouse_col] > 0:
                                if mouse_row  == 7:
                                    if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                        piece_move(selected_square, selected_row, selected_col, -9, mouse_row, mouse_col)
                                        selected_square = False
                                        turn = 0
                                else:
                                    if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                        piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                        selected_square = False
                                        turn = 0

                        elif selected_piece == 3: # Light Knight Movement
                            if ((selected_col + 1 == mouse_col or selected_col - 1 == mouse_col) and (selected_row - 2 == mouse_row or selected_row + 2 == mouse_row) or
                                (selected_col + 2 == mouse_col or selected_col - 2 == mouse_col) and (selected_row - 1 == mouse_row or selected_row + 1 == mouse_row)) and BOARD_GRID[mouse_row][mouse_col] <= 0:
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 1
                        elif selected_piece == -3: # Dark Knight Movement
                            if ((selected_col + 1 == mouse_col or selected_col - 1 == mouse_col) and (selected_row - 2 == mouse_row or selected_row + 2 == mouse_row) or
                                (selected_col + 2 == mouse_col or selected_col - 2 == mouse_col) and (selected_row - 1 == mouse_row or selected_row + 1 == mouse_row)) and BOARD_GRID[mouse_row][mouse_col] >= 0:
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 0

                        elif selected_piece == 4: # Light Bishop
                            if ((abs(selected_col - mouse_col) == abs(selected_row - mouse_row)) and BOARD_GRID[mouse_row][mouse_col] <= 0 and clear_path_diagonal(selected_row, selected_col, mouse_row, mouse_col)):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 1
                        elif selected_piece == -4: # Light Bishop
                            if ((abs(selected_col - mouse_col) == abs(selected_row - mouse_row)) and BOARD_GRID[mouse_row][mouse_col] >= 0 and clear_path_diagonal(selected_row, selected_col, mouse_row, mouse_col)):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 0

                        elif selected_piece == 9:
                            if ((((selected_row == mouse_row or selected_col == mouse_col) and clear_path_orthogonal(selected_row, selected_col, mouse_row, mouse_col)) or (abs(selected_col - mouse_col) == abs(selected_row - mouse_row)) and clear_path_diagonal(selected_row, selected_col, mouse_row, mouse_col)) and BOARD_GRID[mouse_row][mouse_col] <= 0):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 1
                        elif selected_piece == -9:
                            if ((((selected_row == mouse_row or selected_col == mouse_col) and clear_path_orthogonal(selected_row, selected_col, mouse_row, mouse_col)) or (abs(selected_col - mouse_col) == abs(selected_row - mouse_row)) and clear_path_diagonal(selected_row, selected_col, mouse_row, mouse_col)) and BOARD_GRID[mouse_row][mouse_col] >= 0):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    selected_square = False
                                    turn = 0

                        elif selected_piece == 10:
                            if(((abs(selected_row - mouse_row) + abs(selected_col - mouse_col) == 1) or (abs(selected_row - mouse_row) == 1 and abs(selected_col - mouse_col) == 1)) and BOARD_GRID[mouse_row][mouse_col] <= 0):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    light_king_row = mouse_row
                                    light_king_col = mouse_col
                                    selected_square = False
                                    turn = 1
                        elif selected_piece == -10:
                            if(((abs(selected_row - mouse_row) + abs(selected_col - mouse_col) == 1) or (abs(selected_row - mouse_row) == 1 and abs(selected_col - mouse_col) == 1)) and BOARD_GRID[mouse_row][mouse_col] >= 0):
                                if is_move_legal(selected_row, selected_col, mouse_row, mouse_col, turn):
                                    piece_move(selected_square, selected_row, selected_col, selected_piece, mouse_row, mouse_col)
                                    dark_king_row = mouse_row
                                    dark_king_col = mouse_col
                                    selected_square = False
                                    turn = 0
                        check_checker(light_king_row, light_king_col, dark_king_row, dark_king_col)


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
