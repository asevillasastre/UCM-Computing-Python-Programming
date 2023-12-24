def is_threaten(piece, ori_col, ori_row, dest_col, dest_row):
    
    """
    Given a chess piece, an initial pigeonhole and a final pigeonhole, 
    that function sais of the piece can be moved.
    
    Parameters
    ----------
    piece:
        character
        that character denotes a chess piece, being:
        "K"= "king", "R"= "rook", "B"= "bishop", "Q"= "queen", "N"= "knight"
    ori_col, dest_col:
        character
        that characters denote the initial and final number of column 
        (starting on the left of the table), being:
            "a", "b", "c", "d", "e", "f", "g", "h" = 1, 2, 3, 4, 5, 6, 7, 8
        that character only can be "a", "b", "c", "d", "e", "f", "g" or "h"
    ori_row, dest_row:
        int
        that numbers denote the initial and final number of row 
        (starting on the left of the table)
        that character only can be 1, 2, 3, 4, 5, 6, 7 or 8
        
    Returns
    -------
    It returns a boolean value which determines if a piece can be moved to a certain pigeonhole
    
    Example
    -------
    >>> is_threaten("K", "a", 2, "b", 3)
    True
    
    """
    
    ori_col_number, dest_col_number = ord(ori_col) - 96, ord(dest_col) - 96
    #associate an "int" to the character defined in function of the column
    
    if ori_col_number>8 or ori_row>8 or ori_col_number<1 or ori_row<1:
        return None
    #error: original pigeonhole is not defined
    if dest_col_number<1 or dest_row<1 or dest_col_number>8 or dest_row>8:
        return None
    #error: destination pigeonhole is not defined
    if ori_row!=int(ori_row) or dest_row!=int(dest_row):
        return None
    #error: you have introduced a not "int" value
    if (ori_col == dest_col and ori_row == dest_row):
        return None
    #error: there is not any moviement
    
    else:    
    #when every requirement is satisfied:
        
        if piece == "K":
            return (abs(ori_col_number - dest_col_number) or abs(ori_row - dest_row)) <2
        #the increase of column or row only can be 0 or 1
        if piece == "R":
            return (abs(ori_col_number - dest_col_number) and abs(ori_row - dest_row)) ==0
        #the increase of a line must be null
        if piece == "B":
            return (abs(ori_col_number - dest_col_number) == abs(ori_row - dest_row))
        #the increase of column must be equal to row´s one
        if piece == "Q":
            rook_can_move = (abs(ori_col_number - dest_col_number) and abs(ori_row - dest_row)) ==0
            bishop_can_move = (abs(ori_col_number - dest_col_number) == abs(ori_row - dest_row))
            return rook_can_move or bishop_can_move
        #it is valid a movement as a rook and as a bishop
        if piece == "N":
            return (abs(ori_col_number - dest_col_number), abs(ori_row - dest_row)) == ((1, 2) or (2, 1))
        #the increase of a line must be exactly 2 and the remaining one must be 1
        
        else:   
            return N¡
            #error: piece is not defined