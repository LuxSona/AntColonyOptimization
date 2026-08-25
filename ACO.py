import numpy as np
import numpy.typing as npt
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
        if n_ants < 0 or pheromone_weight < 0 or heuristic_weight < 0 or evaporation_rate < 0 or Q < 0:
            raise ValueError("Negative values for any hyperparameters are not allowed. Double check all of your hyperparameters.")
        
        self.tsp: TravellingSalesmanProblem  = TSP
        self.tsp_size : int = self.tsp.n
        self.n_ants: int = n_ants
        self.pheromone_weight : float = pheromone_weight
        self.heuristic_weight : float = heuristic_weight
        self.evaporation_rate : float = evaporation_rate
        self.Q : float = Q
        #Set up pheromones
        self.pheromones = np.ones((self.tsp_size, self.tsp_size))
    

    def ant_tours(self) -> tuple[npt.NDArray[np.float64], list[tuple[int, int]], float]:
        '''
        Docstring for ant_tours

        :return: A tuple of the pheromone update, the best route from the ants, and the best length from all the ants.
        :rtype: tuple[NDArray[float64], list[int], float]
        '''
        total_update : npt.NDArray[np.float64] = np.zeros(shape=((self.tsp_size, self.tsp_size)))
        best_length : float = float("inf")
        best_route : list[tuple[int, int]] = []
        for _ in range(self.n_ants):
            #Individual update for ants
            path : list[tuple[int, int]] = []
            indices = np.array([i for i in range(self.tsp_size)])
            #initial starting location
            current_location : int = np.random.choice(indices)
            starting_city: int = current_location

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
            
            if indices.size == 0:
                #An ant exhausted all the cities, so we can add the edge from current location to starting location.
                path.append((current_location, starting_city))
                length += self.tsp.distances[current_location,starting_city]
            

            if length == 0:
                continue
            for update in path:
                updx, updy = update
                total_update[updx, updy] += self.Q / length 
            
            if length < best_length:
                best_length = length
                best_route = path 

        return total_update, best_route, best_length


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

    def iterate(self, n_iterations: int) -> tuple[list[tuple[int, int]], float]:
        '''
        Docstring for iterate

        :param n_iterations: Number of iterations
        :type n_iterations: int
        :return: The pheromone update, best path, and best path length.
        :rtype: tuple[list[tuple[int, int]], float]
        '''
        if type(n_iterations) != int:
            raise ValueError("Iterations are not of type int")
        
        if n_iterations < 0:
            raise ValueError("Iterations cannot be less than 0")
        
        best_path : list[tuple[int, int]] = []
        best_length : float  = float("inf")
        for iteration in range(n_iterations):
            delta_txy, path, length = self.ant_tours()
            if length < best_length:
                best_length = length
                best_path = path
            self.update_pheromones(delta_txy)
        
        return best_path, best_length
    