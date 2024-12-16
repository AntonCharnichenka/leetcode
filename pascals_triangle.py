class Solution:
    '''Straigh forward'''
    def generate(self, numRows: int) -> list[list[int]]:
        result: list[list[int]] = []
        
        for n in range(numRows):
            if n == 0:
                result.append([1])
            elif n == 1:
                result.append([1, 1])
            else:
                previous_row = result[-1]
                row = [1] * (len(previous_row) + 1)
                for i in range(1, len(row) - 1):
                    row[i] = previous_row[i-1] + previous_row[i]
                
                result.append(row)
        
        return result


class Solution:
    '''Recursion'''
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        previous_rows = self.generate(numRows-1)
        
        final_row = [1] * numRows
        for i in range(1, numRows - 1):
            final_row[i] = previous_rows[-1][i - 1] + previous_rows[-1][i]
        
        previous_rows.append(final_row)

        return previous_rows


print(Solution().generate(5))
