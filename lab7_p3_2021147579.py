
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self, arr):
        ### YOUR CODE HERE ###
        if not all(isinstance(row, list) for row in arr):
            raise not2DError()

        if len(arr) > 0:
            row_length = len(arr[0])
            for row in arr:
                if len(row) != row_length:
                    raise unevenListError()
        else:
            pass
        ######

        self.extend(arr)

    def __str__(self):
        ### YOUR CODE HERE ###
        rows = len(self)
        cols = len(self[0]) if rows > 0 else 0
        return f'list_2D: {rows}*{cols}'
        ######

    def transpose(self):
        ### YOUR CODE HERE ###
        # Transpose the matrix: shape (n, m) -> (m, n)
        if len(self) == 0:
            return list_D2([])
        transposed = list(map(list, zip(*self)))
        return list_D2(transposed)


    def __matmul__(self, others):
        ### YOUR CODE HERE ###
        # Matrix multiplication: (n x m) @ (p x q) = (n x q) if m == p
        n = len(self)
        m = len(self[0]) if n > 0 else 0
        p = len(others)
        q = len(others[0]) if p > 0 else 0

        if m != p:
            raise improperMatrixError()
        others_T = others.transpose()
        result = []
        for i in range(n):
            row_result = []
            for j in range(q):
                row_result.append(mul1d(self[i], others_T[j]))
            result.append(row_result)

        return list_D2(result)
        ######

    def avg(self):
        ### YOUR CODE HERE ###
        total_sum = 0
        count = 0
        for row in self:
            for val in row:
                total_sum += val
                count += 1
        return total_sum / count if count > 0 else 0.0
        ######
