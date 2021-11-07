import numpy as np
import matplotlib.pyplot as plt
import random

crnt_state = [ random.randint(0,20), random.randint(0,20)]
def action(crnt_state, move):
    """!
    @param crnt_state List of cars in Location 0 and 1 respectively.
    @param move Number of cars moved from Location 0 to Location 1.
    """
    rqst0 = np.random.poisson(lam=3)
    rqst1 = np.random.poisson(lam=4)
    rtn0 = np.random.poisson(lam=3)
    rtn1 = np.random.poisson(lam=2)

    reward = (10 * np.min([crnt_state[0], rqst0])
              + 10 * np.min([crnt_state[1], rqst1])
              - 2 * previous_move)

