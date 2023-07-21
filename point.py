
import numpy as np


class Point:
    '''
    Point 4D for hypercube
    '''

    def __init__(self, x: int, y: int, z: int, w: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def mult(self, scale) -> None:
        self.x *= scale
        self.y *= scale
        self.z *= scale
        self.w *= scale

    @property
    def matrix(self) -> np.ndarray:
        '''Return matrix.
         [
             [], [], [], []
         ]
        '''
        return np.array([[self.x], [self.y], [self.z], [self.w]])

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z}, {self.w})"


class Point3D:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def mult(self, scale) -> None:
        self.x *= scale
        self.y *= scale
        self.z *= scale

    @property
    def matrix(self) -> np.ndarray:
        '''Return matrix.
         [
             [], [], []
         ]
        '''
        return np.array([[self.x], [self.y], [self.z]])
