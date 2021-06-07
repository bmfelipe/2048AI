def canMoveUp(self) -> bool:
    for j in range(4):
        k = -1
        for i in range(3, -1, -1):
            if self.matrix[i][j] > 0:
                k = i
                break
        if k > -1:
            for i in range(k, 0, -1):
                if self.matrix[i-1][j] == 0 or self.matrix[i][j] == self.matrix[i-1][j]:
                    return True
    return False