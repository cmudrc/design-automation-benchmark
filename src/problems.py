import scipy.optimize # Used for solvers
import math # Used for pi value
import numpy # for random array generation

def _pill_volume(radius, length):
    """Calculates pill volume, simple helper function"""
    return 4.0/3.0*math.pi*radius**3 + length*math.pi*radius**2

def _pill_area(radius, length):
    """Calculates pill area, simple helper function"""
    return 2*math.pi*radius*length + 4*math.pi*radius**2

class Pill:
    """Class to contain all pill knowledge""" 
    def __init__(self, name="pill", required_volume=1e-06):
        self.name = name
        self.required_volume = required_volume
        self.bounds = scipy.optimize.Bounds([0.0, 0.0], [1.0, 1.0])
        self.constraints = [
            scipy.optimize.NonlinearConstraint(
                lambda x: _pill_volume(x[0], x[1]), 
                self.required_volume, 
                self.required_volume
                )
            ]
        
    def generate_initial_solution(self):
        return numpy.random.rand(2)

    def objective(self, variables):
        """Objective function, pill area"""
        return _pill_area(variables[0], variables[1])

    def generate_data(self, n=1000):
        """Generate data containing x, an array of design variables, and y, an 
        array of objective function values"""
        x = numpy.random.random((n, len(self.initial_solution)))
        y = numpy.random.random((n, 1))
        for i in range(x.shape[1]):
            x[:, i] = x[:, i] * (self.bounds.ub[i] - self.bounds.lb[i]) + self.bounds.lb[i]
        for i in range(x.shape[0]):
            y[i] = self.objective(x[i, :])
        return x, y

    def load_data(self):
        """Loads a curated dataset for this problem, either associated with an 
        experiment or a specific data generation process."""
        raise NotImplementedError("There is no dataset available for this problem.") # <<<< For other problems (e.g., LINKS), this function would load hte available dataset.
