import numpy as np
import numpy.typing as npt


#Travelling Salesman Problem 
class TravellingSalesmanProblem():
    """
    Creates an instance of the Travelling Salesman Problem
    :param labels: An n length set of labels for each city..
    :type labels: lost[str],

    :param distances: An nxn (where n is the length of the number of cities) describing distances between row to cols. A value of float(inf) DISABLES that connection
    :type distances: npt.NDArray[np.float64] 
    """
    def __init__(self, labels: list[str], distances: npt.NDArray[np.float64]):
        self.distances : npt.NDArray[np.float64] = distances
        self.labels : list[str] = labels
        self.n : int = len(labels)
        self.labels_to_indices = {label : idx for idx, label in enumerate(labels)}
        self.indices_to_labels = {idx: label for idx, label in enumerate(labels)}
    

    
    def get_linked_destinations(self, index : int) -> npt.NDArray[np.float64]:
        '''
        Docstring for get_linked_destinations

        :param self: Description
        :param label: Description
        :type label: str
        :return: Description
        :rtype: ndarray[float64, dtype[Any]]
        '''
        

        return self.distances[index]

if __name__ == "__main__":
    # Sample: [Denver, Albuquerque, Santa Fe, Las Vegas, Elko]
    distances = np.array([
        [0,545,453,971,878],
        [545,0,94,774,1003],
        [453,94,0,838,1019],
        [971,774,839,0,527],
        [878,1003,1019,527,0],
        ])
    labels = ["Denver", "Albuquerque", "Santa Fe", "Las Vegas", "Elko"]
    problem = TravellingSalesmanProblem(labels, distances)
