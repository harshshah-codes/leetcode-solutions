class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=set()
        col_set=set()
        for r,row in enumerate(board):
            for c,val in enumerate(row):
                if val!='.':
                    if(((r,val) in row_set) or ((c,val) in col_set) or ((r//3,c//3,val) in col_set)):
                        return False
                    else:
                        row_set.add((r,val))
                        col_set.add((c,val))
                        col_set.add((r//3,c//3,val))
        return True