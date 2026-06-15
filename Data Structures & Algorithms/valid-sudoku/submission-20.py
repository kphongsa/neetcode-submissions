class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row check, all x indexs for each y index
        for i in range(9):
            row = set()

            for j in range(9):
                if (board[i][j] == "."): 
                    pass
                elif (board[i][j] not in row ):
                    row.add(board[i][j])
                else:
                    return False
                

        #column check, all y indexs for each x index
        for i in range(9):
            col = set()

            for j in range(9):
                if(board[j][i] == "."): 
                    pass
                elif (board[j][i] not in col):
                    col.add(board[j][i])
                else:
                    return False
                

        #grid check
            #how can we store data in the gird? 
            #smth to track the index
            #one set for each square?
                #floor divide by 3 to get a square
            #then iterate through the entire grid?

        for x in range(0, 7, 3):
            for y in range(0, 7, 3): 
                square = set()
                for i in range(3): 
                    for j in range(3): 
                        if(board[i+x][j+y] == "."): 
                            pass
                        elif (board[i+x][j+y] not in square): 
                            square.add(board[i+x][j+y])
                        else: 
                            return False

        return True

                
