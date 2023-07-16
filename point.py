
import numpy as np


class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def matrix(self) -> np.ndarray:
        '''Return matrix.
         [
             [], [], []
         ]
        '''
        return np.array([[self.x], [self.y], [self.z]])
