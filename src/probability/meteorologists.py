import numpy as np
# Input:
# - prior[i]: the prior belief in model i
# - likelihood[D][i]: the probability of the data D given model i.
# - D: the data (in this case an integer)
# Reurn:
# - posterior[i]: the posterior belief in model i, given the data
def get_posterior(prior, likelihood, D):
    print(likelihood[D])
    factors = prior * likelihood[D]
    posterior = factors / np.sum(factors)
    return posterior

prior = np.array([0.5, 0.25, 0.25])
n_events = 2 # 1 = rain, 0 = no rain
n_models = len(prior)
likelihood = np.zeros([n_events, n_models])

# initialise the probabilities of rain
likelihood[1][0] = 0.25
likelihood[1][1] = 0.3
likelihood[1][2] = 0.9

# also the probabilities of no rain
for i in range(n_models):
    likelihood[0][i] = 1- likelihood[1][i]


print(prior)
prior = get_posterior(prior, likelihood, 1)
print(prior)
prior = get_posterior(prior, likelihood, 0)
print(prior)
prior = get_posterior(prior, likelihood, 0)
print(prior)
prior = get_posterior(prior, likelihood, 1)
print(prior)
