import dab.problems
import dab.algorithms


def solve(problem, algorithm):
    """This does the heavy lifting - its where the problem and the algorithm come together"""  
    import scipy.optimize
    if type(algorithm)==dab.algorithms.SLSQP or type(algorithm)==dab.algorithms.TrustConstr:
        return scipy.optimize.minimize(
            problem.objective, # function is the problem's objective function
            problem.initial_solution,  # intial solution is also defined in the problem
            method=algorithm.name, # just a string input for right now
            bounds=problem.bounds, # get bounds from problem
            constraints=problem.constraints # get constraints from problem
        )
    else:
        raise ValueError("The algorithm is not one of `SLSQP` and `trust-constr`") # currently only these two solvers work

        
def solve_matrix(problems, algorithms):
    """This does the even heavier lifting - it runs matrices of problems against matrices of algorithms"""
    results = []
    for algorithm in algorithms:
        for problem in problems:
            result = dab.solve(problem, algorithm)
            results.append(result)
    return results

