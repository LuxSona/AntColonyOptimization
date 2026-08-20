import numpy as np
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
    """
    def __init__(self, TSP : TravellingSalesmanProblem, n_ants : int, pheromone_weight: float, heuristic_weight: float, evaporation_weight: float):
        self.tsp = TSP
        self.n_ants = n_ants
        self.pheromone_weight = pheromone_weight
        self.heuristic_weight = heuristic_weight
        self.evaporation_rate = self.evaporation_rate
    

    