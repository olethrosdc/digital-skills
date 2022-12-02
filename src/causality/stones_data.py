# generate data
import numpy as np
def generate_data(n_data = 100000, p_large_stones = 0.2, P_A_small = 0.9, P_A_large = 0.2, P_cure_A_small = 0.8, P_cure_A_large = 0.3, P_cure_B_small = 0.9, P_cure_B_large = 0.6):
    stone_size = np.random.choice(2, p = [1 - p_large_stones, p_large_stones], size = n_data)
    treatment = np.zeros(n_data)
    cured = np.zeros(n_data)
    P_cure = np.zeros([2,2])
    P_cure[0,0] = P_cure_A_small
    P_cure[0,1] = P_cure_B_small
    P_cure[1,0] = P_cure_A_large
    P_cure[1,1] = P_cure_B_large
    for t in range(n_data):
        P_A = 0.2 # P_A_small * (1 - stone_size[t]) + P_A_large * stone_size[t]
        treatment[t] = np.random.choice(2, p = [P_A, 1 - P_A])
        P_cure_t = P_cure[stone_size[t], int(treatment[t])]
        cured[t] = np.random.choice(2, p = [1 - P_cure_t, P_cure_t])
    return stone_size, treatment, cured
