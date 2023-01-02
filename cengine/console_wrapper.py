def board_wrapper(board):
    """ Wraps the board with coordinates """
    header = "      A     B     C     D     E     F     G     H\n"
    footer = f"\n{header}"

    board_length = len(header) + 6
    header += board_length * "-"
    footer = board_length * "-" + footer

    rows = "\n"
    for i, row in enumerate(board):
        row_number = 8 - i
        rows += f"{row_number} | {row} | {row_number}\n"
    
    board = header + rows + footer
    return board


def translate_coordinates(chess_remap: dict, chess_coordinates: str):
    """ user input eg. A1  ['A', '1'] returns as 0, 0 to get correct list position """
    column, row = list(chess_coordinates)
    return chess_remap[row], chess_remap[column]
