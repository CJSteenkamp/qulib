import numpy as np

class I:
    def __init__(self):
        self.matrix = np.eye(2)

    def __call__(self):
        return self.matrix

    def __str__(self):
        return "I"

class X:
    def __init__(self):
        self.matrix = np.array([[0, 1], 
                                [1, 0]])

    def __str__(self):
        return "X"
    
class Z:
    def __init__(self):
        self.matrix = np.array([[1, 0], 
                                [0, -1]])

    def __str__(self):
        return "Z"
    
class Y:
    def __init__(self):
        self.matrix = np.array([[0, -1j], 
                                [1j, 0]])

    def __str__(self):
        return "Y"
    
class H:
    def __init__(self):
        self.matrix = np.array(np.array([[1, 1], 
                                         [1, -1]]) / np.sqrt(2)).astype(complex)

    def __str__(self):
        return "H"

class RX:
    def __init__(self, theta):
        # theta is in rads
        sin = np.sin(theta / 2)
        cos = np.cos(theta / 2)
        self.matrix = np.array([[cos, -1j * sin], 
                                [-1j * sin, cos]])

    def __str__(self):
        return "RX"

class RY:
    def __init__(self, theta):
        # theta is in rads
        sin = np.sin(theta / 2)
        cos = np.cos(theta / 2)
        self.matrix = np.array([[cos, -sin], 
                                [sin, cos]])

    def __str__(self):
        return "RY"
    
class RZ:
    def __init__(self, theta):
        # theta is in rads
        self.matrix = np.array([[np.exp(-1j * (theta / 2)), 0], 
                                [0, np.exp(1j * (theta / 2))]])

    def __str__(self):
        return "RZ"

class S:
    def __init__(self, dagger=None):
        if dagger:
            self.matrix = np.array([[1, 0], 
                                    [0, -1j]])
        else:
            self.matrix = np.array([[1, 0], 
                                    [0, 1j]])

    def __str__(self):
        return "S"

class T:
    def __init__(self, dagger=None):
        if dagger:
            self.matrix = np.array([[1, 0], 
                                    [0, np.exp((-1j * np.pi) / 4)]])
        else:
            self.matrix = np.array([[1, 0], 
                                    [0, np.exp((1j * np.pi) / 4)]])
        

    def __str__(self):
        return "T"

class CNOT:
    def __init__(self, fliped=False):
        if fliped:
            self.matrix = np.array([[1, 0, 0, 0], 
                                    [0, 0, 0, 1], 
                                    [0, 0, 1, 0], 
                                    [0, 1, 0, 0]])
        else:
            self.matrix = np.block([[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 1],
                                    [0, 0, 1, 0]]).astype(int)

    def __str__(self):
        return "CNOT"

class CCNOT:
    def __init__(self):
        self.matrix = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0, 0, 1, 0]])                  

    def __str__(self):
        return "CCNOT"

class SWAP:
    def __init__(self, fliped=False):
        self.matrix = np.array([[1, 0, 0, 0], 
                                [0, 0, 1, 0], 
                                [0, 1, 0, 0], 
                                [0, 0, 0, 1]])

    def __str__(self):
        return "SWAP"