
from re import S


class Point:
    def __init__(self, x: int, y: int, z: int, w: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @property
    def matrix(self) -> list[float]:
        '''Return matrix.
         [
             [], [], [], []
         ]
        '''
        return [[self.x], [self.y], [self.z], [self.w]]
