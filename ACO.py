import numpy as np
import numpy.typing as npt
import random 
from TSP import TravellingSalesmanProblem



class ACO:
    """
    ACO Class, implements the Ant Colony Optimization function on a Travelling Salesman Problem

    :param TSP: An instance of the Travelling Salesman Problem for the ants to solve.
    :type TSP: Travelling Salesman Problem
    :param n_ants: The Number of ants, effectively the number of solutions to solve.
    :type n_ants: Integer
    :param pheromone_weight: The weight of the pheromones.
    :type pheromone_weight: float
    :param heuristic_weight: The weight of the heuristic (typically a distance/cost metric)
    :type heuristic_weight: float
    :param evaporation_rate: How much each pheromone fades, which may encourage the exploration/exploitation rates
    :type evaporation_rate: float
    :param Q: How much pheromone is deposited
    :type Q: float
    """
    def __init__(self, TSP : TravellingSalesmanProblem, n_ants : int, pheromone_weight: float, heuristic_weight: float, evaporation_rate: float, Q : float):
        self.tsp: TravellingSalesmanProblem  = TSP
        self.tsp_size : int = self.tsp.n
        self.n_ants: int = n_ants
        self.pheromone_weight : float = pheromone_weight
        self.heuristic_weight : float = heuristic_weight
        self.evaporation_rate : float = evaporation_rate
        self.Q : float = Q
        #Set up pheromones
        self.pheromones = np.ones((self.tsp_size, self.tsp_size))
    

    def ant_tours(self, iterations : int) -> npt.NDArray[np.float64]:
        '''
        Runs an iterations number of ant tours.

        :param iterations: The number of iterations for each ant to go through
        :type iterations: int
        :return: Returns the change in pheromones
        :rtype: NDArray[float64]
        '''
        total_update : npt.NDArray[np.float64] = np.zeros(shape=((self.tsp_size, self.tsp_size)))

        #For each iteration
        for iteration in range(iterations):
            for ant in range(self.n_ants):
                #Individual update for ants
                path = []
                indices = np.array([i for i in range(self.tsp_size)])
                #initial starting location
                current_location : int = np.random.choice(indices)
                length = 0
                while indices.size != 0:
                    indices = indices[indices != current_location]
                    #Get the available destinations from the tsp
                    # NOTE - Keep indices monotonically increasing. See comment by probs calculations
                    mask = np.zeros(self.tsp_size, dtype=bool)
                    mask[indices] = True  
                    #Get destinations from here
                    destinations_from_here = self.tsp.get_linked_destinations(current_location)[mask]
                    if destinations_from_here.size == 0:
                        #We have no more destinations and may break
                        break
                    #Else, select an edge from the edge selection formula
                    eta = 1 / destinations_from_here ** self.heuristic_weight #type: ignore
                    tau = self.pheromones[current_location][mask] ** self.pheromone_weight

                    if np.sum(tau*eta) == 0:
                        #If the sum is zero
                        probs = np.ones(len(destinations_from_here)) / len(destinations_from_here)
                    else:
                        probs = tau*eta / np.sum(tau*eta)
                    
                    # NOTE - Keep indices monotonically increasing. This next location calculation relies on Mask and Indices coinciding. IF we shuffle, re-order, or append indices, we risk misaligning probs and our available locations.
                    # TODO - Eliminate the dependency between monotonically increasing indices and the mask.
                    next_location : int = np.random.choice(indices, p = probs)
                    #Get the index of the current location and the next location

                    distance : float = self.tsp.distances[current_location, next_location]

                    path.append((current_location, next_location))
                    length += distance 
                    current_location = next_location
                
                if length == 0:
                    continue
                for update in path:
                    updx, updy = update
                    total_update[updx, updy] += self.Q / length 
            
        return total_update


    def update_pheromones(self, delta_txy : npt.NDArray[np.float64]):
        '''
        Updates the pheromones in our pheromone array.
        Pheromones are determined by the following equation:

        txy <- (1-rho) * txy + sum^m _k dtxyk
        variables:
            rho = pheromone evaporation coefficient
            m is the number of ants
            k is an iterator for the kth ant
            dtxyk is the change in pheromone from ant k at spot xy
        
        The sum is easy. It'll be represented during the pheromone step naturally, so there's no summation required in this function

        :param delta_txy: The change in pheromones
        :type delta_txy: NDArray[float64]
        '''

        rho = self.evaporation_rate
        self.pheromones = (1-rho) * self.pheromones + delta_txy

