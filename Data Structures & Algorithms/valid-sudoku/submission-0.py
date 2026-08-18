class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colCache = defaultdict(set);
        boxCache = defaultdict(set);
        for r in range(9):
            rowCache = set();
            for c in range(9):

                currValue = board[r][c];
                if currValue == '.':
                    continue;

                # Check Row Valid   
                if currValue in rowCache:
                    return False;
                rowCache.add(currValue);
                
                # Check Column Valid
                if currValue in colCache[c]:
                    return False;
                colCache[c].add(currValue);

                # Check Box Valid
                box = (r // 3) * 3 + (c // 3)
                if currValue in boxCache[box]:
                    return False;
                boxCache[box].add(currValue);

                

                
        return True;