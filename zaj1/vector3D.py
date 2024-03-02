from math import sqrt

import numpy as np


class Vector3D:
    def __init__(self, x, y ,z) -> None:
        self.x = x 
        self.y = y
        self.z = z
    def __str__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    def norm(self):
        return sqrt((self.x^2) + (self.y^2) + (self.z^2))
                    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def cross(self, other):
        x = [self.x, self.y, self.z]
        y = [other.x, other.y, other.z]
        result = np.cross(x, y)
        return Vector3D(result[0], result[1], result[2])
    @staticmethod
    def are_orthogonal(self, other):
        if self.dot(other) == 0:
            return True
        return False