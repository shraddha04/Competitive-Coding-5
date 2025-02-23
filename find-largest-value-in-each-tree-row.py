# Time Complexity : O(n*m) - n is the number of rows and m is the number of cols
# Since n and m are constant (9 and 9), we can consider overall time complexity as O(1)
# Space Complexity : O(n*m) - n is the number of rows and m is the number of cols
# Since n and m are constant (9 and 9), we can consider overall space complexity as O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""

Maintain a list of sets for rows
Maintain a list of sets for columns
Maintain a hashmap with key as (r/3,c/3) and value as a set

As (r/3.c/3) would be unique for each of the 9 boxes, we can use that as the key for the hashmap

Iterate through the board and if the value is already there in that row or column or box then return False
If no violation then return true at the end

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9

        rows = [set() for _ in range(0,n)]
        cols = [set() for _ in range(0,n)]
        boxes = {}

        for i in range(0,n):
            for j in range(0,n):
                value = board[i][j]
                if value == ".":
                    continue

                r = i//3
                c = j//3
                k = str(r) + "," + str(c)

                if value in rows[i] or value in cols[j] or (k in boxes and value in boxes[k]):
                    return False
                
                rows[i].add(value)
                cols[j].add(value)
                if k in boxes:
                    boxes[k].add(value)
                else:
                    boxes[k] = set()
                    boxes[k].add(value)
        return True









