import numpy as np

n_pop = 10000000 # population
n_inf = 10 # current number of infections
n_imm = 0 # current number of immune people
n_death = 0 # current number of dead
R_zero = 3 # basic reproduction rate
R_reinfect = 1.2 # reinfection rate
R_cure = 0.1 # cure rate
R_death = 0.001 # death rate
P_sym_if_inf = 0.5 #probability of symptoms if infected
P_test_if_sym = 0.01 # probability of getting tested if symptomatic (daily)
P_test_if_not_sym = 0.01 # probability of getting tested if non-symptomatic (regardless of being infected)
P_positive_if_inf = 0.5 # probability of a positive test if infected
P_positive_if_not_inf = 0.001 # probability of a positive test if not infected

T = 180
n_infections = np.zeros(T)
n_deaths = np.zeros(T)
n_tests = np.zeros(T)
n_positive_tests = np.zeros(T)
print("deaths,positive,tests")
for t in range(T):
    n_infections[t] = n_inf # record the (unknown) number of infections
    n_sym = np.random.binomial(n_inf, P_sym_if_inf) # the number of symtomatic people is random
    n_nonsym = n_pop - n_sym # the remaining people are not symptomatic

    ## Let us first look at the infected symptomatic people
    n_tests_inf = np.random.binomial(n_sym, P_test_if_sym) # number of tests made by symptomatic
    n_pos = np.random.binomial(n_tests_inf, P_positive_if_inf) # the number of positive test

    ## Let us now look at the infected, non-symptomatic people
    n_tests_inf_not_sym = np.random.binomial(n_inf - n_sym, P_test_if_not_sym) # number of tests made by non-symptomatic infected people
    n_pos += np.random.binomial(n_tests_inf_not_sym, P_positive_if_inf)

    ## Let us now look at the remaining people, who are not infected
    n_tests_not_inf = np.random.binomial(n_pop - n_inf, P_test_if_not_sym) # number of tests made by non-infected people
    n_pos += np.random.binomial(n_tests_not_inf, P_positive_if_not_inf)

    ## add up the number of all tests made
    n_tests = n_tests_inf + n_tests_inf_not_sym + n_tests_not_inf
    
    #print(n_inf, n_pos, n_tests, n_pos/n_tests)

    # how many people will die this round
    n_death = np.random.binomial(n_inf, R_death)
    n_pop -= n_death # reduce the population!

    n_cured = np.random.binomial(n_inf, R_cure)
    n_imm += n_cured
    R_immune = (n_imm + n_inf) / n_pop
    
    R_tr = R_zero * (1 - R_immune) + R_reinfect * R_immune
    n_inf = round(n_inf * R_tr) - n_cured# multiply the infected people

    print("%d,%d,%d" % (n_death, n_pos, n_tests))

