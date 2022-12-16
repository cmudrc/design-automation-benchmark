import problems

def solve(problem, algorithm):
    """This does the heavy lifting - its where the problem and the algorithm come together"""  
    import scipy.optimize
    if algorithm=='SLSQP' or algorithm=='trust-constr':
        return scipy.optimize.minimize(
            problem.objective, # function is the problem's objective function
            problem.initial_solution,  # intial solution is also defined in the problem
            method=algorithm, # just a string input for right now
            bounds=problem.bounds, # get bounds from problem
            constraints=problem.constraints # get constraints from problem
        )
    else:
        raise ValueError("The input is not one of `SLSQP` and `trust-constr`") # currently only these two solvers work
