# Anders Poirel

import numpy as np

# Runtime: 108 ms, faster than 7.03% of Python3 online submissions for Unique Paths.
# Memory Usage: 30.6 MB, less than 7.05% of Python3 online submissions for Unique Paths.
class SolutionDP:
    def _getNumPaths(self, sols: np.ndarray, row: int, col: int) -> int:
        """
        Returns number of paths from (row, cols) to (0,-)
        Solutions are memoized in array sols
        """
        if sols[row, col] != -1:
            return sols[row,col] 
        else:
            num_paths = 0
            if (row == 0) and (col == 0): # bottom of recursion - we've found unique path
                num_paths = 1
            if row != 0:
                num_paths += self._getNumPaths(sols, row-1, col)
            if col != 0 :
                num_paths += + self._getNumPaths(sols, row, col-1)
            sols[row, col] =  num_paths
            
        return sols[row, col]
    
    def uniquePaths(self, m: int, n: int) -> int:
        sols = np.full(shape=(m,n), fill_value=-1, dtype=np.int32)
        
        return self._getNumPaths(sols, m-1, n-1) 

# TODO
#
class SolutionMath:
    def uniquePaths(self, m: int, n: int) -> int:
        pass