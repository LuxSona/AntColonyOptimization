import numpy as np
import numpy.typing as npt

#Travelling Salesman Problem 
class TravellingSalesmanProblem():
    """
    Creates an instance of the Travelling Salesman Problem

    :param distances: An nxn (where n is the length of the number of cities) describing distances between col and row.
    :type distances: npt.NDArray[np.float64] 
    """
    def __init__(self, distances: npt.NDArray[np.float64]):
        self.distances = distances
    


if __name__ == "__main__":
    # Sample: [Denver, Albuquerque, Santa Fe, Las Vegas, Elko]
    distances = np.array([
        [0,545,453,971,878],
        [545,0,94,774,1003],
        [453,94,0,838,1019],
        [971,774,839,0,527],
        [878,1003,1019,527,0],
        ])
    
    problem = TravellingSalesmanProblem(distances)
