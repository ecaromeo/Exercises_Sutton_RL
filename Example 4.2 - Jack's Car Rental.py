import numpy as np
import matplotlib.pyplot as plt
import random

class JackRental():
    def __init__(self) -> None:
        self.gamma = 0.9
        self.reset()

    def reset(self):
        self.crnt_state = [random.randint(0,20), random.randint(0,20)]
        self.actn = 0
        self.rqst = np.array([0, 0])
        self.rtn = np.array([0, 0])
        self.tt_rwrd = 0
        

    def step(self, actn):
        if abs(actn) > 5:
            actn = np.sign(actn) * 5
        # Rewards for the past action
        reward = (10 * np.min([self.crnt_state[0], self.rqst[0]])
        + 10 * np.min([self.crnt_state[1], self.rqst[1]])
        - 2 * self.actn)

        # New state depends on the request of cars and the number of returns of the day
        # before.
        self.rqst = np.array([np.random.poisson(lam=3), np.random.poisson(lam=4)])
        new_state = self.crnt_state + self.rtn - self.rqst
        new_state = np.clip(np.array([new_state[0] - actn, new_state[1] + actn]), 0,20)
        self.rtn = np.array([np.random.poisson(lam=3), np.random.poisson(lam=2)])
        self.actn = actn

        return reward, new_state
    
    def policy(self):
        actn = np.random.randint(-5, 5)     # random policy
        actn = 0                            # Do nothing
        return actn
    
    def run(self):
        for i in range(100):
            actn = self.policy()
            rwrd, self.crnt_state = self.step(actn)
            self.tt_rwrd = rwrd + self.gamma* self.tt_rwrd
    

if __name__ == "__main__":
    myRental = JackRental()
    myRental.run()



